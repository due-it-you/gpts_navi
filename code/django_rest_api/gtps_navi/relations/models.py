from django.db import models
from django.conf import settings

class Relation(models.Model):
    follower = models.ForeignKey(settings.ACCOUNTS_MODEL, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(settings.ACCOUNTS_MODEL, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('follower', 'followed')

    def __str__(self):
        return f"{self.follower.username} follows {self.followed.username}"
