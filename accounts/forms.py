from django import forms
# Есть 2 вида форм
# ModelForm - формы основанные на полях модели
# Form - Обычная форма

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

