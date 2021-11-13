from django.forms import ModelForm, DateInput, TextInput, Textarea
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
                'placeholder': 'eg. My First Pipeline',
                'id': 'pipeline_name',
            }),
            'pipeline_des': Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Give your pipeline a description',
                'id': 'pipeline_des'
            }),
            'start_date': DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'id': 'start_date',
            }),
            'end_date': DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'id': 'end_date',
            }),
        }
