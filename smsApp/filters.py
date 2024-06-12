import django_filters
from django_filters import *
from .models import Student

class StudentFilter(django_filters.FilterSet):
    gender = ChoiceFilter(choices= GENDER)
    name = CharFilter(field_name='firstname', lookup_expr='icontains')
    class Meta:
        model = Student
        fields = '__all__'