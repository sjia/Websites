from rest_framework import serializers
from .models import Case


class TestcaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Case  # 指定的模型类
        fields = ('pk', 'case_id',
                  'description', 'purpose',
                  'requirement',
                  'duration', 'use_counter', 'error_rate',
                  'serious_error_counter')
