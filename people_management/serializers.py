from rest_framework.serializers import ModelSerializer
from people_management.models import Person, Jobs, Company


class CompanyListSerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']


class JobsListCreateSerializer(ModelSerializer):
    company = CompanyListSerializer(read_only=True)

    class Meta:
        model = Jobs
        fields = ['id', 'name', 'descripion', 'status',
                  'salary', 'company', 'created_at']


class JobsDetailSerializer(ModelSerializer):

    class Meta:
        model = Jobs
        fields = ['id', 'name', 'descripion', 'status',
                  'salary', 'company', 'created_at']


class PersonListCreateSerializer(ModelSerializer):
    jobs = JobsDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = ['id', 'name', 'email', 'phone', 'status', 'bio', 'jobs']


class PersonDetailSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'email', 'phone', 'status', 'bio', 'jobs']
