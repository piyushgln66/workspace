from django.shortcuts import render
from connections.models import UserProfile, DemoContent, Document
from connections.forms import DocumentForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, HttpResponse



webAppTitle="MySite"

def index(request):
    context_dict = {'webAppTitle': webAppTitle, 'title':webAppTitle}
    return render(request, 'connections/index.html', context_dict)

@login_required
def profile(request):
    form = DocumentForm()
    
    try:
        picture = Document.objects.get(user_id=request.user.id)
        photo = "/media/" + picture.docfile.name
    except Document.DoesNotExist:
        photo = '/media/blank_male.jpg'
    
    context_dict = {'form': form, 'photo':photo}   
    
    return render(request, 'connections/profile.html', context_dict)
        
    


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
        Sex = request.POST['sex']
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
            user = User.objects.create_user(first_name=FirstName,last_name=LastName,email=Email,username=Username,password=Password)
            user_profile = UserProfile(user=user, sex=Sex)
            user_profile.save()
            return render(request,
            'connections/success.html')
        else:
            return render(request,
            'connections/index.html')


def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('login_username')
        password = request.POST.get('login_password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/connections/profile/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")



# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/connections/')



@login_required
def fetch_content(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        try:
            demo_content = DemoContent.objects.get(id=id)
            return HttpResponse(demo_content.content)
        except DemoContent.DoesNotExist:
            return HttpResponse("No content with given id found !")
        




@login_required
def upload(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # first delete the previous object
                Document.objects.get(user= User.objects.get(id=request.user.id)).delete()
            except Document.DoesNotExist:
                print('already deleted')

            # now create the new object
            newdoc = Document(docfile = request.FILES['docfile'])

            newdoc.user = User.objects.get(id=request.user.id)
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect('/connections/profile/')










