from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from datetime import datetime  
# Create your models here.

class UserModel(models.Model):
    user_full_name = models.CharField(max_length=50)
    user_name =  models.CharField(max_length=10, unique=True, db_index=True)
    user_email = models.EmailField(primary_key=True, max_length=50,  db_index=True)
    user_password = models.CharField(max_length=16, validators=[MinLengthValidator(8)])
    user_age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(60)])

    def __str__(self) -> str:
        return f'{self.user_name} || {self.user_email}'

    def get_user_object(self):
        return {
            "full_name" : self.user_full_name,
            "user_name" : self.user_name,
            "email" : self.user_email,
            "password" : self.user_password,
            "age" : self.user_age
        }

    

class LoanModel(models.Model):
    is_approved = models.BooleanField(default=False) 
    user_requested = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2)
    loan_years = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    request_date_time = models.DateTimeField(default=datetime.now, blank=True)
    monthly_payment = models.DecimalField(max_digits=12, decimal_places=2)
    num_of_payments = models.IntegerField()
    rate_per_period = models.DecimalField(max_digits=4, decimal_places=3)
    total_payment = models.DecimalField(max_digits=12, decimal_places=2)
    total_interest = models.DecimalField(max_digits=12, decimal_places=2)
    

    @classmethod
    def get_fields_names(self):
        return [f.name for f in self._meta.fields]

    def __str__(self) -> str:
        return f'{self.user_requested} || {self.loan_amount} || {self.is_approved}'
    
    def get_loan_object(self):
        return {
            "user_requested" : self.user_requested,
            "loan_amount" : self.loan_amount,
            "loan_years" : self.loan_years,
            "request_date_time" : self.request_date_time,
            "monthly_payment" : self.monthly_payment,
            "num_of_payments" : self.num_of_payments,
            "rate_per_period" : self.rate_per_period,
            "total_payment" : self.total_payment,
            "total_interest" : self.total_interest,
            "is_approved" : self.is_approved
              

        }

