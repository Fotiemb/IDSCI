from django.db import models

"""class Books(models.Model):
    isbm = models.CharField(unique=True)
    auteur = models.CharField()
    editeur = models.CharField()
    libelle = models.CharField()
    exemplaire = models.CharField()"""


class ProfilStudent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=10)
    photo = models.FileField(upload_to="photos")


class BookModel(models.Model):
    isbm = models.CharField(max_length=11, primary_key=True)
    auteur = models.CharField(max_length=30)
    editioin = models.CharField(max_length=30)
    libelle = models.CharField(max_length=30)
    exemplaire = models.CharField(max_length=30)
    domaine = models.CharField(max_length=30)
    photo = models.FileField(upload_to="books")

    class Meta:
        verbose_name = "Livre"
