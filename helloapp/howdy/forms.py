from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='Courriel')
    password = forms.CharField(label='Mot de passe',
                        widget = forms.PasswordInput)
