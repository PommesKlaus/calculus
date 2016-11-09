__author__ = 'CF'
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.http import HttpResponseForbidden, HttpResponse

import datetime, dateutil.parser, calendar, pdb

from core.models import Company, Year


class YearListView(View):
    template_name = 'core/year_list.html'

    def get(self, request, *args, **kwargs):

        y = Year.objects.filter(company_id=kwargs['company_id'])
        n = y.last().end_date + datetime.timedelta(days=1)
    
        if calendar.isleap(y.last().end_date.year+1):
            ye = y.last().end_date + datetime.timedelta(days=366)
        else:
            ye = y.last().end_date + datetime.timedelta(days=365)
    
        # Feststellen, ob Jahr gelöscht werden kann
        for elem in y:
            if elem.year_set.count() > 0 or elem.version_set.count() > 0:
                elem.deletable = False
            else:
                elem.deletable = True
            #pdb.set_trace()


        context = {
            'Company_id': kwargs['company_id'],
            'Years':y,
            'Yearend':ye,
            'Nextyear':n            }
            
        return render(request, self.template_name, context)
        
        
    def post(self, request, *args, **kwargs):
        sd = dateutil.parser.parse(request.POST.get('inputFromDate')).date()
        ed = dateutil.parser.parse(request.POST.get('inputToDate')).date()
        pyid = request.POST.get('prior_year_id')
        ny = Year(start_date=sd, end_date=ed, prior_year_id=pyid, company_id=kwargs['company_id'])
        if sd <= ed:
            ny.save()
            messages.success(request, 'Neues Jahr hinzugefügt')
        else:
            messages.error(request, 'Das "Bis"-Datum muss zeitlich nach dem "Von"-Datum liegen.')
        
        y = Year.objects.filter(company_id=kwargs['company_id'])
        n = y.last().end_date + datetime.timedelta(days=1)
    
        if calendar.isleap(y.last().end_date.year+1):
            ye = y.last().end_date + datetime.timedelta(days=366)
        else:
            ye = y.last().end_date + datetime.timedelta(days=365)
    
        # Feststellen, ob Jahr gelöscht werden kann
        for elem in y:
            if elem.year_set.count() > 0 or elem.version_set.count() > 0:
                elem.deletable = False
            else:
                elem.deletable = True
    
        context = {
            'Company_id': kwargs['company_id'],
            'Years':y,
            'Yearend':ye,
            'Nextyear':n
            }
    
        return render(request, self.template_name, context)


class YearDetailView(View):

    def delete(self, request, *args, **kwargs):
        y = get_object_or_404(Year, id=kwargs['year_id'])
        if y.year_set.count() > 0 or y.version_set.count() > 0:
            return HttpResponseForbidden
        else:
            y.delete()
            return HttpResponse(status=200)
