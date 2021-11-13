from django.db import models

# Create your models here.
class PipelineList(models.Model):

    # status choices
    status_choices = (
        ('active', 'Active'),
        ('complete', 'Complete'),
        ('in_progress', 'In Progress'),
    )

    # interval choice for results from pipeline
    interval = (
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('biweekly', 'Biweekly'),
        ('monthly', 'Monthly'),
        ('bimonthly', 'Bimonthly'),
    )

    # output image choice
    output_image = (
        ('true-colour', 'True Colour Image'),
        ('false-colour-urban', 'False Colour Urban'),
        ('false-colour-infrared', 'False Colour Infrared'),
        ('near-infrared', 'Near Infrared'),
    )

    # auto generated
    pipeline_id     = models.IntegerField(primary_key=True)
    created_by      = models.CharField(max_length=50)
    date_created    = models.DateTimeField(auto_now=True)
    status          = models.CharField(choices=status_choices, max_length=20)

    # user form
    pipeline_name   = models.CharField(max_length=30)
    pipeline_des    = models.TextField()
    aoi             = models.JSONField()
    start_date      = models.DateTimeField()
    end_date        = models.DateTimeField()
    interval        = models.CharField(choices=interval, max_length=12, null=True)
    output_image    = models.CharField(choices=output_image, max_length=50, null=True)


