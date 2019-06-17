from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='Почта', max_length=100)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())

class RegistrationForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    surname = forms.CharField(label='Фамилия', max_length=100)
    email = forms.EmailField(label='Почта', max_length=100)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


