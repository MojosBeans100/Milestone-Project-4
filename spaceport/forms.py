from django.forms import ModelForm, DateInput
from .models import PipelineList

class CreatePipeline(ModelForm):
    class Meta:
        model = PipelineList
        fields = [
            'pipeline_name',
            'pipeline_des',
            'aoi',
            'start_date',
            'end_date'
            ]
