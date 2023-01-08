from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpRequest, Http404, HttpResponse
from django.views import View
import pytesseract
from .forms import ImageUpload
import os
from PIL import Image
from django.conf import settings


# Create your views here.
class Index(View):
    def get(self,request):
        return render(request, "formpage.html")
    def post(self,request):
        text = ""
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            # try:
            form.save()
            image = request.FILES['image']
            image = image.name
            path = settings.MEDIA_ROOT
            pathz = path + "/images/" + image

            text = pytesseract.image_to_string(Image.open(pathz))
            text = text.encode("ascii", "ignore")
            text = text.decode().split(' ')
            os.remove(pathz)
            # except:
            #     message = "check your filename and ensure it doesn't have any space or check if it has any text"
        return render(request, 'result.html', {'text': text})


