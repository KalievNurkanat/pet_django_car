from django import forms
from users.models import CustomUser

class RegistrationForm(forms.Form):
    image = forms.ImageField(label='image', required=False)
    username = forms.CharField(label="Username", max_length=25)
    email = forms.EmailField(label="Email", max_length=55)
    password = forms.CharField(label="Password")
    confirm_password = forms.CharField(label="Confirm Password")
    ballance = forms.DecimalField(label="Ballance", max_digits=10, decimal_places=2)
    birth_date = forms.DateField(label="Date of birth", widget=forms.DateInput(attrs={'type': 'date'}))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        symbols = sum(not x.isalnum() for x in password)
        if password != confirm_password:
            raise forms.ValidationError("Password do not match")
        
        if not any(x.isupper() for x in password):
                raise forms.ValidationError("Password must contain at least 1 upper letter")
            
        if not any(x.islower() for x in password):
                raise forms.ValidationError("Password must contain at least 1 lower letter")
            
        if not any(x.isdigit() for x in password):
                raise forms.ValidationError("Password must contain at least 1 digit")
            
        if symbols <= 0:
                raise forms.ValidationError("Password must contain at least 1 symbol")
            
        return cleaned_data
            

class LoginForm(forms.Form):
    email = forms.EmailField(label="email", max_length=25)
    password = forms.CharField(label="password")
    
            
            
            
            

