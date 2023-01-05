from django.urls import path
from . import views

urlpatterns = [
    path("", views.LogInView.as_view(), name="user-log-in-page"),
    path("sign_up_page", views.SignUpView.as_view(), name="user-sign-up-page"),
    path("all_users", views.UsersBoardView.as_view(), name="all-users-page"),
    path("loan_request_page/<str:user_email>", views.LoanRequestView.as_view(), name= "loan-request-page"),
    path("loan_dashboard/<str:user_email>", views.LoansDashboardView.as_view(), name="loans-dashboard")
]
