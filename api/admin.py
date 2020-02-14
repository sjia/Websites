from django.contrib import admin

# Register your models here.
from .models import Case

@admin.register(Case)
class CaseByAdmin(admin.ModelAdmin):
    list_display = ('case_id',
                    'description',
                    'purpose',
                    'requirement',
                    'storage_device',
                    'exclusive',
                    'duration',
                    'usr_counter',
                    'error_rate',
                    'serious_error_counter',
                    'last_run_state',
                    'code_coverage',
                    )