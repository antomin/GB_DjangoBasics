import hashlib
import random

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
from django.forms import fields
from pyexpat import model

from .models import ShopUser, ShopUserProfile


class ShopUserLoginForm(AuthenticationForm):
    # Вся это конструкция только для добавления класса?
    def __init__(self, *args, **kwargs):
        # Не понятно зачем это выражение? Наследование конструктора у самого себя?
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    #  ... до сюда
    class Meta:
        model = ShopUser
        fields = ("username", "password")


class ShopUserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(ShopUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    def clean_age(self):
        data = self.cleaned_data["age"]
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return data

    def clean_username(self):
        data = self.cleaned_data["username"]
        if len(data) < 5:
            raise forms.ValidationError("Имя пользователя должно содержать от 6 символов")
        return data

    def save(self):
        user = super(ShopUserRegisterForm, self).save()

        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode("utf8")).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode("utf8")).hexdigest()
        user.save()

        return user

    class Meta:
        model = ShopUser
        fields = ("username", "first_name", "password1", "password2", "email", "age", "avatar")


class ShopUserEditForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(ShopUserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    def clean_age(self):
        data = self.cleaned_data["age"]
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return data

    def clean_username(self):
        data = self.cleaned_data["username"]
        if len(data) < 5:
            raise forms.ValidationError("Имя пользователя должно содержать от 6 символов")
        return data

    class Meta:
        model = ShopUser
        fields = ("username", "first_name", "email", "age", "avatar")


class ShopUserProfileEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ShopUserProfileEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = ShopUserProfile
        fields = ("tagline", "aboutMe", "gender")
