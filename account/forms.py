from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import User, EmailVerification, PasswordResetCode


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="confirm password", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["email"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["email", 'username' ,"password", "is_active"]


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input100', 'placeholder': 'email'}), )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'password'}))

    def clean(self):
        self.cleaned_data = super().clean()
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)
            if user is None:
                raise ValidationError("invalid email or password")
        return self.cleaned_data


class RegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input100', 'placeholder': 'email'}), )
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'username'}))
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'fullname'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'confirm password'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("username already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("email already taken")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        validate_password(password1)

        if len(password1) < 8:
            raise ValidationError('password must be more than 8 characters')

        return password1

    def clean_password2(self):
        password2 = self.cleaned_data['password2']
        if password2 is None:
            raise ValidationError('this field is required')
        return password2

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("invalid password")

        return cleaned_data


class VerifyEmailForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'verification code'}))

    def clean_code(self):
        code = self.cleaned_data['code']
        if EmailVerification.objects.filter(code=code) is None:
            raise ValidationError('invalid verification code')


class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input100', 'placeholder': 'email'}), )

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("this email is not registered")
        return email


class PasswordVerifyForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'code'}))

    def clean_code(self):
        code = self.cleaned_data['code']
        try:
            if not PasswordResetCode.objects.filter(code=code).exists():
                raise forms.ValidationError("Invalid code")
        except PasswordResetCode.DoesNotExist:
            raise forms.ValidationError("Invalid code")

        return code


class SetNewPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'password'}))
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'confirm password'}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def clean_password1(self):
        new_password = self.cleaned_data.get('new_password')
        validate_password(new_password)

        if len(new_password) < 8:
            raise ValidationError('password must be more than 8 characters')

        return new_password
