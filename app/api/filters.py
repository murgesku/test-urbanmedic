from django_filters import rest_framework as filters

from .models import AssignedExercise


class AssignedExerciseFilter(filters.FilterSet):
    date = filters.DateFilter(method='custom_date_filter')

    class Meta:
        model = AssignedExercise
        fields = ['doctor', 'patient', 'date']

    def custom_date_filter(self, queryset, name, value):
        return queryset.filter(date_start__lte=value).filter(**{f'exercise__period__{value.weekday()}': 1})
