from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    # DjangoのデフォルトのUserモデルにはユーザー名(username)、メールアドレス(email)、
    # パスワード(password)などの基本フィールドが含まれています。

    # is_superuser: システム管理者かどうかを示すフラグ
    # is_staff: 管理サイトへのアクセス権を持つ従業員かどうかを示すフラグ
    # DjangoのAbstractUserモデルにこれらのフィールドが既に含まれています。

    # 追加の情報が必要な場合は、ここに新しいフィールドを追加します。
    # 例: department = models.CharField(max_length=100, null=True, blank=True)

    # カスタムメソッドやプロパティを必要に応じて追加することができます。
    # 例:
    # def is_admin(self):
    #     return self.is_superuser

    # クラスメタデータを必要に応じて設定することができます。
    # class Meta:
    #     verbose_name = "User"
    #     verbose_name_plural = "Users"

    def __str__(self):
        return self.name
