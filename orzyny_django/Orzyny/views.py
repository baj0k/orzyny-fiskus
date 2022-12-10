from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpRequest, Http404, HttpResponse
from django.views import View

# Create your views here.

def button(request):
    if request.method == "GET":
        return render(request, "button.html")
    if request.method == "POST":
        return HttpResponse('<html><body>Miejsce dodane</body></html>')