from django.shortcuts import render
from connections.models import User
from django.contrib import messages



webAppTitle="MySite"

def index(request):
    context_dict = {'webAppTitle': webAppTitle, 'title':webAppTitle}
    return render(request, 'connections/index.html', context_dict)


def profile(request):
    context_dict = {'webAppTitle': webAppTitle, 'title':webAppTitle}
    return render(request, 'connections/profile.html')


def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    error = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # fetch all values
        FirstName = request.POST['firstname']
        LastName = request.POST['lastname']
        Email = request.POST['email']
        Username = request.POST['username']
        Password = request.POST['password']
        #validate
        if not FirstName:
            messages.add_message(request, messages.INFO, 'Please enter the firstname');
            error=True
        if not LastName:
            messages.add_message(request, messages.INFO, 'Please enter the lastname');
            error=True

        if not Email:
            messages.add_message(request, messages.INFO, 'Please enter the email');
            error=True

        if not Username:
            messages.add_message(request, messages.INFO, 'Please enter a unique username');
            error=True

        if not Password:
            messages.add_message(request, messages.INFO, 'Please enter the password');
            error=True

        if not error:
            user = User(firstname=FirstName,lastname=LastName,email=Email,username=Username,password=Password)
            user.save()
            return render(request,
            'connections/success.html')
        else:
            return render(request,
            'connections/index.html')


