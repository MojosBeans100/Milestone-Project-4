from django.forms import ModelForm, DateInput, TextInput, Textarea, Select
from .models import PipelineList

class CreatePipeline(ModelForm):

    interval = (
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('biweekly', 'Biweekly'),
        ('monthly', 'Monthly'),
        ('bimonthly', 'Bimonthly'),
    )

    output_image = (
        ('true-colour', 'True Colour Image'),
        ('false-colour-urban', 'False Colour Urban'),
        ('false-colour-infrared', 'False Colour Infrared'),
        ('near-infrared', 'Near Infrared'),
    )

    class Meta:
        model = PipelineList
        fields = [
            'pipeline_name',
            'pipeline_des',
            'aoi',
            'start_date',
            'end_date',
            'interval',
            'output_image',
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
            'interval': Select(choices='interval',attrs={
                'class': 'form-select',
            }),
            'output_image': Select(choices='output_image',attrs={
                'class': 'form-select',
            })
        }
