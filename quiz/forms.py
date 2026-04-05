from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'option1', 'option2', 'option3', 'option4', 'correct_option', 'explanation']
        labels = {
            'question_text': 'Текст вопроса',
            'option1': 'Вариант 1',
            'option2': 'Вариант 2',
            'option3': 'Вариант 3',
            'option4': 'Вариант 4',
            'correct_option': 'Номер правильного варианта (1-4)',
            'explanation': 'Пояснение',
        }
        widgets = {
            'explanation': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_correct_option(self):
        data = self.cleaned_data['correct_option']
        if data not in [1, 2, 3, 4]:
            raise forms.ValidationError('Правильный вариант должен быть числом от 1 до 4.')
        return data

class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=100, required=False)