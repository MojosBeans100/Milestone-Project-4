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