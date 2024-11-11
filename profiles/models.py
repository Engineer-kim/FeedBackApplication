from django.db import models

# Create your models here.

class UserProfile(models.Model):
    image = models.ImageField(upload_to='images')
#ImageField 는 이미지 전용 필드 , JPEG, PNG , GIF 등의 형식만 허용
#FileField는 일반적인 파일 업로드를 위한 필드, 예를 들어, 문서, 텍스트 파일, 이미지 파일 등 다양한 파일을 저장