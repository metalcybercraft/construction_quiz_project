"""Миграция для добавления 10 начальных вопросов по строительным терминам."""

from django.db import migrations

QUESTIONS_DATA = [
    {
        "question_text": 'Что означает термин "Абрис"?',
        "option1": "Чертёж контура сооружения",
        "option2": "Вид кирпичной кладки",
        "option3": "Инструмент геодезиста",
        "option4": "Строительный материал",
        "correct_option": 1,
        "explanation": "Абрис - чертёж внешнего контура объекта.",
    },
    {
        "question_text": 'Что такое "бутовый камень"?',
        "option1": "Искусственный бетонный блок",
        "option2": "Крупный природный камень для кладки фундаментов",
        "option3": "Отходы кирпичного производства",
        "option4": "Декоративная плитка",
        "correct_option": 2,
        "explanation": "Бутовый камень - крупные куски горных пород.",
    },
    {
        "question_text": 'Что называют "водоупором" в геологии?',
        "option1": "Слой грунта, не пропускающий воду",
        "option2": "Насос для откачки воды",
        "option3": "Гидроизоляционный материал",
        "option4": "Уровень грунтовых вод",
        "correct_option": 1,
        "explanation": "Водоупор - пласт горных пород, задерживающий воду.",
    },
    {
        "question_text": "Что изучает геодезия?",
        "option1": "Свойства бетона",
        "option2": "Измерения на местности",
        "option3": "Проектирование зданий",
        "option4": "Строительные материалы",
        "correct_option": 2,
        "explanation": "Геодезия - наука об измерениях земной поверхности.",
    },
    {
        "question_text": 'Что такое "дренчер"?',
        "option1": "Водосточная труба",
        "option2": "Система пожаротушения с открытыми оросителями",
        "option3": "Вентиляционный канал",
        "option4": "Дренажная канава",
        "correct_option": 2,
        "explanation": "Дренчер - система пожаротушения с открытыми оросителями.",
    },
    {
        "question_text": 'Что означает термин "железнение"?',
        "option1": "Покрытие бетона железом",
        "option2": "Уплотнение поверхности бетона",
        "option3": "Сварка арматуры",
        "option4": "Окраска металлоконструкций",
        "correct_option": 2,
        "explanation": "Железнение - упрочнение верхнего слоя бетона.",
    },
    {
        "question_text": 'Что такое "кессон"?',
        "option1": "Временное ограждение",
        "option2": "Конструкция для создания сухой полости под водой",
        "option3": "Тип фундамента",
        "option4": "Строительный кран",
        "correct_option": 2,
        "explanation": "Кессон - водонепроницаемая камера для подводных работ.",
    },
    {
        "question_text": 'Что такое "мауэрлат"?',
        "option1": "Верхний брус для крепления стропил",
        "option2": "Нижняя обвязка фундамента",
        "option3": "Подоконная доска",
        "option4": "Балка перекрытия",
        "correct_option": 1,
        "explanation": "Мауэрлат - брус для опирания стропил.",
    },
    {
        "question_text": 'Что такое "опалубка"?',
        "option1": "Инструмент для замешивания бетона",
        "option2": "Форма для заливки бетона",
        "option3": "Защитная плёнка",
        "option4": "Арматурная сетка",
        "correct_option": 2,
        "explanation": "Опалубка - форма для заливки бетона.",
    },
    {
        "question_text": 'Что такое "ростверк"?',
        "option1": "Балка, объединяющая сваи",
        "option2": "Вид кровли",
        "option3": "Свайный фундамент",
        "option4": "Бетонная плита",
        "correct_option": 1,
        "explanation": "Ростверк - верхняя часть свайного фундамента.",
    },
]


def add_questions(apps, schema_editor):
    """Добавляет 10 вопросов в базу данных."""
    Question = apps.get_model("quiz", "Question")
    for q in QUESTIONS_DATA:
        Question.objects.create(**q)


def remove_questions(apps, schema_editor):
    """Удаляет добавленные ранее вопросы (для отката миграции)."""

    Question = apps.get_model("quiz", "Question")
    for q in QUESTIONS_DATA:
        Question.objects.filter(question_text=q["question_text"]).delete()


class Migration(migrations.Migration):
    """Миграция данных с 10 вопросами."""

    dependencies = [
        ("quiz", "0001_initial"),
    ]
    operations = [
        migrations.RunPython(add_questions, remove_questions),
    ]
