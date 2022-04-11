from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'


class AuthUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "password1", "password2")

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = f'form-control {field_name}'
                field.help_text = ''


class AuthUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email", "age", "avatar")

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = f'form-control {field_name}'
                field.help_text = ''
