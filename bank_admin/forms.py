from django import forms



class AdminLogInForm(forms.Form):
    admin_email = forms.EmailField(max_length=50, label="Your email")
    admin_password = forms.CharField(max_length=16,min_length=8 , widget=forms.PasswordInput, label="Your Password")