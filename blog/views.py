from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random

# Create your views here.

def models_list(request):
    return HttpResponse("ČAU KERES")



def colorful_time(request):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    color_code = "#{:06x}".format(random.randint(0, 0xFFFFFF))

    response_html = f"<div style='display: flex; align-items: center; justify-content: center; height: 100vh;'>"
    response_html += f"<p style='color: {color_code}; font-size: 24px;'>Aktuální čas: {current_time}</p>"
    response_html += "</div>"

    return HttpResponse(response_html)

