from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random
import math
import hashlib
import secrets


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

def random_predicted_number(secret_number):
    # Převedení tajného čísla na řetězec
    secret_str = str(secret_number)

    # Hashování tajného čísla
    hash_value = hashlib.sha256(secret_str.encode()).hexdigest()

    # Konverze hash hodnoty na číslo v rozsahu 1-100
    hash_number = int(hash_value, 16)
    scaled_number = hash_number % 100 + 1

    # Zvýšení čísla o 16 a zajištění, že zůstane v rozsahu 1-100
    generated_number = (scaled_number + 16) % 100
    if generated_number == 0:
        generated_number = 100

    return generated_number

def generate_random_number(request):
    # Tajné číslo, které budeme používat pro generování náhodných čísel
    secret_number = 16  # Zde vložte vaše tajné číslo

    # Generování předpovídaného čísla na základě tajného čísla
    predicted_number = random_predicted_number(secret_number)

    # Vracení výsledného čísla v HttpResponse
    return HttpResponse(f"Vaše tajné náhodné číslo v rozsahu 1-100: {predicted_number}")