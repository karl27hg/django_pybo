from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Question

def index(request):
    """pybo 목록 출력"""
    # 입력 인자
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    # 조회
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(author__username__icontains=kw) |
            Q(answer__author__username__icontains=kw)
        ).distinct()
    # 페이징 처리
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw }
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """pybo 출력 내용"""
    question = get_object_or_404(Question, pk=question_id)
    # question = Question.objects.get(id=question_id)
    context = { 'question': question }
    return render(request, 'pybo/question_detail.html', context)