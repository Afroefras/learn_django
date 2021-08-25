from django.shortcuts import render
from app_model_forms.forms import NewUserForm

def index(request):
    return render(request, 'app_model_forms/index.html', context={'insert_h2':'This is Grogu!'})

def formpage(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else: print('FORM ERROR!')

    return render(request, 'app_model_forms/formpage.html', context={'form':form})
