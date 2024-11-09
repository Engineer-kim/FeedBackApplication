from urllib import request

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from django.views import View


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


def thank_you(request):
    return render(request, "reviews/thank_you.html")
