from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, \
    UserChangeForm


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Логин", widget=forms.TextInput(
        attrs={"placeholder": "example@example.ru"}))
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")

    class Meta:
        model = get_user_model()
        fields = ("email", "password1")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'


class AuthUserCreationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label="Подтвердите пароль")
    email = forms.EmailField(label="Логин", widget=forms.TextInput(
        attrs={"placeholder": "example@example.ru"}))

    class Meta:
        model = get_user_model()
        fields = ("email", "password1", "password2")

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = f'form-control {field_name}'
                field.help_text = ''


class AuthUserChangeForm(UserChangeForm):
    email = forms.EmailField(label="Логин", widget=forms.TextInput(
        attrs={"readonly": "readonly"}))
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = get_user_model()
        fields = ("email", "first_name", "last_name", "age", "avatar")

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = f'form-control {field_name}'
                field.help_text = ''

