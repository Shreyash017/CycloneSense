from django.shortcuts import render
from .models import Images
import datetime

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
    
    try:
        if request.method == 'POST':
            image = request.FILES['image']
            if image:
                now = datetime.datetime.now()
                filename = filename = now.strftime("%d-%m-%Y-%H-%M-%S") + "." + image.name.split('.')[-1]
                uploaded_image = Images.objects.create()
                uploaded_image.image.save(filename, image)
                image_url = uploaded_image.image.url
                data = {
                    "page_title" : "| Analysis",
                    "css_file" : "analysis",
                    "image_url": image_url,
                }
                return render(request, 'analysis.html', data)
            else:
                print("No image uploaded")
    except Exception as e:
        print("Error: ", e)
        
    return render(request, 'analysis.html', data)


def about(request):
    data = {
        "page_title" : "| About",
        "css_file" : "about",
    }
    return render(request, 'about.html', data)