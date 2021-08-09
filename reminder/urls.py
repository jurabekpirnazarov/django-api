from django.urls import path
from .views import RemainderList,RemainderDetail


urlpatterns = [
    path('<int:pk>/',RemainderList.as_view()),
    path('', RemainderDetail.as_view())

]