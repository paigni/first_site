from django import forms


class UserForm(forms.Form):
    regul = forms.CharField(label="Регулярное выражение")
    comment = forms.CharField(label="Ваш текст", widget=forms.Textarea)