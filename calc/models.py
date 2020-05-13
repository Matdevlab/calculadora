from django.db import models


class Calc(models.Model):
    CALCULO_MAT = (
        ("+", "Soma"),
        ("-", "Subtração"),
        ("*", "Multiplicação"),
        ("/", "Divisão")
    )

    val1 = models.FloatField(null=False, blank=False)
    val2 = models.FloatField(null=False, blank=False)
    oper = models.CharField(max_length=1, choices=CALCULO_MAT, blank=False, null=False)

