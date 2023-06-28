from django.shortcuts import render

# Create your views here.

def home(request):
    data = {
        "css_file" : "home",
    }
    return render(request, 'index.html', data)


def analysis(request):
    data = {
        "page_title" : "| Analysis",
        "css_file" : "analysis",
    }
    return render(request, 'analysis.html', data)


def about(request):
    data = {
        "page_title" : "| About",
        "css_file" : "about",
    }
    return render(request, 'about.html', data)