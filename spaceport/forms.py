from django.forms import ModelForm, DateInput, TextInput
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

        widgets = {
            'pipeline_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'eg. My First Pipeline'
            })
        }
