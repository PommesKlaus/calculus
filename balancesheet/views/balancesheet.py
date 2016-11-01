import json

from django.shortcuts import render
from django.views import View
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Sum

from ..models import Difference, BsLineItem
from core.core_functions import format_list_decimal2string


class BalanceSheetView(View):
    template_name = 'balancesheet/balancesheet.html'

    def get(self, request, *args, **kwargs):
        bs_line_items = BsLineItem.objects.annotate(
            subtotal_difference=Sum('difference__difference'),
            subtotal_temporary=Sum('difference__temporary'),
            subtotal_pl_true_up=Sum('difference__pl_true_up'),
            subtotal_pl_movement=Sum('difference__pl_movement')
        )

        differences = Difference.objects.filter(version_id=self.kwargs['version_id'])

        return render(request, self.template_name, {
            'line_items': json.dumps(format_list_decimal2string(bs_line_items), cls=DjangoJSONEncoder),
            'differences': json.dumps(format_list_decimal2string(differences), cls=DjangoJSONEncoder),
            'version': self.kwargs['version_id']
        })
