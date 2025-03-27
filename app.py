import os

from aiogram import Router, Bot, F
from aiogram.types import Message,  InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
from dotenv import load_dotenv

from text import *


load_dotenv()  # Загрузка токена из переменных окружения

bot = Bot(token=os.getenv('TOKEN'))
router = Router()


# Обработчики команд

# Начать
@router.message(Command('start'))
async def cmd_start(msg: Message):
    await bot.send_message(msg.chat.id, START_TEXT, parse_mode='HTML')


# Начать -> Об организации
@router.message(Command('about'))
async def cmd_about(msg: Message):

    # Inline-кнопка для возвращения к обработчику /start
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="go_back")]
        ]
    )

    await bot.send_message(msg.chat.id, ABOUT_TEXT, parse_mode='HTML', reply_markup=keyboard)

# Начать -> Услуги
@router.message(Command('services'))
async def cmd_services(msg: Message):
    text = """<b>Категории услуг:</b>"""

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Работодателям", callback_data="services_employers")],
            [InlineKeyboardButton(text="Гражданам", callback_data="services_citizens")],
            [InlineKeyboardButton(text="Часто задаваемые вопросы", callback_data='services_faq')],
            [InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="go_back")]
        ]
    )

    await bot.send_message(msg.chat.id, text, parse_mode="HTML", reply_markup=keyboard)


# Начать -> Услуги -> Рабодотаделям
@router.callback_query(F.data == "services_employers")
async def services_employers(callback: CallbackQuery):
    text = "<b>Услуги для работодателей:</b>"

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Подбор персонала", callback_data="employers_recruitment")],
            [InlineKeyboardButton(text="Проф. обучение", callback_data="employers_professional_education")],
            [InlineKeyboardButton(text="Семинары", callback_data="employers_seminars")],
            [InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="go_back_to_services")]
        ]
    )

    await callback.message.edit_text(text, parse_mode="HTML", reply_markup=keyboard)
    await callback.answer()


# Начать -> Услуги -> Рабодотаделям -> Подбор персонала
@router.callback_query(F.data == "employers_recruitment")
async def employers_recruitment(callback: CallbackQuery):
    text = """
    📄<b>Документ с информацией доступен по ссылке ниже:</b>
    <a href="https://docs.yandex.ru/docs/view?url=ya-disk-public%3A%2F%2FYdltfNbH8CZOeeBFWU%2B5Jq0xZx9YjEaMwWWI4IWZ0oO%2BcplcQHsDQgwmv2o5IjQiq%2FJ6bpmRyOJonT3VoXnDag%3D%3D&name=Инструкция_по_размещению_вакансий_и_количества_рабочих_мест%20(5).pdf">
    Инструкция по размещению вакансий и количества рабочих мест</a>
    """

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="go_back_to_services_employers")]
        ]
    )

    await callback.message.edit_text(text, parse_mode="HTML", reply_markup=keyboard)
    await callback.answer()


# Начать -> Услуги -> Рабодотаделям -> Проф. обучение
@router.callback_query(F.data == "employers_professional_education")
async def employers_professional_education(callback: CallbackQuery):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="go_back_to_services_employers")]
        ]
    )

    await callback.message.edit_text(EMPLOYERS_PROFESSIONAL_EDUCATION_TEXT, parse_mode="HTML", reply_markup=keyboard)
    await callback.answer()


# Начать -> Услуги -> Рабодотаделям -> Семинары
@router.callback_query(F.data == "employers_seminars")
async def employers_seminars(callback: CallbackQuery):
    text = """
    <b>🗓️ Расписание актуальных онлайн и оффлайн семинаров</b>:
    Пока информации о семинарах нет. Ожидайте обновлений!
    """

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="go_back_to_services_employers")]
        ]
    )

    await callback.message.edit_text(text, parse_mode="HTML", reply_markup=keyboard)
    await callback.answer()


# Начать -> Услуги -> Гражданам
@router.callback_query(F.data == "services_citizens")
async def services_citizens(callback: CallbackQuery):
    text = "<b>Услуги для граждан:</b>"

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Профориентационные тесты", callback_data="guidance_tests")],
            [InlineKeyboardButton(text="Проф. обучение", callback_data="citizens_professional_education")],
            [InlineKeyboardButton(text="Мероприятия", callback_data="events")],
            [InlineKeyboardButton(text="Подача заявления", callback_data="application")],
            [InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="go_back_to_services")]
        ]
    )

    await callback.message.edit_text(text, parse_mode="HTML", reply_markup=keyboard)
    await callback.answer()


# Начать -> Услуги -> Гражданам -> Профориентационные тесты
@router.callback_query(F.data == "guidance_tests")
async def guidance_tests(callback: CallbackQuery):
    text = """
    <b>Профориентационные тесты доступны по ссылке ниже:</b>:\n
    <a href="https://trudvsem.ru/proforientation/testing">Профориентационное тестирование</a>
    """

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="go_back_to_services_citizens")]
        ]
    )

    await callback.message.edit_text(text, parse_mode="HTML", reply_markup=keyboard)
    await callback.answer()


# Начать -> Услуги -> Гражданам -> Проф. обучение
@router.callback_query(F.data == "citizens_professional_education")
async def citizens_professional_education(callback: CallbackQuery):
    text = """
    <b>Информация о проф.обучении</b>
    """

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="go_back_to_services_citizens")]
        ]
    )

    await callback.message.edit_text(text, parse_mode="HTML", reply_markup=keyboard)
    await callback.answer()


# Начать -> Услуги -> Гражданам -> Мероприятия
@router.callback_query(F.data == "events")
async def events(callback: CallbackQuery):
    text = """
    <b>Информация о предстоящих мероприятиях</b>
    """

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="go_back_to_services_citizens")]
        ]
    )

    await callback.message.edit_text(text, parse_mode="HTML", reply_markup=keyboard)
    await callback.answer()


# Начать -> Услуги -> Гражданам -> Подача заявления
@router.callback_query(F.data == "application")
async def application(callback: CallbackQuery):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="go_back_to_services_citizens")]
        ]
    )

    await callback.message.edit_text(APPLICATION_TEXT, parse_mode="HTML", reply_markup=keyboard)
    await callback.answer()


# Начать -> Услуги -> ЧАВО
@router.callback_query(F.data == "services_faq")
async def services_faq(callback: CallbackQuery):
    text = "<b>Часто задаваемые вопросы:</b>"

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Кто не может быть признан безработным?",
                                  callback_data="is_not_unemployed")],
            [InlineKeyboardButton(text="Размер пособия по безработице и её продолжительность получения",
                                  callback_data="compensation_info")],
            [InlineKeyboardButton(text="Повторная регистрация в качестве безработного",
                                  callback_data="re_registration_as_unemployed")],
            [InlineKeyboardButton(text="Перерегистрация безработных граждан",
                                  callback_data="re_regestration_unemployed_citizens")],
            [InlineKeyboardButton(text="Как сняться с учёта в качестве безработного?",
                                  callback_data="how_to_deregister")],
            [InlineKeyboardButton(text="Как получить справку из ЦЗН?",
                                  callback_data="how_to_get_certificate")],
            [InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="go_back_to_services")]
        ]
    )

    await callback.message.edit_text(text, parse_mode="HTML", reply_markup=keyboard)
    await callback.answer()


# Начать -> Услуги -> ЧАВО -> Кто не может быть признан безработным?
@router.callback_query(F.data == "is_not_unemployed")
async def is_not_unemployed(callback: CallbackQuery):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="go_back_to_faq")]
        ]
    )
    await callback.message.edit_text(IS_NOT_UNEMPLOYED_TEXT, parse_mode="HTML", reply_markup=keyboard)
    await callback.answer()


# Начать -> Услуги -> ЧАВО -> Размер пособия по безработице и её продолжительность получения
@router.callback_query(F.data == "compensation_info")
async def compensation_info(callback: CallbackQuery):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="go_back_to_faq")]
        ]
    )
    await callback.message.edit_text(COMPENSATION_INFO_TEXT, parse_mode="HTML", reply_markup=keyboard)
    await callback.answer()


# Начать -> Услуги -> ЧАВО -> Повторная регистрация в качестве безработного
@router.callback_query(F.data == "re_registration_as_unemployed")
async def re_registration_as_unemployed(callback: CallbackQuery):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="go_back_to_faq")]
        ]
    )
    await callback.message.edit_text(RE_REGISTRATION_AS_UNEMPLOYED_TEXT, parse_mode="HTML", reply_markup=keyboard)
    await callback.answer()


# Начать -> Услуги -> ЧАВО -> Перерегистрация безработных граждан
@router.callback_query(F.data == "re_regestration_unemployed_citizens")
async def re_regestration_unemployed_citizens(callback: CallbackQuery):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="go_back_to_faq")]
        ]
    )
    await callback.message.edit_text(RE_REGISTRATION_UNEMPLOYED_CITIZENS_TEXT, parse_mode="HTML", reply_markup=keyboard)
    await callback.answer()


# Начать -> Услуги -> ЧАВО -> Как сняться с учёта в качестве безработного?
@router.callback_query(F.data == "how_to_deregister")
async def how_to_deregister(callback: CallbackQuery):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="go_back_to_faq")]
        ]
    )
    await callback.message.edit_text(HOW_TO_DERIGISTER_TEXT, parse_mode="HTML", reply_markup=keyboard)
    await callback.answer()


# Начать -> Услуги -> ЧАВО -> Как получить справку из ЦЗН?
@router.callback_query(F.data == "how_to_get_certificate")
async def how_to_get_certificate(callback: CallbackQuery):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="go_back_to_faq")]
        ]
    )
    await callback.message.edit_text(HOW_TO_GET_CERTIFICATE_TEXT, parse_mode="HTML", reply_markup=keyboard)
    await callback.answer()


# Обработчики кнопки "Вернуться назад"

# к Началу
@router.callback_query(lambda c: c.data == "go_back")
async def go_back(callback):
    await cmd_start(callback.message)
    await callback.answer()

# к Услугам
@router.callback_query(F.data == "go_back_to_services")
async def go_back_to_services(callback: CallbackQuery):
    await cmd_services(callback.message)
    await callback.answer()

# к Работодателям
@router.callback_query(F.data == "go_back_to_services_employers")
async def go_back_to_services_employers(callback: CallbackQuery):
    await services_employers(callback)
    await callback.answer()

# к Гражданам
@router.callback_query(F.data == "go_back_to_services_citizens")
async def go_back_to_services_citizens(callback: CallbackQuery):
    await services_citizens(callback)
    await callback.answer()

# к ЧАВО
@router.callback_query(F.data == "go_back_to_faq")
async def go_back_to_faq(callback: CallbackQuery):
    await services_faq(callback)
    await callback.answer()