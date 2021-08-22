from django.shortcuts import render
from app_forms.forms import Users

def index(request):
    return render(request, 'app_forms/index.html', context={'insert_h2':'This is inserted!'})

def formpage(request):
    form = Users()
    print(request.method)
    if request.method == 'POST': 
        form = Users(request.POST)

        if form.is_valid():
            print(f"NAME:\t{form.cleaned_data['name']}\nEMAIL:\t{form.cleaned_data['email']}\nTEXT:\t{form.cleaned_data['text']}")

    return render(request, 'app_forms/formpage.html', context={'insert_form':form})