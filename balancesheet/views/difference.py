import json
from decimal import Decimal
from babel.numbers import parse_decimal

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponseBadRequest
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Sum

from ..models import Difference, BsLineItem
from Calculus.settings import LANGUAGE_CODE
from core.core_functions import format_dict_decimal2string, format_list_decimal2string
import pdb


class DifferenceView(View):

    def post(self, request, *args, **kwargs):
        # Create new Difference and return calculated Difference and Line Item
        r = json.loads(request.body.decode('utf-8'))
        difference = Difference()
        for key, value in r.items():
            if key not in ['comment', 'name', 'bs_line_item_id', 'version_id']:
                setattr(difference, key, parse_decimal(value, locale=LANGUAGE_CODE[:2]))
            else:
                setattr(difference, key, value)
        try:
            # pdb.set_trace()
            difference.save()

            line_item = BsLineItem.objects.filter(pk=difference.bs_line_item_id).annotate(
                subtotal_difference=Sum('difference__difference'),
                subtotal_temporary=Sum('difference__temporary'),
                subtotal_pl_true_up=Sum('difference__pl_true_up'),
                subtotal_pl_movement=Sum('difference__pl_movement')
            )
            return JsonResponse({
                'line_item': json.dumps(format_list_decimal2string(line_item)[0], cls=DjangoJSONEncoder),
                'difference': json.dumps(format_dict_decimal2string(difference), cls=DjangoJSONEncoder)
            })

        except Exception as e:
            return HttpResponseBadRequest(str(e))

    def put(self, request, *args, **kwargs):
        # Update Difference and return calculated Difference and Line Item
        r = json.loads(request.body.decode('utf-8'))
        difference = Difference.objects.get(pk=int(r['id']))
        del r['id']
        for key, value in r.items():
            if key not in ['comment']:
                setattr(difference, key, parse_decimal(value, locale=LANGUAGE_CODE[:2]))
            else:
                setattr(difference, key, value)
        try:
            difference.save()

            line_item = BsLineItem.objects.filter(pk=difference.bs_line_item_id).annotate(
                subtotal_difference=Sum('difference__difference'),
                subtotal_temporary=Sum('difference__temporary'),
                subtotal_pl_true_up=Sum('difference__pl_true_up'),
                subtotal_pl_movement=Sum('difference__pl_movement')
            )
            return JsonResponse({
                'line_item': json.dumps(format_list_decimal2string(line_item)[0], cls=DjangoJSONEncoder),
                'difference': json.dumps(format_dict_decimal2string(difference), cls=DjangoJSONEncoder)
            })

        except Exception as e:
            return HttpResponseBadRequest(str(e))
        
    def delete(self, request, *args, **kwargs):
        r = json.loads(request.body.decode('utf-8'))
        difference = Difference.objects.select_related('version').get(pk=int(r['id']))
        field_list = ['difference', 'oci_permanent', 'oci_temporary', 'pl_permanent', 'pl_temporary', 'py_difference', 'py_oci_permanent', 'py_oci_temporary', 'py_pl_permanent', 'py_pl_temporary', 'tu_difference', 'tu_oci_permanent', 'tu_oci_temporary', 'tu_pl_permanent', 'tu_pl_temporary']
        id = difference.id
        
        if all(difference(key) == Decimal(0.00) for key in field_list) and difference.version.closed:
            try:
                difference.delete()
                return JsonResponse({'deleted_difference_id': id})
            except Exception as e:
                return HttpResponseBadRequest(str(e))
        else:
            return HttpResponseBadRequest('Not allowed!')
            