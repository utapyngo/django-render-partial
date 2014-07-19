from django.shortcuts import render
from django.views.generic.base import TemplateView


def partial_test(request):
    return render(request, 'partial_test.html')


class PartialView(TemplateView):
    template_name = 'partial_view.html'

    def get_context_data(self, **kwargs):
        result = kwargs['arg1'] + kwargs['arg2']
        kwargs['result'] = result
        return super(PartialView, self).get_context_data(**kwargs)


def partial_view(request, *args, **kwargs):
    result = kwargs['arg1'] + kwargs['arg2']
    kwargs['result'] = result
    return render(request, 'partial_view.html', kwargs)
