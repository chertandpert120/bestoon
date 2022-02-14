from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
    path('', views.ExpenseList.as_view(), name='list'),
    path('<int:pk>/', views.ExpenseDetail.as_view(), name='detail'),
    path('create/', views.CreateExpense.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateExpense.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteExpense.as_view(), name='delete'),
]