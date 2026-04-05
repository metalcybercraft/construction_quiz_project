from django.db import models


class Question(models.Model):
    """
    Модель вопроса с вариантами ответов и пояснением.
    Атрибуты:
        question_text (str): Текст вопроса.
        option1 (str): Первый вариант ответа.
        option2 (str): Второй вариант ответа.
        option3 (str): Третий вариант ответа.
        option4 (str): Четвёртый вариант ответа.
        correct_option (int): Номер правильного варианта (1-4).
        explanation (str): Пояснение к правильному ответу.
    """

    question_text = models.CharField(max_length=500, verbose_name="Текст вопроса")
    option1 = models.CharField(max_length=200, verbose_name="Вариант 1")
    option2 = models.CharField(max_length=200, verbose_name="Вариант 2")
    option3 = models.CharField(max_length=200, verbose_name="Вариант 3")
    option4 = models.CharField(max_length=200, verbose_name="Вариант 4")
    correct_option = models.PositiveSmallIntegerField(verbose_name="Правильный вариант (1-4)")
    explanation = models.TextField(verbose_name="Пояснение")

    def __str__(self):
        """Возвращает строковое представление вопроса."""
        return self.question_text

    class Meta:
        """Метаданные модели Question."""

        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
