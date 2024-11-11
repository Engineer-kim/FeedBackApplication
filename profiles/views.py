from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from django.views import View
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# Create your views here.

# def store_file(file):
#     with open("temp/image.jpg", "wb+") as destination:
#         # "wb+" : 파일을 쓰기 모드(w)로 열고, 파일이 존재하지 않으면 생성(b)하며, 파일 포인터를 파일의 처음으로 이동(+).
#         # 즉, 기존 파일이 있으면 덮어쓰고, 없으면 새로 생성.
#         for chunk in file.chunks():
#             destination.write(chunk)



# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html"),{
#             "form":form
#         }
#
#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
#
#         if submitted_form.is_valid():
#             #store_file(request.FILES["images"])
#             profile = UserProfile(image=request.FILES['user_image'])
#             profile.save()
#             return HttpResponseRedirect("/profiles")
#
#         return render(request, "profiles/create_profile.html"),{
#             "form":submitted_form
#         }

class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"



class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"