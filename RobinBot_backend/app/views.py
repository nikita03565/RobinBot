from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html', {})

@csrf_exempt
def data_channel(request):
    return render(request, 'dataChannel.html', {})
