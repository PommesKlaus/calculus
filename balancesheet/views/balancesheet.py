import json

from django.shortcuts import render
from django.views import View
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Sum

from ..models import Difference, BsLineItem
from core.models import Version
from core.core_functions import format_list_decimal2string, format_dict_decimal2string


class BalanceSheetView(View):
    template_name = 'balancesheet/balancesheet.html'

    def get(self, request, *args, **kwargs):
        
        v = Version.objects.get(pk=self.kwargs['version_id'])
        version = {
            'id': v.id,
            'year': str(v.year),
            'year_id': v.year_id,
            'py_year': '-' if v.py_version_id is None else str(v.py_version.year),
            'tu_year': '-' if v.tu_version_id is None else str(v.tu_version.year),
            'name': v.name,
            'shortname': v.shortname,
            'py_shortname': '-' if v.py_version_id is None else str(v.py_version.shortname),
            'py_name': '-' if v.py_version_id is None else str(v.py_version.name),
            'tu_shortname': '-' if v.tu_version_id is None else str(v.tu_version.shortname),
            'tu_name': '-' if v.tu_version_id is None else str(v.tu_version.name),
            'closed': v.closed
        }
        
        bs_line_items = BsLineItem.objects.annotate(
            subtotal_difference=Sum('difference__difference'),
            subtotal_temporary=Sum('difference__temporary'),
            subtotal_pl_true_up=Sum('difference__pl_true_up'),
            subtotal_pl_movement=Sum('difference__pl_movement')
        )

        differences = Difference.objects.filter(version_id=self.kwargs['version_id'])

        bs_total = differences.aggregate(Sum('difference'), Sum('pl_true_up'), Sum('pl_movement'))

        return render(request, self.template_name, {
            'line_items': json.dumps(format_list_decimal2string(bs_line_items), cls=DjangoJSONEncoder),
            'differences': json.dumps(format_list_decimal2string(differences), cls=DjangoJSONEncoder),
            'totals': json.dumps(format_dict_decimal2string(bs_total), cls=DjangoJSONEncoder),
            'version': json.dumps(version, cls=DjangoJSONEncoder)
        })
