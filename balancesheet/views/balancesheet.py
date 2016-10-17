import json
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Sum
from ..models import Difference, BsLineItem


class BalanceSheetView(View):
    template_name = 'balancesheet/balancesheet.html'

    def get(self, request, *args, **kwargs):
        # bs_structure = BsLineItem.objects.all().values()
        bs_structure = BsLineItem.objects.annotate(
            subtotal_difference=Sum('difference__difference'),
            subtotal_temporary=Sum('difference__temporary'),
            subtotal_pl_true_up=Sum('difference__pl_true_up'),
            subtotal_pl_movement=Sum('difference__pl_movement')
        ).values()
        differences = Difference.objects.filter(version_id=self.kwargs['version_id']).values()

        return render(request, self.template_name, {
            'line_items': json.dumps(list(bs_structure), cls=DjangoJSONEncoder),
            'differences': json.dumps(list(differences), cls=DjangoJSONEncoder)
        })

    def post(self, request, *args, **kwargs):
        # Create new Difference and return calculated Difference and Line Item
        return JsonResponse({
            'line_item': 'OPEN',
            'difference': 'OPEN'
        })

    def put(self, request, *args, **kwargs):
        # Update Difference and return calculated Difference and Line Item
        return JsonResponse({
            'line_item': 'OPEN',
            'difference': 'OPEN'
        })
