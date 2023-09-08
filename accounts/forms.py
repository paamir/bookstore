from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUserModel


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        # fields = UserCreationForm.Meta.fields + ('age', )
        fields = ('username', 'email', 'age', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUserModel
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'email', 'age', 'first_name', 'last_name')