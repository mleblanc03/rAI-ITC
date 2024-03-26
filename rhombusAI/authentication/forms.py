from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'password-field'})
        self.fields['new_password1'].widget.attrs.update({'class': 'password-field'})
        self.fields['new_password2'].widget.attrs.update({'class': 'password-field'})

class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')

class profilePhotoForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('profile_photo',)
