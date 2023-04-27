from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone

# Create your views here.

def index(request):
    """pybo 목록 출력
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    # return HttpResponse("안녕하세요. pybo에 오신 것을 환영합니다.")
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """pybo 출력 내용
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    question = get_object_or_404(Question, pk=question_id)
    # question = Question.objects.get(id=question_id)
    context = { 'question': question }
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    """pybo 답변 등록
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)