from django.contrib.auth.forms import AuthenticationForm
from django.forms import fields

from .models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    # Вся это конструкция только для добавления класса?
    def __init__(self, *args, **kwargs):
        # Не понятно зачем это выражение? Наследование конструктора у самого себя?
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    #  ... до сюда
    class Meta:
        model = ShopUser
        fields = ('username', 'password')
