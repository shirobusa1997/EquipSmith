from django.db import models

# Create your models here.
class SignUpToken(models.Model):
    id = models.CharField('トークンID', max_length = 100, primary_key = True)
    token = models.CharField('トークン', blank = False, max_length = 32)
    available = models.BooleanField('アクティベート状況', blank = False, default = False)
    target = models.CharField('対象ユーザ', default='hogehoge', max_length = 64)