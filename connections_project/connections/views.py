from django.shortcuts import render



webAppTitle="MySite"

def index(request):
    context_dict = {'webAppTitle': webAppTitle, 'title':webAppTitle}
    return render(request, 'connections/index.html', context_dict)


