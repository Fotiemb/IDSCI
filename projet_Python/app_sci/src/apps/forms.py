from django.forms import ModelForm

from apps.models import ProfilStudent, BookModel


class profilStudentForm(ModelForm):
    class Meta:
        model = ProfilStudent
        fields = ['name', 'email', 'telephone', 'photo']


class BookForm(ModelForm):
    class Meta:
        model = BookModel
        fields = '__all__'
