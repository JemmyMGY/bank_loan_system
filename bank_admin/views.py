from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import FormView, TemplateView
from django.views import View
from django.urls import reverse, reverse_lazy
from bank_user.models import LoanModel
from .models import AdminModel
from .forms import AdminLogInForm
from django.http import  HttpResponseRedirect, HttpResponse
# Create your views here.
# def reject_all_loans():
#     try:
#         all_loans = LoanModel.objects.all()
#         all_loans.update(is_approved = False)
#         return True
#     except:
#         return False

def get_admin(admin_email):
    try:
        return AdminModel.objects.all().get(admin_email = admin_email)
    except:
        return None

def get_all_pending_loans():
    try:
        return LoanModel.objects.all().filter(is_approved = False)
    except:
        return None

def accept_loan_by_id(loan_id):
    try:
        approved_loan = get_all_pending_loans().get(id = loan_id)
        approved_loan.is_approved = True
        approved_loan.save()
        return True
    except:
        return None

class AdminLogInView(FormView):
    template_name = "bank_admin/log_in_page.html"
    form_class = AdminLogInForm

    def get_success_url(self):
        return reverse_lazy("admin-loans-dashboard", kwargs={"admin_email" : self.request.POST["admin_email"]})

    def form_valid(self, form):
        admin_account = get_admin(self.request.POST["admin_email"])
        if admin_account and form.cleaned_data["admin_password"] == admin_account.admin_password:
            return HttpResponseRedirect(self.get_success_url())
        return render(self.request, "bank_admin/log_in_page.html", {"form" : form, "msg" : "Invalid email or password"})



class LoansBordView(View):
    
    def get(self, request, *args, **kwargs):
        admin = get_admin(kwargs["admin_email"])
        if not admin:
            return render(request, "bank_admin/log_in_page.html")
        all_pending_loans = get_all_pending_loans()
        column_names = LoanModel.get_fields_names()
        return render(request, "bank_admin/all_loans_dashboard.html" , { "column_names" : column_names, "all_pending_loans" : all_pending_loans.values(), "admin_email" : kwargs["admin_email"] } )


    def post(self, request, *args, **kwargs):
        admin_email = kwargs["admin_email"]
        loan_id = request.POST["accept"]
        if accept_loan_by_id(loan_id):
            redirect_to = reverse_lazy("admin-loans-dashboard", kwargs = {"admin_email": admin_email})
            return HttpResponseRedirect(redirect_to)
            

        return HttpResponse("not confirmed")
        




    