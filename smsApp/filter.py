import django_filters
from django_filters import *
from .models import Student
GENDER = (
    ('Female','Female'),
    ('Male','Male'),
)

class StudentFilter(django_filters.FilterSet):
    name = CharFilter(field_name='firstname', lookup_expr='icontains')
    gender = ChoiceFilter(choices = GENDER)
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['lastname', 'email', 'phone','date_added','firstname']