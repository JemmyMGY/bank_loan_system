from django import forms
from .models import UserModel, LoanModel


class LogInForm(forms.Form):
    user_email = forms.EmailField(max_length=50, label="Your email")
    user_password = forms.CharField(max_length=16,min_length=8 , widget=forms.PasswordInput, label="Your Password")


class SignUpForm(forms.ModelForm):
    user_password = forms.CharField(max_length=16, min_length=8, widget=forms.PasswordInput)
    class Meta:
        model = UserModel
        fields = "__all__"
        labels = {
            "user_full_name": "Your Full Name",
            "user_name": "Your user_name",
            "user_email" : "Your Email",
            "user_password" : "Your Password",
            "user_age": "Your Age"
        }

        error_messages = {
            "user_name": {
                "unique": "There is another user with this name",

            },
            "user_email" : {
                "primary_key": "This Email is already exist"
            }
        }


class LoanRequestForm(forms.ModelForm):
    loan_amount = forms.DecimalField(required=True, min_value=1, max_value= 1000000000)
    loan_years = forms.IntegerField(required=True, min_value=1, max_value=30)
    class Meta: 
        model = LoanModel

        fields = ["loan_amount", "loan_years"]
        labels = {
            "loan_amount": "Total loan amount",
            "loan_years": "Total payment yeas",
        }

        error_messages = {
            "loan_amount": {
                "required": "This is required value",

            },
            "loan_years" : {
                "required": "This is required value"
            }
        }