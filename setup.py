import os

from setuptools import setup

version = '0.3'

long_description = ''

if os.path.exists('README.rst'):
    long_description = open('README.rst').read()

setup(
      name='django-render-partial',
      version=version,
      description='Django render_partial tag allows inserting rendered views into templates',
      long_description=long_description,
      author='utapyngo',
      author_email='ut@pyngo.tom.ru',
      url='https://github.com/utapyngo/django-render-partial',
      packages=['django_render_partial', 'django_render_partial.templatetags'],
      keywords=['django', 'render', 'partial', 'view', 'template', 'tag'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Environment :: Web Environment',
        'Framework :: Django',
      ],
)
