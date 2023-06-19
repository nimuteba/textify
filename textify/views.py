from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

import replicate
import requests


# Create your views here.
def index(request):
    context = {}
    
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        
        file = FileSystemStorage()
        file_name = file.save(uploaded_file.name, uploaded_file)
        
        #replicate.Client(api_token=r8_S7oW49LSIOIeHeK4O1akqgb0Mhf5R1n1MVyun)
        client = replicate.Client(api_token='r8_S7oW49LSIOIeHeK4O1akqgb0Mhf5R1n1MVyun')
        output = client.run(
    "openai/whisper:91ee9c0c3df30478510ff8c8a3a545add1ad0259ad3a9f78fba57fbc05ee64f7",
        input={"audio": open("media/harvard.wav", "rb")})
        
        output_real = output

        
        context['url'] = file.url(file_name)
        context['output'] = output_real['transcription']
        
    return render(request, 'textify/index.html', context)
