from django.shortcuts import render
from django.conf import settings
from .models import Images
import datetime
# For ML
import numpy as np
import tensorflow
model = tensorflow.keras.models.load_model('Model.h5')
from tensorflow import keras
from keras.utils import load_img, img_to_array   
import cv2           

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
            cyclone_image = request.FILES['image']
            if cyclone_image:
                now = datetime.datetime.now()
                filename = now.strftime("%d-%m-%Y-%H-%M-%S") + "." + cyclone_image.name.split('.')[-1]
                uploaded_image = Images.objects.create()
                uploaded_image.original_image.save(filename, cyclone_image)
                uploaded_image_url = uploaded_image.original_image.url
                
                # Loading Image
                # Because Direct path such as /media/images/03-07-2023-15-31-54.jpeg will not work
                # So we need to give media/images/03-07-2023-15-31-54.jpeg this as a relative path
                # Source: https://stackoverflow.com/a/69493498/22150559
                base_path = uploaded_image_url[1:]
                
                
                # Itensify of cyclone
                img_size = 512
                img = load_img(base_path, target_size=(img_size, img_size))
                img_array = img_to_array(img)
                img_batch = np.expand_dims(img_array, axis=0)
                prediction = (model.predict(img_batch) / 40)
                ans = round((prediction[0][0] * 18) / 5, 2)
                print("Intensity of cyclone is: ", ans)
                
                
                # Features of cyclone
                # Feature-1
                img0 = cv2.imread(base_path, cv2.IMREAD_GRAYSCALE)
                temperature_ranges = {'dark_blue': (200, 230), 'darkest_blue': (150, 200)}
                dark_blue_mask = cv2.inRange(img0, temperature_ranges['dark_blue'][0], temperature_ranges['dark_blue'][1])
                darkest_blue_mask = cv2.inRange(img0, temperature_ranges['darkest_blue'][0], temperature_ranges['darkest_blue'][1])
                areas_of_interest = cv2.bitwise_or(dark_blue_mask, darkest_blue_mask)
                areas_of_interest_bgr = cv2.cvtColor(areas_of_interest, cv2.COLOR_GRAY2BGR)
                areas_of_interest_bgr[np.where((areas_of_interest_bgr == [255, 255, 255]).all(axis=2))] = [0, 0, 255]
                marked_image = cv2.addWeighted(cv2.cvtColor(img0, cv2.COLOR_GRAY2BGR), 1, areas_of_interest_bgr, 0.5, 0)
            
                # To store edited-0 image
                e0_fn = "media/e0/" + "e0-" + filename
                cv2.imwrite(e0_fn, marked_image)

                # To access edited-1 image
                e0_temp = "e0/" + "e0-" + filename
                e0_url = settings.MEDIA_URL + e0_temp
                print(1)
                
                
                # Feature-2
                img1 = cv2.imread(base_path)
                
                # Same color features
                # edges = cv2.Canny(img1, 50, 100)
                # contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
                # for contour in contours:
                #     cv2.drawContours(img1, [contour], -1, (255, 0, 0), 1)
                
                # Different color features
                edges = cv2.Canny(img1, 50, 100)
                contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
                cs = sorted(contours, key=cv2.contourArea, reverse=True)
                colors = [(0, 0, 255), (0, 0, 200), (0, 0, 150), (0, 0, 100), (0, 0, 50)]
                for i, contour in enumerate(cs):
                    color = colors[i % len(colors)]
                    cv2.drawContours(img1, [contour], -1, color, 1)
                              
                # To store edited-1 image
                e1_fn = "media/e1/" + "e1-" + filename
                cv2.imwrite(e1_fn, img1)

                # To access edited-1 image
                e1_temp = "e1/" + "e1-" + filename
                e1_url = settings.MEDIA_URL + e1_temp
                print(2)
                
                
                # Feature-3
                img2 = cv2.imread(base_path)
                blur = cv2.GaussianBlur(img2, (5, 5), 0)
                edges = cv2.Canny(blur, 100, 200)
                contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
                largest_contour = max(contours, key=cv2.contourArea)
                (x, y), radius = cv2.minEnclosingCircle(largest_contour)
                # cv2.circle(img2, (int(x), int(y)), int(radius), (0, 255, 0), -1)
                # cv2.line(img2, (int(x), 0), (int(x), img2.shape[0]), (255, 0, 0), 1)  # Vertical line
                # cv2.line(img2, (0, int(y)), (img2.shape[1], int(y)), (255, 0, 0), 1)  # Horizontal line
                cv2.circle(img2, (int(x), int(y)), int(radius), (0, 255, 0), -1)
                cv2.line(img2, (int(x), 0), (int(x), img2.shape[0]), (255, 0, 0), 1)  # Vertical line
                cv2.line(img2, (0, int(y)), (img2.shape[1], int(y)), (255, 0, 0), 1)  # Horizontal line
                                
                # To store edited-2 image
                e2_fn = "media/e2/" + "e2-" + filename
                cv2.imwrite(e2_fn, img2)

                # To access edited-2 image
                e2_temp = "e2/" + "e2-" + filename
                e2_url = settings.MEDIA_URL + e2_temp
                print(3)
                
                
                # Location
                width, height = 350, 350
                center_x = width // 2
                center_y = height // 2
                print(x, y)
                # Determine location based on x and y coordinates
                if x < center_x and y < center_y:
                    location = "North-West"
                elif x >= center_x and y < center_y:
                    location = "North-East"
                elif x < center_x and y >= center_y:
                    location = "South-West"
                elif x >= center_x and y >= center_y:
                    location = "South-East"
                elif x == center_x:
                    location = "North" if y < center_y else "South"
                elif y == center_y:
                    location = "West" if x < center_x else "East"


                # Cyclone Type
                if ans <= 31:
                    cyclone_type = "Low pressure Area"
                elif ans <= 49:
                    cyclone_type = "Depression"
                elif ans <= 61:
                    cyclone_type = "Deep Depression"
                elif ans <= 88:
                    cyclone_type = "Cyclonic Storm"
                elif ans <= 118:
                    cyclone_type = "Severe Cyclonic Storm"
                elif ans <= 221:
                    cyclone_type = "Very Severe Cyclonic Storm"
                elif ans > 221:
                    cyclone_type = "Super Cyclonic Storm"
                
                # "uploaded_image_url": uploaded_image_url,
                data = {
                    "page_title" : "| Analysis",
                    "css_file" : "analysis",
                    "e0_url": e0_url,
                    "e1_url": e1_url,
                    "e2_url": e2_url,
                    "result": ans,
                    "cyclone_type": cyclone_type,
                    "location": location,
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