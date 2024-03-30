from django.shortcuts import render
from django.urls import reverse
import requests
from bs4 import BeautifulSoup
import urllib.parse
from .models import News1, News2, News3
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

period = {
    "day": "d",
    "week": "w",
    "month": "m"
}

queries = [
    "Мероприятия города Перми",
    "События Перми для туристов",
    "События для владельцев малого бизнеса Перми"
]

# Create your views here.
def extract_links(query, time):
    url = f"https://www.google.com/search?q={query}&tbs=qdr:{period[time]}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.select("a:has(h3)")[:5] # Получаем первые 5 ссылок
        extracted_links = [link["href"] for link in links]
        return extracted_links
    except:
        print("error")
        return None

def parse_page(url, timeout=30):
    try:
        # Получаем HTML-код страницы с таймаутом
        response = requests.get(url, timeout=timeout)
        # Проверяем успешность запроса
        response.raise_for_status()
        
        # Используем BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Извлекаем весь текст с помощью метода get_text()
        page_text = soup.get_text()
        
        return page_text
    except requests.exceptions.Timeout:
        print("Timeout error: Request took too long.")
        return None
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

def index(request):
    return render(request, 'core/index.html')

def login_view(request):
    if request.method == "POST":
        Username = request.POST["username"]
        Password = request.POST["password"]
        user = authenticate(request, username=Username, password=Password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "core/login.html", {
                "username": Username
            })
    return render(request, 'core/login.html')

def events(request):
    events1 = News1.objects.all()
    events2 = News2.objects.all()
    events3 = News3.objects.all()
    return render(request, 'core/events.html', {
        "events1": events1,
        "events2": events2,
        "events3": events3
    })

def day(request):
    events1 = News1.objects.all()
    events2 = News2.objects.all()
    events3 = News3.objects.all()
    return render(request, 'core/day.html', {
        "events1": events1,
        "events2": events2,
        "events3": events3
    })

def week(request):
    events1 = News1.objects.all()
    events2 = News2.objects.all()
    events3 = News3.objects.all()
    return render(request, 'core/week.html', {
        "events1": events1,
        "events2": events2,
        "events3": events3
    })

def month(request):
    events1 = News1.objects.all()
    events2 = News2.objects.all()
    events3 = News3.objects.all()
    return render(request, 'core/month.html', {
        "events1": events1,
        "events2": events2,
        "events3": events3
    })

def generate(request):
    if request.method == 'POST':
        period = request.POST['period']
        news1, created1 = News1.objects.get_or_create(period=period)
        news2, created2 = News2.objects.get_or_create(period=period)
        news3, created3 = News3.objects.get_or_create(period=period)
        if created1: #зависит от того, сгенерированны или нет события. Если да - то записать, Если уже сгенерированны, то удалить и записать новые (обновить)
            pass
        else:
            news1.text = ''
            news1.save()
        if created2:
            pass
        else:
            news2.text = ''
            news2.save()
        if created3:
            pass
        else:
            news3.text = ''
            news3.save()
        for query in queries:
            links = extract_links(query, period)
            for link in links:
                parsed_url = urllib.parse.urlparse(link)
                query_params = urllib.parse.parse_qs(parsed_url.query)
                inner_url = query_params.get('url', [''])[0]
                text = parse_page(inner_url)
                if query == 'Мероприятия города Перми':
                    news1.title = query
                    if text is not None:
                        news1.text = str(news1.text) + text
                    else:
                        pass
                elif query == 'События Перми для туристов':
                    news2.title = query
                    if text is not None:
                        news2.text = str(news2.text) + text
                    else:
                        pass
                else:
                    news3.title = query
                    if text is not None:
                        news3.text = str(news3.text) + text
                    else:
                        pass
            news1.save()
            news2.save()
            news3.save()
        return HttpResponseRedirect(reverse("index"))
    return render(request, 'core/generate.html')
        

             