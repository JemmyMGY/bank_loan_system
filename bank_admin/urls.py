from . import views
from django.urls import path 


urlpatterns = [
    path("", views.AdminLogInView.as_view(), name="admin-log-in-page"),
    path("loans_dashboard/<str:admin_email>", views.LoansBordView.as_view(), name= "admin-loans-dashboard" )
]
