import os

from aiogram import Router, Bot, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, FSInputFile
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
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📋 Услуги", callback_data="open_services")],
            [InlineKeyboardButton(text="ℹ️ Об организации", callback_data="open_about")],
            [InlineKeyboardButton(text="📩 Обратная связь", callback_data="feedback")]
        ]
    )

    await bot.send_message(
        msg.chat.id,
        "👋 Добро пожаловать в чат-бот <b>Центра занятости Ленинградского района</b>!\n\n"
        "Что может делать этот бот?\n"
        "• Помогает найти актуальные вакансии\n"
        "• Предоставляет информацию о программах обучения\n"
        "• Консультирует по вопросам трудоустройства\n\n"
        "Выберите интересующий Вас раздел:",
        parse_mode="HTML",
        reply_markup=keyboard
    )

@router.callback_query(F.data == "open_services")
async def open_services(callback: CallbackQuery):
    await cmd_services(callback.message)
    await callback.answer()


@router.callback_query(F.data == "open_about")
async def open_about(callback: CallbackQuery):
    await cmd_about(callback.message)
    await callback.answer()

@router.callback_query(F.data == "feedback")
async def open_feedback(callback: CallbackQuery):
    await cmd_feedback(callback.message)
    await callback.answer()


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


# Начать -> Обратная связь
@router.message(Command('feedback'))
async def cmd_feedback(msg: Message):
    text = ("Если вам нужна дополнительная информация о документах или трудоустройстве, "
            "либо у вас есть идеи, как улучшить работу центра занятости и этого чат-бота, "
            "— поделитесь ими через специальную форму."
            "\n📌 Перейти к форме: <a href='https://docs.google.com/forms/d/e/1FAIpQLSfnqIvWSbgOM_IEXWvR20FVH2fPDnowY-X28apDuiYfJmaGfA/viewform?usp=dialog'>Нажмите здесь</a>"
            "\n Спасибо за обратную связь!")

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
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
    text = ("📄<b>Документ с информацией о подброне персонала доступен по ссылке:</b>"
            "<a href='https://docs.yandex.ru/docs/view?url=ya-disk-public%3A%2F%2FYdltfNbH8CZOeeBFWU%2B5Jq0xZx9YjEaMwWWI4IWZ0oO%2BcplcQHsDQgwmv2o5IjQiq%2FJ6bpmRyOJonT3VoXnDag%3D%3D&name=Инструкция_по_размещению_вакансий_и_количества_рабочих_мест%20(5).pdf'> "
            "Инструкция по размещению вакансий и количества рабочих мест</a>")

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
            [InlineKeyboardButton(text="⬅️Вернуться назад", callback_data="go_back_to_services_employers")]
        ]
    )

    await callback.message.edit_text(EMPLOYERS_PROFESSIONAL_EDUCATION_TEXT, parse_mode="HTML", reply_markup=keyboard)
    await callback.answer()


# Начать -> Услуги -> Рабодотаделям -> Семинары
@router.callback_query(F.data == "employers_seminars")
async def employers_seminars(callback: CallbackQuery):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="go_back_to_services_employers")]
        ]
    )

    await callback.message.edit_text(EMPLOYERS_SEMINARS_TEXT, parse_mode="HTML", reply_markup=keyboard)
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
    text = ("Не знаете, какую профессию выбрать?"
            " Пройдите тесты — они помогут определить ваши сильные стороны и "
            "подобрать подходящую работу: <a href='https://trudvsem.ru/proforientation/testing'>Профориентационное тестирование</a>")

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

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="go_back_to_services_citizens")]
        ]
    )

    await callback.message.edit_text(CITIZENS_PROFFESIONAL_EDUCATION_TEXT, parse_mode="HTML", reply_markup=keyboard)
    await callback.answer()


# Начать -> Услуги -> Гражданам -> Мероприятия
@router.callback_query(F.data == "events")
async def events(callback: CallbackQuery):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="go_back_to_services_citizens")]
        ]
    )

    await callback.message.edit_text(EVENTS_TEXT, parse_mode="HTML", reply_markup=keyboard)
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
            [InlineKeyboardButton(text="Минимальное пособие", callback_data="show_image_1")],
            [InlineKeyboardButton(text="Максимальное пособие", callback_data="show_image_2")],
            [InlineKeyboardButton(text="Мин. пособие (предпенсионный)",
                                  callback_data="show_image_3")],
            [InlineKeyboardButton(text="Макс. пособие (предпенсионный)",
                                  callback_data="show_image_4")],
            [InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="go_back_to_faq")]
        ]
    )

    try:
        await callback.message.delete()  # Удаляем старое сообщение (фото)
    except Exception:
        pass  # На всякий случай, если сообщение уже удалено

    await callback.message.answer("Выберете интересующий раздел", parse_mode="HTML", reply_markup=keyboard)
    await callback.answer()


# Обработчик изображений
@router.callback_query(F.data.startswith("show_image_"))
async def show_selected_image(callback: CallbackQuery):
    image_number = callback.data.split("_")[-1]  # Получаем номер изображения
    image_path = f"images/{image_number}.jpg"  # Путь к изображению

    # Отправляем фото с кнопкой "Назад"
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="compensation_info")]
        ]
    )

    try:
        photo = FSInputFile(image_path)
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption="Информация по выбранному разделу",
            reply_markup=keyboard
        )
    except FileNotFoundError:
        await callback.message.answer(
            "Изображение временно недоступно",
            reply_markup=keyboard
        )

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