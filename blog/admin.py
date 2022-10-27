from django.contrib import admin
# 새로 생성한 모델 import
from .models import Post

# 관리자 페이지에서 만든 모델을 보려면 다음 코드 필요
admin.site.register(Post)