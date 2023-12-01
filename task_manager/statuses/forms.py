from django.forms import ModelForm, CharField
from django.utils.translation import gettext as _
from .models import Status


class StatusForm(ModelForm):

    name = CharField(
        max_length=150, required=True, label=_("Name")
    )

    class Meta:
        model = Status
        fields = ('name',)
