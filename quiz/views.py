"""Представления (контроллеры) для приложения quiz."""

from django.shortcuts import render, get_object_or_404, redirect
import random
from .models import Question
from .forms import QuestionForm, SearchForm


def question_list(request):
    """Отображает список всех вопросов  возможностью поиска.
    GET параметр 'query' фильтрует вопросы по вхождению подстроки."""
    form = SearchForm(request.GET)
    query = request.GET.get("query", "")
    if query:
        questions = Question.objects.filter(question_text__icontains=query)
    else:
        questions = Question.objects.all()
    return render(
        request,
        "quiz/question_list.html",
        {
            "questions": questions,
            "form": form,
            "query": query,
        },
    )


def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, "quiz/question_detail.html", {"question": question})


def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("quiz:question_list")
    else:
        form = QuestionForm()
    return render(request, "quiz/question_form.html", {"form": form, "title": "Добавить вопрос"})


def question_edit(request, pk):
    """Начало теста: выбирает 5 случайных вопросо
    и сохраняет их ID в сессии."""
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect("quiz:question_detail", pk=question.pk)
    else:
        form = QuestionForm(instance=question)
    return render(
        request, "quiz/question_form.html", {"form": form, "title": "Редактировать вопрос"}
    )


def quiz_start(request):
    """Начало теста: выбирает 5 случайных
    вопросов и сохраняет их ID в сессии."""
    all_questions = list(Question.objects.all())
    if len(all_questions) >= 5:
        questions = random.sample(all_questions, 5)
    else:
        questions = all_questions
    request.session["quiz_questions_ids"] = [q.id for q in questions]
    return render(request, "quiz/quiz.html", {"questions": questions})


def quiz_result(request):
    """Обрабатывает ответы пользователя, подсчитывает результат.POST:
    получает ответы из request.POST, сравнивает
    правильными, вычисляет процент
    правильных ответов и отображает результат."""
    if request.method != "POST":
        return redirect("quiz:quiz_start")
    question_ids = request.session.get("quiz_questions_ids", [])
    if not question_ids:
        return redirect("quiz:quiz_start")
    questions = Question.objects.filter(id__in=question_ids)
    user_answers = {}
    for q in questions:
        answer_key = f"question_{q.id}"
        answer = request.POST.get(answer_key)
        if answer and answer.isdigit():
            user_answers[q.id] = int(answer)
    results = []
    correct_count = 0
    for q in questions:
        is_correct = user_answers.get(q.id) == q.correct_option
        if is_correct:
            correct_count += 1
        results.append(
            {
                "question": q,
                "user_answer": user_answers.get(q.id),
                "is_correct": is_correct,
                "explanation": q.explanation,
            }
        )
    score_percent = int(correct_count / len(questions) * 100) if questions else 0
    del request.session["quiz_questions_ids"]
    return render(
        request,
        "quiz/quiz_result.html",
        {
            "results": results,
            "correct_count": correct_count,
            "total": len(questions),
            "score_percent": score_percent,
        },
    )


def about(request):
    """Страница «О проекте»"""
    count = Question.objects.count()
    return render(request, "quiz/about.html", {"count": count})
