from django import forms
from django_filters import BooleanFilter, FilterSet
from django.utils.translation import gettext_lazy as _
from .models import Task


class TaskFilter(FilterSet):
    own_tasks = BooleanFilter(
        field_name='author',
        label=_('Only own tasks'),
        method='filtered_own_tasks',
        widget=forms.CheckboxInput,
    )

    class Meta:
        model = Task
        fields = ['status', 'executor']

    def filtered_own_tasks(self, queryset, name, value):
        if value:
            user = self.request.user.pk
            return queryset.filter(author=user)
        return queryset
