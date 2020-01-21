from django.urls import path
from people_management.views import (
    JobsListCreate,
    JobsDetail,
    PersonListCreate,
    PersonDetail
)
urlpatterns = [
    path('jobs/', JobsListCreate.as_view(), name=JobsListCreate.name),
    path('jobs/<int:pk>/', JobsDetail.as_view(), name=JobsDetail.name),
    path('jobs/persons/', PersonListCreate.as_view(), name=PersonListCreate.name),
    path('jobs/person/<int:pk>/', PersonDetail.as_view(), name=PersonDetail.name)
]
