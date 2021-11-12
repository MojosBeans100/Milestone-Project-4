from django.shortcuts import render
from .models import PipelineList

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def models_temp(request):
    context = {
        'list' : PipelineList.objects.all()
    }

    print(context)
    return render(request, 'models_temp.html', context)