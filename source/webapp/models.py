from django.db import models


class Counts(models.Model):
    string_a = models.IntegerField(null=False, blank=False, verbose_name="Число А")
    string_b = models.IntegerField(null=False, blank=False, verbose_name="Число Б")
    answer = models.IntegerField(default=0, null=True, blank=True)