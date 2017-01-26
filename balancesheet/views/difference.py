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

def difference_create_update(request):
    # Reusable method which updates or creates a Difference.
    # Takes a request as param and returns a Difference-object
    r = json.loads(request.body.decode('utf-8'))

    if "id" in r:
        difference = Difference.objects.get(pk=int(r['id']))
        del r['id']
    else:
        difference = Difference()

    for key, value in r.items():
        if key not in ['comment', 'name', 'bs_line_item_id', 'version_id']:
            setattr(difference, key, parse_decimal(value, locale=LANGUAGE_CODE[:2]))
        else:
            setattr(difference, key, value)

    return difference

def calculate_follow_ups(difference):
    # Calculate  Follow-up-values for a given difference and return multiple values
    line_item = BsLineItem.objects.filter(pk=difference.bs_line_item_id).annotate(
        subtotal_difference=Sum('difference__difference'),
        subtotal_temporary=Sum('difference__temporary'),
        subtotal_pl_true_up=Sum('difference__pl_true_up'),
        subtotal_pl_movement=Sum('difference__pl_movement')
    )

    bs_total = Difference.objects.filter(version_id=difference.version_id).aggregate(Sum('difference'),
                                                                                     Sum('pl_true_up'),
                                                                                     Sum('pl_movement'))

    return line_item, bs_total


class DifferenceView(View):

    def post(self, request, *args, **kwargs):
        # Create new Difference and return calculated Difference, Line Item and totals
        difference = difference_create_update(request)

        try:
            difference.save()

            line_item, bs_total = calculate_follow_ups(difference)

            return JsonResponse({
                'line_item': json.dumps(format_list_decimal2string(line_item)[0], cls=DjangoJSONEncoder),
                'difference': json.dumps(format_dict_decimal2string(difference), cls=DjangoJSONEncoder),
                'totals': json.dumps(format_dict_decimal2string(bs_total), cls=DjangoJSONEncoder)
            })

        except Exception as e:
            return HttpResponseBadRequest(str(e))

    def put(self, request, *args, **kwargs):
        # Update Difference and return calculated Difference, Line Item and totals

        difference = difference_create_update(request)

        try:
            difference.save()

            line_item, bs_total = calculate_follow_ups(difference)

            return JsonResponse({
                'line_item': json.dumps(format_list_decimal2string(line_item)[0], cls=DjangoJSONEncoder),
                'difference': json.dumps(format_dict_decimal2string(difference), cls=DjangoJSONEncoder),
                'totals': json.dumps(format_dict_decimal2string(bs_total), cls=DjangoJSONEncoder)
            })

        except Exception as e:
            return HttpResponseBadRequest(str(e))
        
    def delete(self, request, *args, **kwargs):
        difference = Difference.objects.get(pk=int(kwargs['difference_id']))
        bs_line_item_id = difference.bs_line_item_id
        if difference.deletable:
            try:
                difference.delete()
                line_item = BsLineItem.objects.filter(pk=bs_line_item_id).annotate(
                    subtotal_difference=Sum('difference__difference'),
                    subtotal_temporary=Sum('difference__temporary'),
                    subtotal_pl_true_up=Sum('difference__pl_true_up'),
                    subtotal_pl_movement=Sum('difference__pl_movement')
                )
                return JsonResponse({'line_item': json.dumps(format_list_decimal2string(line_item)[0], cls=DjangoJSONEncoder)})
            except Exception as e:
                return HttpResponseBadRequest(str(e))
        else:
            return HttpResponseBadRequest('Not allowed!')
