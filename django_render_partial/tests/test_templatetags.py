from django.http import HttpRequest, HttpResponse
from django.template import Context, Template
from django.test import TestCase, override_settings


def partial_view(request, *args, **kwargs):
    content = Template(
        "{{ result }}"
    ).render(Context(dict(
        result=kwargs['x'] * 2
    )))
    return HttpResponse(content)


class RenderPartialTemplateTagTests(TestCase):
    @override_settings(TEMPLATES=[{'BACKEND': 'django.template.backends.django.DjangoTemplates'}])
    def test_render_partial_tag(self):
        content = Template(
            '{% load render_partial %}'
            '{% render_partial "django_render_partial.tests.test_templatetags.partial_view" x=4 %}'
        ).render(Context(dict(
            request=HttpRequest()
        )))
        self.assertEqual('8', content)
