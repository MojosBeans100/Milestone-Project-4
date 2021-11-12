from django.shortcuts import render
from .models import PipelineList

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def models_temp(request):

    context = {
        'active_list' : PipelineList.objects.filter(status="active"),
        'complete_list' : PipelineList.objects.filter(status="complete")
    }

    print(context)
    return render(request, 'models_temp.html', context)

def list_pipelines(request):

    user = str(request.user).capitalize()

    active_list = PipelineList.objects.filter(created_by=user).filter(status="active")
    complete_list = PipelineList.objects.filter(created_by=user).filter(status="complete")
    in_progress_list = PipelineList.objects.filter(created_by=user).filter(status="in_progress")

    context = {
        'active_list': active_list,
        'complete_list': complete_list,
        'in_progress_list': in_progress_list,
    }

    return render(request,'user_home.html', context)
