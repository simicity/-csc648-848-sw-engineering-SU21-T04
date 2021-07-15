from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=40,
        required=True
    )
    email = forms.EmailField(
        label='Email',
        max_length=100,
        required=True
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        max_length=100,
        required=True
    )
    confirmPassword = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(),
        max_length=100,
        required=True
    )
    avatar = forms.ImageField(
        label='Avatar',
        required=False
    )
    tosCheck = forms.NullBooleanField(
        label='I agree to Terms of Service',
        widget=forms.CheckboxInput()
    )


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        max_length=100,
        required=True
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        max_length=100,
        required=True
    )


class ContactForm(forms.Form):
    fullname = forms.CharField(
        label='Full Name',
        max_length=45,
        required=True
    )
    telephone = forms.CharField(
        label='Telephone',
        max_length=15,
        required=True
    )
    email = forms.EmailField(
        label='Email',
        max_length=45,
        required=True
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(),
        max_length=200,
        required=True
    )


class StudyGroupForm(forms.Form):
    groupName = forms.CharField(
        label='Study Group Name', 
        max_length = 100, 
        required=True
    )
    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(),
        max_length = 5000,
        required=True
    )
