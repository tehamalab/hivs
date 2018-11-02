# hivs_dash/views.py

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'hivs_dash/index.html'


@method_decorator(login_required, name='dispatch')
class ReportsView(TemplateView):
    template_name = 'hivs_dash/reports.html'
