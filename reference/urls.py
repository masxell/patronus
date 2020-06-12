from django.urls import path
from . import views

app_name = 'reference'
urlpatterns = [
    path('', views.reference_list, name='reference_list'),
    path('references/add/', views.ReferenceCreateView.as_view(), name='reference_create'),
    path('references/<int:pk>/update/', views.ReferenceUpdateView.as_view(), name='reference_update'),
    path('references/<int:pk>/delete/', views.ReferenceDeleteView.as_view(), name='reference_delete'),
]