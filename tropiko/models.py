from django.db import models


class TropikoModel(models.Model):
    NAME = models.CharField('Name', max_length=255)
    P_NUM = models.IntegerField('Phone')
    EMAIL = models.EmailField('Email')
    MESSAGE = models.TextField('Message')

    def __str__(self):
        return self.NAME