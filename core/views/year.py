
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.views import View
from django.http import HttpResponseForbidden

from core.models import Year
import pdb

class YearListView(View):
    template_name = 'core/year_list.html'

    def get(self, request, *args, **kwargs):

        y = Year.objects.filter(company_id=kwargs['company_id'])
        context = {
            'Years': y,
            'company_id': kwargs['company_id']
        }
        return render(request, self.template_name, context)
        
    def post(self, request, *args, **kwargs):
        y = Year.objects.filter(company_id=kwargs['company_id']).reverse()[0]
        return


class YearDetailView(View):
    template_name = 'core/year_detail.html'

    def delete(self, request, *args, **kwargs):
        y = get_object_or_404(Year, pk=kwargs['year_id'])

        if y.version_set.count() == 0:
            y.delete()
            pdb.set_trace()
            return redirect('core:year_index', company_id=kwargs['company_id'])

        else:
            return HttpResponseForbidden('Jahr kann nicht gelöscht werden, da es Versionen beinhaltet.')
