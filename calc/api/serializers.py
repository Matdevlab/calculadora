from rest_framework import serializers
from calc.models import Calc


class CalcSerializer(serializers.ModelSerializer):
    calc = serializers.SerializerMethodField()

    class Meta:
        model = Calc
        fields = ('val1', 'val2', 'oper', 'calc')

    def get_calc(self, obj):
        if obj.oper == '+':
            return obj.val1 + obj.val2
        elif obj.oper == '-':
            return obj.val1 - obj.val2
        elif obj.oper == '*':
            return obj.val1 * obj.val2
        elif obj.oper == '/':
            return obj.val1 / obj.val2
