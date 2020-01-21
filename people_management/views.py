from people_management.models import Person, Jobs, Company
from people_management.serializers import (
    JobsListCreateSerializer,
    JobsDetailSerializer,
    PersonListCreateSerializer,
    PersonDetailSerializer
)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class JobsListCreate(ListCreateAPIView):
    queryset = Jobs.objects.filter(status=True)
    serializer_class = JobsListCreateSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
    name = 'list-and-create-jobs'


class JobsDetail(RetrieveUpdateDestroyAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobsDetailSerializer
    name = 'detail-update-and-delete-jobs'


class PersonListCreate(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonListCreateSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
    name = 'list-and-create-people'


class PersonDetail(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonDetailSerializer
    name = 'detail-update-and-delete-person'
