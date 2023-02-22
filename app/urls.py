from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio_detail/<int:id>', views.detailPortfolio, name='detailPortfolio'),

]