import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from main import TaskMaker

TOKEN_API = "6242888980:AAE4OW9MpMnR5vEo4AuVI0n9WpmZ-9OeED0"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage=MemoryStorage())

tm = TaskMaker()


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    keyboard = [[types.KeyboardButton(text="Видати завдання")]]
    reply_markup = types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

    await message.answer(
        "Привіт! " + message.from_user.first_name + "\nЯ бот, який допомагає підготуватися до КРОК і оціню твої знання"
        "\nДодаткова інформація /info",
        reply_markup=reply_markup)


@dp.message_handler(Text(equals="Видати завдання"))
async def process_poll_answer(message: types.Message):
    task = tm.get_task()

    await bot.send_poll(message.chat.id, question=task.task, options=task.options, correct_option_id=task.right_option,
                        type=types.PollType.QUIZ, is_anonymous=False)


@dp.message_handler(commands=['reference_list'])
async def reference_list(message: types.Message):
    button = InlineKeyboardButton("Показати більше", callback_data="show_more")

    keyboard = InlineKeyboardMarkup()
    keyboard.add(button)

    await message.answer("Літератури для підготовки до КРОК:"
                         "\n1) Медична енциклопедія В. П. Васильєва, С. М. Савченко, В. Г. Трифонова."
                         "\n\n2) Судинна хірургія Е. Н. Гапонов-Петровський."
                         "\n\n3) Основи внутрішньої медицини А. А. Корольков."
                         "\n\n4) Основи хірургії М. А. Крутевич, І. С. Ямпольський, О. Є. Єременко."
                         "\n\n5) Фармакологія з основами фармацевтичної технології М. М. Поліщук, І. П. Засенко.",
                         reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data == 'show_more')
async def list_users(query: types.CallbackQuery):
    await query.message.answer("Літератури для підготовки до КРОК:"
                               "\n1) Медична енциклопедія В. П. Васильєва, С. М. Савченко, В. Г. Трифонова. Це комплексний довідник з усіма основними медичними темами, які вам знадобляться для підготовки до КРОК. Книга містить як теоретичні, так і практичні матеріали."
                               "\n\n2) Судинна хірургія Е. Н. Гапонов-Петровський. Це підручник, який присвячений основам судинної хірургії. Він містить докладні описи профільних захворювань, діагностику, лікування і ускладнення, пов'язані з цією галуззю."
                               "\n\n3) Основи внутрішньої медицини А. А. Корольков. Ця книга розглядає основи внутрішньої медицини, звертаючи увагу на клінічні симптоми, діагностику та лікування хвороб. Вона містить комплексний підхід до вивчення внутрішніх органів та систем організму."
                               "\n\n4) Основи хірургії М. А. Крутевич, І. С. Ямпольський, О. Є. Єременко. Цей підручник охоплює основи загальної хірургії, включаючи хірургію органів черевної порожнини, травматологію, нейрохірургію, урологію та інші галузі."
                               "\n\n5) Фармакологія з основами фармацевтичної технології М. М. Поліщук, І. П. Засенко. Ця книга охоплює основи фармакології та фармацевтичної технології. Вона допоможе вам у розумінні механізмів дії лікарських засобів, їх клінічних властивостей та використання у практиці.")


@dp.message_handler(commands=['lecture'])
async def lecture(message: types.Message):
    link_1 = '<a href="https://www.youtube.com/watch?v=jcDVlKNrE7g&ab_channel=%D0%91%D1%96%D0%BE%D0%BB%D0%BE%D0%B3%D1%96%D1%8FUA">Лекція 1</a>'
    link_2 = '<a href="https://www.youtube.com/watch?v=o2gdr7OPNFw&list=PLaldVqYPrCD2uNy4hsLLzgj_2TjfzORhr&ab_channel=%D0%9F%D0%B5%D0%B4%D1%96%D0%B0%D1%82%D1%80%D0%B8%D1%87%D0%BD%D0%B8%D0%B9%D1%84%D0%B0%D0%BA%D1%83%D0%BB%D1%8C%D1%82%D0%B5%D1%82%D0%9D%D0%9C%D0%A3%D1%96%D0%BC.%D0%9E.%D0%9E.%D0%91%D0%BE%D0%B3%D0%BE%D0%BC%D0%BE%D0%BB%D1%8C%D1%86%D1%8F">Лекція 2</a>'
    link_3 = '<a href="https://www.youtube.com/watch?v=LtWd9dZMBl8&ab_channel=%D0%9F%D0%B5%D0%B4%D1%96%D0%B0%D1%82%D1%80%D0%B8%D1%87%D0%BD%D0%B8%D0%B9%D1%84%D0%B0%D0%BA%D1%83%D0%BB%D1%8C%D1%82%D0%B5%D1%82%D0%9D%D0%9C%D0%A3%D1%96%D0%BC.%D0%9E.%D0%9E.%D0%91%D0%BE%D0%B3%D0%BE%D0%BC%D0%BE%D0%BB%D1%8C%D1%86%D1%8Ff">Лекція 3</a>'
    link_4= '<a href="https://www.youtube.com/watch?v=I4fFxX8BaMc&ab_channel=SapiensMED">Лекція 4</a>'
    link_5 = '<a href="https://www.youtube.com/watch?v=dXvrhJPKo9M&ab_channel=%D0%91%D1%96%D0%BE%D0%BB%D0%BE%D0%B3%D1%96%D1%8FUA">Лекція 5</a>'

    await message.answer("Корисні лекції для підготовки:"
                         f'\n1) {link_1}'
                         f'\n2) {link_2}'
                         f'\n3) {link_3}'
                         f'\n4) {link_4}'
                         f'\n5) {link_5}', disable_web_page_preview=True, parse_mode=types.ParseMode.HTML)


@dp.message_handler(commands=['info'])
async def info(message: types.Message):
    await message.answer("· /start - Початкова команда для виконання тестів"
                         "\n· /reference_list - Корисна література"
                         "\n· /lecture - Корисні лекції")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
