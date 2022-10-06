import lec as lc
import logging
from config import TOKEN
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем константы этапов разговора
CHOICE, OPERATIONS_RATIONAL, OPERATIONS_COMPLEX = range(3)
    

# функция обратного вызова точки входа в разговор


def start(update, _):
    update.message.reply_text(
        'Добро пожаловать в телефонный справочник. Выберите нужный вариант.\n'
        'Команда /cancel, чтобы прекратить разговор.\n\n')
    update.message.reply_text(
        '1 - поиск информации по фамилии: \n2 -поиск информации по номеру телефона: \n3 - для выхода \n')
    return CHOICE


def choice(update, context):
    user = update.message.from_user
    logger.info("Выбор операции: %s: %s", user.first_name, update.message.text)
    user_choice = update.message.text
    if user_choice in '123':
        if user_choice == '1':
            update.message.reply_text(
                'Введите Фамилию')
           
            return OPERATIONS_RATIONAL
        if user_choice == '2':
            context.bot.send_message(
                update.effective_chat.id, 'Введите номер телефона: ')
            return OPERATIONS_COMPLEX
    else:
        update.message.reply_text('Это не то.\n 1 - поиск информации по фамилии: \n2 - поиск информации по телефону: \n3 - для выхода \n')

# def rational_one(update, context):
#     user = update.message.from_user
#     logger.info("Пользователь ввел фамилию: %s: %s", user.first_name, update.message.text)
#     get_rational = update.message.text
#     # if get_rational.isdigit():
#     #     get_rational = float(get_rational)
#         context.user_data['rational_one'] = get_rational
#         update.message.reply_text(
#             'Введите второе рациональное')
#         return RATIONAL_TWO

    # else:
    #     update.message.reply_text(
    #         'Нужно ввести число')


# def rational_two(update, context):
#     user = update.message.from_user
#     logger.info("Пользователь ввел число: %s: %s", user.first_name, update.message.text)
#     get_rational = update.message.text
#     if get_rational.isdigit():
#         get_rational = float(get_rational)
#         context.user_data['rational_two'] = get_rational
#         update.message.reply_text(
#             'Выберите операцию с числами: \n\n+ - для сложения: \n- - для вычетания: \n* - для умножения: \n/ - для деления: \n')
#         return OPERATIONS_RATIONAL


def operatons_rational(update, context):
    # user = update.message.from_user
    # logger.info(
    #     "Пользователь выбрал операцию %s: %s", user.first_name, update.message.text)
    # # rational_one = context.user_data.get('rational_one')
    # rational_two = context.user_data.get('rational_two')
    user_choice = update.message.text

    if user_choice in lc.stud_card['Фамилия']:
        index = lc.stud_card['Фамилия'].index(user_choice)
        result = (f"{lc.stud_card['ID'][index]}, {lc.stud_card['Имя'][index]}, {lc.stud_card['Фамилия'][index]},\n {lc.stud_card['Дата рождения'][index]}, {lc.stud_card['Телефон'][index]}")
        update.message.reply_text( f'Результат: {result}')
        return ConversationHandler.END
    else:
        update.message.reply_text('Это не то')
    # if user_choice in '+-/*':
    #     if user_choice == '+':
    #         result = rational_one + rational_two
    #     if user_choice == '-':
    #         result = rational_one - rational_two
    #     if user_choice == '*':
    #         result = rational_one * rational_two
    #     if user_choice == '/':
    #         try:
    #             result = rational_one / rational_two
    #         except:
    #             update.message.reply_text('Деление на ноль запрещено')
    #     update.message.reply_text(
    #         f'Результат: {rational_one} + {rational_two} = {result}')
    #     return ConversationHandler.END
    # else:
    #     update.message.reply_text('Это не то.Введите +-*/')

# def complex_one(update, context):
#     user = update.message.from_user
#     logger.info(
#         "Пользователь ввел телефон %s: %s", user.first_name, update.message.text)
#     user_choice = update.message.text
#     test = user_choice.replace('-', '')
#     if ' ' in test and (test.replace(' ', '')).isdigit():
#         user_choice = user_choice.split(' ')
#         complex_one = complex(int(user_choice[0]), int(user_choice[1]))
#         context.user_data['complex_one'] = complex_one
#         update.message.reply_text(
#             f'Первое число {complex_one},  Введите Re и Im второго числа через ПРОБЕЛ: ')
#         return COMPLEX_TWO
#     else:
#         update.message.reply_text('Это не то. Введите Re и Im первого числа через ПРОБЕЛ')


# def complex_two(update, context):
#     user = update.message.from_user
#     logger.info(
#         "Пользователь ввел число %s: %s", user.first_name, update.message.text)
#     user_choice = update.message.text
#     test = user_choice.replace('-', '')
#     if ' ' in test and (test.replace(' ', '')).isdigit():
#         user_choice = user_choice.split(' ')
#         complex_two = complex(int(user_choice[0]), int(user_choice[1]))
#         context.user_data['complex_two'] = complex_two
#         update.message.reply_text(
#             f'Второе число {complex_two}, Выберите операцию с цислами: \n\n+ - для сложения: \n- - для вычетания: \n* - для умножения: \n/ - для деления: \n')
#         return OPERATIONS_COMPLEX
#     else:
#         update.message.reply_text('Это не то. Введите Re и Im второго числа через ПРОБЕЛ')

def operatons_complex(update, context):
    # user = update.message.from_user
    # logger.info(
    #     "Пользователь выбрал операцию %s: %s", user.first_name, update.message.text)
    # complex_one = context.user_data.get('complex_one')
    # complex_two = context.user_data.get('complex_two')
    user_choice = update.message.text
    if user_choice in lc.stud_card['Телефон']:
        index = lc.stud_card['Телефон'].index(user_choice)
        result = (f"{lc.stud_card['ID'][index]}, {lc.stud_card['Имя'][index]}, {lc.stud_card['Фамилия'][index]},\n {lc.stud_card['Дата рождения'][index]}, {lc.stud_card['Телефон'][index]}")
        update.message.reply_text(f'Результат: {result}')
        return ConversationHandler.END
    else:
        update.message.reply_text('Это не то')

def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.',
    )
    return ConversationHandler.END


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler`
    # с состояниями CHOICE, RATIONAL_ONE, RATIONAL_TWO, OPERATIONS_RATIONAL, OPERATIONS_COMPLEX, COMPLEX_ONE, COMPLEX_TWO
    conversation_handler = ConversationHandler(  # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            CHOICE: [MessageHandler(Filters.text, choice)],
            OPERATIONS_RATIONAL: [MessageHandler(Filters.text, operatons_rational)],
            OPERATIONS_COMPLEX: [MessageHandler(Filters.text, operatons_complex)],
            
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conversation_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()