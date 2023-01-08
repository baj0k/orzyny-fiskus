from django import forms
from .models import Ocr


class ImageUpload(forms.ModelForm):
    class Meta:
        model = Ocr
        fields = ['image']

#PEOPLE = (
#     (0, "Wszyscy"),
#     (1, "Hubert F."),
#     (2, "Karolina Ż."),
#     (3, "Adam S."),
#     (4, "Agata F."),
#     (5, "Ola B."),
#     (6, "Bartek Ś."),
#     (7, "Filip H."),
#     (8, "Gosia W."),
#     (9, "Karolina K."),
#     (10, "Kinga K."),
#     (11, "Krzysztof B."),
#     (12, "Kuba P."),
#     (13, "Maks K."),
#     (14, "Mateusz Z."),
#     (15, "Patryk D."),
#     (16, "Wiola S.")
# )

#class ShoppingList(forms.ModelForm):
 #   item = forms.CharField()
  #  quantity = forms.IntegerField(default=0)
   # person = forms.IntegerField(choices=PEOPLE, default=0)