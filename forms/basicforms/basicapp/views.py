from django.shortcuts import render
from basicapp import forms

# Create your views here.

def index(request):
    return render(request,'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #DO SOMETHING
            print("VALIDATION SUCCESS")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])   
            print("Message: "+form.cleaned_data['text'])   

        
    return render(request,'basicapp/form_page.html',context={'form':form})

