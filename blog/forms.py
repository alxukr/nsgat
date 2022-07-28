from django import forms
from django.core.exceptions import ValidationError
from .models import ContactMessage
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField, CaptchaTextInput


class CustomCaptchaTextInput(CaptchaTextInput):
    template_name = 'blog/captcha.html'


class ContactMessageForm(forms.ModelForm):
    capatcha = CaptchaField(widget=CustomCaptchaTextInput, label='Защита от роботов')

    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'title', 'content')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control text-bg-dark border-secondary',
                'placeholder': 'Ваше имя'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control text-bg-dark border-secondary',
                'placeholder': 'Ваш e-mail адрес'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control text-bg-dark border-secondary',
                'placeholder': 'тема сообщения'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control text-bg-dark border-secondary',
                'rows': 7,
                'placeholder': 'введите текст сообщения'
            }),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise ValidationError('Имя должно быть от 3 до 255 символов')
        return name

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise ValidationError('Название темы должно быть от 3 до 255 символов')
        return title

    def clean_content(self):
        content = self.cleaned_data['content']
        if not (10 <= len(content) <= 500):
            raise ValidationError('Сообщение должно быть от 10 до 500 символов')
        return content


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={
            'class': 'form-control text-bg-dark border-secondary',
            'placeholder': 'Введите логин'
        })
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control text-bg-dark border-secondary',
            'placeholder': 'Введите e-mail адрес'
        })
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control text-bg-dark border-secondary',
            'placeholder': 'Введите пароль'
        })
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control text-bg-dark border-secondary',
            'placeholder': 'Введите пароль еще раз'
        })
    )
    capatcha = CaptchaField(widget=CustomCaptchaTextInput, label='Защита от роботов')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={
            'class': 'form-control text-bg-dark border-secondary',
            'placeholder': 'Введите логин'
        })
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control text-bg-dark border-secondary',
            'placeholder': 'Введите пароль'
        })
    )
