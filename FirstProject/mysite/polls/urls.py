from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [

    path('', views.index, name="index"),
    path('<q_id>/', views.detail, name="detail"),
    path('<q_id>/results/', views.results, name="results"),
    path('<q_id>/vote/', views.vote, name="vote"),
]