from lib2to3.fixes.fix_input import context
from urllib import request

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review
from django.views.generic import ListView



# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form": form
        })


    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

# def review(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#
#         if form.is_valid():  # 벨리데이션 (자체 내장 함수)
#             # review = Review(user=request.user, content=form.cleaned_data['user_name'] ,
#             #                 review_text=form.cleaned_data['review_text'],
#             #                 rating=form.cleaned_data['rating']) # 일반 폼이 아닌 모델 폼이 있으므로 굳이 객체 생성 안해됨
#             form.save()
#             #print(form.cleaned_data)  # 벨리데이션 끝나고 정제된 데이터
#             return HttpResponseRedirect("/thank-you")
#
#     else:
#         form = ReviewForm()
#
#     return render(request, "reviews/review.html", {
#         "form": form
#     })

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works!"
        return context


# def thank_you(request):
#     return render(request, "reviews/thank_you.html")

class ReviewListView(ListView):
    template_name = "reviews/review_list.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context["reviews"] = reviews
    #     return context

    model = Review
    context_object_name = "reviews" # 클라이언트에서 사용할 객체명을 명시, 명시해야 클라이언트에서 사용가능 그게 아니라면 디폴트값인 object_list 를 사용해야함

    # def get_queryset(self):
    #     base_query = super().get_queryset()



class SingleReviewView(TemplateView):
    template_name = "reviews/single_review.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs.get("id")
        selected_review = Review.objects.get(pk=review_id)
        context["review"] = selected_review
        return context