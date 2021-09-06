import django_tables2 as tables
from .models import Record


class RecordsTable(tables.Table):
    class Meta:
        model = Record
        template_name = "django_tables2/semantic.html"
        fields = ("id", "userName", "userEmail", "datetime")