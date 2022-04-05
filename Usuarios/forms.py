from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Usuarios


class UsuarioCreateForm(UserCreationForm):

    class Meta:
        model = Usuarios
        fields = ['first_name', 'last_name', 'phone', 'email']
        labels = {'username': 'Username'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UsuarioChangeForm(UserChangeForm):

    class Meta:
        model = Usuarios
        fields = ['username', 'first_name', 'last_name', 'phone', 'email']

    def __init__(self, *args, **kwargs):
        super(UsuarioChangeForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})