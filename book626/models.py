from django.db import models


class BasicInfo(models.Model):

    SEX = [('M', 'Man'),
           ('F', 'Woman'),
           ]

    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=20, choices=SEX)
    age = models.IntegerField(default=0)
