from setuptools import setup, find_packages

setup(
    name = "django-template-tags",
    url = 'https://github.com/citylive/django-template-tags',
    license = 'BSD',
    description = "Some general, useful template tags.",
    long_description = open('README','r').read(),
    author = 'Jonathan Slenders, City Live nv',
    packages = find_packages('src'),
    package_data = {'django_template_tags': ['static/css/*.css', ],},
    include_package_data=True,
    package_dir = {'': 'src'},
    classifiers = [
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)

