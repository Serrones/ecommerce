"""
This view was created only to test our Django application.
Here we have a simple function based view (home_page)
"""

from django.http import HttpResponse
from django.shortcuts import render

# Function based view that calls a html document from templates folder
def home_page(request):
    context = {
    "title": "Hello Universe!! We're working",
    "content": "Welcome to the Home Page"
    }
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
    "title": "We're infinite",
    "content": "Welcome to the About Page"
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    context = {
    "title": "Just look to the skies",
    "content": "Welcome to the Contact Page"
    }
    return render(request, "home_page.html", context)




# Function based view with an html script inside
def home_page_old(request):
    html_ = """
        <!doctype html>
    <html lang="en">
      <head>
        <title>Hello, world!</title>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
      </head>
      <body>
        <div class="text-center">
        <h1>Hello, world!</h1>
        </div>

        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>
      </body>
    </html>
    """
    return HttpResponse(html_)