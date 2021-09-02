from django.shortcuts import render

def index(request):
    add_text = {'insert_h2':'this_is_inserted', 'insert_p':22}
    return render(request, 'PracticeApp/index.html', context=add_text)

def kenobi(request):
    return render(request, 'PracticeApp/kenobi.html')
    
def general(request):
    return render(request, 'PracticeApp/general.html')
