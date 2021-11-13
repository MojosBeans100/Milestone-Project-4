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
    interval        = models.CharField(choices=interval, max_length=12)


