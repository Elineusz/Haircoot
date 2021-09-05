from django import forms
from django.forms import SelectDateWidget
from models import Service, User

class LoginForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(widget=forms.PasswordInput, label='Hasło')
    password_confirmation = forms.CharField(widget=forms.PasswordInput, label='Password confirmation')
    email = forms.EmailField(label='Adres email')
    first_name = forms.CharField(label='Imię')
    surname = forms.CharField(label='Nazwisko')


class NewService(forms.Form):
    service_name = forms.CharField(label='Nazwa usługi' , widget=forms.Textarea(attrs={'rows': 1, 'cols': 50}))
    service_detailed = forms.CharField(label='Opis usługi', widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}))
    service_duration = forms.DurationField(label='Czas wykonania usługi w minutach')
    service_price = forms.FloatField(label='Cena usługi w złotówkach')


class Reservation(forms.Form):
    service = forms.ModelChoiceField(label='Usługa', queryset=Service.objects.all())
    employee = forms.ModelChoiceField(label='Pracownik', queryset=User.objects.filter(is_staff=1))

class OneTimeReservation(forms.Form):
    service = forms.CharField(label='Usługa')
