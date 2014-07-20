from unittest import TestCase
from django.http import HttpRequest, HttpResponse
from django.template import Template, Context


def partial_view(request, *args, **kwargs):
    content = Template(
        "{{ result }}"
    ).render(Context(dict(
        result=kwargs['x'] * 2
    )))
    return HttpResponse(content)


class RenderPartialTemplateTagTests(TestCase):
    def test_render_partial_tag(self):
        content = Template(
            '{% load render_partial %}'
            '{% render_partial "tests.test_templatetags.partial_view" x=4 %}'
        ).render(Context(dict(
            request=HttpRequest()
        )))
        self.assertEqual('8', content)
