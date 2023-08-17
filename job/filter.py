import django_filters
from .models import Jop

class JobFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(lookup_expr='icontains')
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Jop
        fields = '__all__'
        exclude = ['published_at','vacancy','salary','image','slug','owner',]