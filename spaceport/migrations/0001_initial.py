# Generated by Django 3.2.9 on 2021-11-12 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PipelineList',
            fields=[
                ('pipeline_id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_by', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('complete', 'Complete'), ('in_progress', 'In Progress')], max_length=20)),
                ('pipeline_name', models.CharField(max_length=30)),
                ('pipeline_des', models.TextField()),
                ('aoi', models.JSONField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
    ]
