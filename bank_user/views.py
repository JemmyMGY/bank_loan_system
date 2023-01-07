from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponseServerError, HttpResponseRedirect
from django.urls import reverse
from .models import LoanModel, UserModel
from .forms import LogInForm, SignUpForm, LoanRequestForm
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from .loan_calculator import  LoanCalculator

# Create your views here.

def get_all_loans():
    try:
        return LoanModel.objects.all()
    except:
        return None

def get_user_loans(user_email):
    try:
        return get_all_loans().filter(user_requested = user_email)
    except:
        None

def get_user(user_name):
    try: 
       return UserModel.objects.get(user_name = user_name)
    except:
        return None

def get_user_by_email(user_email):
    try: 
       return UserModel.objects.get(user_email = user_email)
    except:
        return None


class LogInView(FormView):
    template_name = "bank_user/log_in_page.html"
    form_class = LogInForm
    
    def get_success_url(self):
        return reverse("loans-dashboard", kwargs = {"user_email" : self.request.POST["user_email"]} )
        
    def form_valid(self, form):
        user_info = form.cleaned_data
        user_details = get_user_by_email(user_info['user_email'])
        if user_details and user_details.user_password == user_info["user_password"]:
            return HttpResponseRedirect(self.get_success_url())
        return render(self.request, "bank_user/log_in_page.html", {"form" : form, "msg" : "Invalid email or password"})

        

class SignUpView(FormView):
    template_name = "bank_user/sign_up_page.html"
    form_class = SignUpForm

    def get_success_url(self):
        return reverse("loans-dashboard", kwargs = {"user_email" : self.request.POST["user_email"]} )

    def form_valid(self, form):
        try:
            form.save()
        except: 
            raise HttpResponseServerError("Error happened while making your account")
       
        return HttpResponseRedirect(self.get_success_url())
       

class LoansDashboardView(ListView):
    template_name = "bank_user/loan_dashboard.html"
    model = LoanModel
    context_object_name = "all_user_loans"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["user_email"] = self.kwargs["user_email"]
        loan_columns = LoanModel.get_fields_names()
        loan_columns = [field for field in loan_columns if field != "user_requested"]
        context["column_names"] = loan_columns
        return context

    def get_queryset(self):
        query_set = super().get_queryset()
        user_info = get_user_by_email(self.kwargs["user_email"])
        if user_info is None:
            raise HttpResponseForbidden("forbidden access")

        query_set = get_all_loans().filter(user_requested = user_info).values()
        return query_set 


def make_loan_request(input_data):
    return LoanCalculator(float(input_data["loan_amount"]), input_data["loan_years"])

def insert_loan(loan_request, user_email):
    loan_result = loan_request.get_result_summary()
    loan_requester = get_user_by_email(user_email)

    loan_db = LoanModel(user_requested = loan_requester,loan_amount = loan_result["loan_amount"],
    loan_years = loan_result["loan_years"], monthly_payment = loan_result["monthly_payment"], num_of_payments = loan_result["num_of_payments"], rate_per_period = loan_result["rate_per_period"], 
    total_payment = loan_result["total_payment"], total_interest = loan_result["total_interest"])

    return loan_db

class LoanRequestView(FormView):
    template_name = "bank_user/loan_request_page.html"
    form_class = LoanRequestForm

    def get_success_url(self):
        user_email = self.kwargs["user_email"]
        if 'apply' in self.request.POST :    
            return reverse("loans-dashboard", kwargs = {"user_email" : user_email})
        elif 'calculate' in self.request.POST:
            return reverse("loan-request-page", kwargs = {"user_email" : user_email} )
        return super().get_success_url


    def form_valid(self, form):
        response = super().form_valid(form)
        input_data = form.cleaned_data
        loan_request = make_loan_request(input_data)

        if  'apply' in self.request.POST:
            loan_db = insert_loan(loan_request, self.kwargs["user_email"])
            loan_db.save()
            return HttpResponseRedirect(self.get_success_url())
        elif  'calculate' in self.request.POST:
            loan_schedule = loan_request.generate_Schedule()
            loan_results = loan_request.get_result_summary()
            return render(self.request, 'bank_user/loan_request_page.html', {'form': form , "loan_results" : loan_results, "loan_schedule" : loan_schedule , "loan_schedule_columns" : loan_schedule[0].keys()})
        
        return response
