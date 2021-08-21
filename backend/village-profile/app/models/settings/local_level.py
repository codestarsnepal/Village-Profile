from django.contrib.auth.models import User
from django.db import models
from app.models.settings.province import Province
from app.models.settings.district import District


class LocalLevel(models.Model):
    name = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=20, null=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)

    status = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

