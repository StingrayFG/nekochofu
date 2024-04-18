from django.urls import path
from rest_framework import routers

from quickstart import views


router = routers.SimpleRouter()
router.register(r'record', views.RecordView)

urlpatterns = [
    path('record/add', views.RecordView.add),
]

