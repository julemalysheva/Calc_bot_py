from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    MessageHandler,
    Filters,
)
from bot_commands import *
import config


# Этапы/состояния разговора
FIRST, SECOND, CALC = range(3)
# Данные обратного вызова
ONE, TWO = range(2)

updater = Updater(config.Token)
dispatcher = updater.dispatcher

# Настройка обработчика разговоров с состояниями `FIRST` и `SECOND`
# Используем параметр `pattern` для передачи `CallbackQueries` с
# определенным шаблоном данных соответствующим обработчикам
# ^ - означает "начало строки"
# $ - означает "конец строки"
# Таким образом, паттерн `^ABC$` будет ловить только 'ABC'
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={  # словарь состояний разговора, возвращаемых callback функциями
        FIRST: [
              CallbackQueryHandler(input_data, pattern='^' + str(ONE) + '$'),
              CallbackQueryHandler(view_log, pattern='^' + str(TWO) + '$'),
        ],
        CALC: [MessageHandler(Filters.text & ~Filters.command, view_result)],
        SECOND: [
            CallbackQueryHandler(start_over, pattern='^' + str(ONE) + '$'),
            CallbackQueryHandler(end, pattern='^' + str(TWO) + '$'),
        ],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)

# Добавляем `ConversationHandler` в диспетчер, который
# будет использоваться для обработки обновлений
dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()
