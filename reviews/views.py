from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from django.views.generic.base import TemplateView
from .models import Review
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView ,CreateView

# Create your views here.

# class ReviewView(FormView): #FormView를 사용하면 처음 페이지를 불러올때의 겟 , 인풋값들을  다 채우고 포스트할때 전부 다 알아서 처리됨
#     # 그래서 form_valid() 메서드에서 실제 데이터 처리 로직만 구현
#     form_class = ReviewForm
#     template_name = 'reviews/review.html'
#     success_url = '/thank-you'
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm    # fields = '__all__' 와 동일함
    template_name = 'reviews/review.html'
    success_url = '/thank-you'


    # def get(self, request):
    #     form = ReviewForm()
    #
    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })


    # def post(self, request):
    #     form = ReviewForm(request.POST)
    #
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")

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



class SingleReviewView(DetailView): #DetailView 사용하면 별도의 함수 작성안해도 됨(편함)
    template_name = "reviews/single_review.html"
    model = Review

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs.get("id")
    #     selected_review = Review.objects.get(pk=review_id)
    #     context["review"] = selected_review
    #     return context
