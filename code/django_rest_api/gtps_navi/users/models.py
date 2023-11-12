from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # OAuthで取得したユーザー名
    username = models.CharField(max_length=150, unique=True)

    # 固有のランダムなID（例：UUID）
    unique_id = models.CharField(max_length=100, unique=True)

    # プロフィール画像（オプション）
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    # プロフィール自己紹介（オプション）
    bio = models.TextField(blank=True, null=True)

    # OAuth認証情報（TwitterのID）
    twitter_id = models.CharField(max_length=100, blank=True, null=True)

    # 追加のフィールドとメソッド（必要に応じて）
