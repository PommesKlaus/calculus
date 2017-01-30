import json

from django.shortcuts import render
from django.views import View
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Sum, When, Case, DecimalField

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
            'py_year': 'n/a' if v.py_version_id is None else str(v.py_version.year),
            'tu_year': 'n/a' if v.tu_version_id is None else str(v.tu_version.year),
            'name': v.name,
            'shortname': v.shortname,
            'py_shortname': 'n/a' if v.py_version_id is None else str(v.py_version.shortname),
            'py_name': 'n/a' if v.py_version_id is None else str(v.py_version.name),
            'tu_shortname': 'n/a' if v.tu_version_id is None else str(v.tu_version.shortname),
            'tu_name': 'n/a' if v.tu_version_id is None else str(v.tu_version.name),
            'closed': v.closed
        }

        bs_line_items = BsLineItem.objects.annotate(
            subtotal_difference=Sum(Case(When(difference__version_id=v.id, then='difference__difference'),
                                         default=0.00, output_field=DecimalField(decimal_places=2))),
            subtotal_pl_permanent=Sum(Case(When(difference__version_id=v.id, then='difference__pl_permanent'),
                                           default=0.00, output_field=DecimalField(decimal_places=2))),
            subtotal_oci_permanent=Sum(Case(When(difference__version_id=v.id, then='difference__oci_permanent'),
                                            default=0.00, output_field=DecimalField(decimal_places=2))),
            subtotal_permanent=Sum(Case(When(difference__version_id=v.id, then='difference__permanent'),
                                        default=0.00, output_field=DecimalField(decimal_places=2))),
            subtotal_pl_temporary=Sum(Case(When(difference__version_id=v.id, then='difference__pl_temporary'),
                                           default=0.00, output_field=DecimalField(decimal_places=2))),
            subtotal_oci_temporary=Sum(Case(When(difference__version_id=v.id, then='difference__oci_temporary'),
                                            default=0.00, output_field=DecimalField(decimal_places=2))),
            subtotal_temporary=Sum(Case(When(difference__version_id=v.id, then='difference__temporary'),
                                        default=0.00, output_field=DecimalField(decimal_places=2))),
            subtotal_pl=Sum(Case(When(difference__version_id=v.id, then='difference__pl'),
                                 default=0.00, output_field=DecimalField(decimal_places=2))),
            subtotal_oci=Sum(Case(When(difference__version_id=v.id, then='difference__oci'),
                                  default=0.00, output_field=DecimalField(decimal_places=2))),
            subtotal_pl_true_up=Sum(Case(When(difference__version_id=v.id, then='difference__pl_true_up'),
                                         default=0.00, output_field=DecimalField(decimal_places=2))),
            subtotal_oci_true_up=Sum(Case(When(difference__version_id=v.id, then='difference__oci_true_up'),
                                          default=0.00, output_field=DecimalField(decimal_places=2))),
            subtotal_pl_movement=Sum(Case(When(difference__version_id=v.id, then='difference__pl_movement'),
                                          default=0.00, output_field=DecimalField(decimal_places=2))),
            subtotal_oci_movement=Sum(Case(When(difference__version_id=v.id, then='difference__oci_movement'),
                                           default=0.00, output_field=DecimalField(decimal_places=2))),
        )

        differences = Difference.objects.filter(version_id=self.kwargs['version_id'])

        bs_total = differences.aggregate(
            Sum('difference'),#
            Sum('pl_permanent'),#
            Sum('oci_permanent'),#
            Sum('permanent'),
            Sum('pl_temporary'),#
            Sum('oci_temporary'),#
            Sum('temporary'),
            Sum('pl'),#
            Sum('oci'),#
            Sum('pl_true_up'),#
            Sum('oci_true_up'),#
            Sum('pl_movement'),#
            Sum('oci_movement')#
        )

        return render(request, self.template_name, {
            'line_items': json.dumps(format_list_decimal2string(bs_line_items), cls=DjangoJSONEncoder),
            'differences': json.dumps(format_list_decimal2string(differences), cls=DjangoJSONEncoder),
            'totals': json.dumps(format_dict_decimal2string(bs_total), cls=DjangoJSONEncoder),
            'version': json.dumps(version, cls=DjangoJSONEncoder)
        })
