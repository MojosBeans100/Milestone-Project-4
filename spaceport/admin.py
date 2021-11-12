from django.contrib import admin
from .models import PipelineList

# Register your models here.
@admin.register(PipelineList)
class PipelineListAdmin(admin.ModelAdmin):
    list_display = (
                'pipeline_id',
                'pipeline_name',
                'pipeline_des',
                'created_by',
                'date_created',
                'status',                
                )