
from django.shortcuts import render, get_list_or_404
from django.views import View

from core.models import Company 


class CompanyView(View):
    template_name = 'core/company_view.html'

    def get(self, request, *args, **kwargs):

        c = get_list_or_404(Company)
        context = {
            'Companies': c,
            
        }
        return render(request, self.template_name, context)