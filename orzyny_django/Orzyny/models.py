from django.db import models


# Create your models here.


class Ocr(models.Model):
    image = models.ImageField(upload_to='images/')


#PEOPLE = (
#    (0, "Wszyscy"),
 #   (1, "Hubert F."),
  #  (2, "Karolina Ż."),
   # (3, "Adam S."),
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
 #   product = models.TextField()
  #  quantity = models.IntegerField(default=0)
   # people = models.IntegerField(choices=PEOPLE, default=0)



class ImageText(models.Model):
    ocr_id = models.ForeignKey(Ocr, on_delete=models.CASCADE)
    original_sentence = models.CharField(max_length=5000)
    translated_sentence = models.CharField(max_length=5000, blank=True, null=True)