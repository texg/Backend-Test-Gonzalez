from django import forms
from .models import Menu, Option, Order
import arrow


class MenuCreate(forms.ModelForm):
    class Meta:
        model = Menu
        fields = [
            "title_menu",
            "menu_date"
        ]

    def clean_menu_date(self):
        date = self.cleaned_data.get('menu_date')

        if arrow.get(date).date() < arrow.utcnow().date():
            msg = "Date must be greater or equal to today"
            raise forms.ValidationError(msg)
        else:
            return self.cleaned_data.get('menu_date')


class OptionCreate(forms.ModelForm):
    class Meta:
        model = Option
        fields = ["title_option"]


class OrderCreate(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["option_selected"]

    def clean(self):
        cleaned_data = super().clean()
        option = cleaned_data.get('option_selected')
        date_option = option.menu.menu_date
        date_arrow = arrow.get(date_option).replace(hour=11, minute=0, second=0)
        if arrow.utcnow() > date_arrow:
            msg = "Date error, date can't be greater"
            raise forms.ValidationError(msg)

        return self.cleaned_data
