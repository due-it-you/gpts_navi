from django.db import models
from django.conf import settings

class User(models.Model):
    # ここでユーザーとの一対多の関連を定義
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='posts_images/')
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
