from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Welcome!'}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'wonderland/index.html', context=context_dict)


def about(request):
    return HttpResponse("Wonderland says hey there is About page! <a href='/wonderland/'>Index</a>")