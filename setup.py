#!/usr/bin/env python

if __name__ == "__main__":
    from setuptools import setup, find_packages
    setup(
        name='Costumer API',
        version='0.1.0',
        packages=find_packages(include=['app', 'app.*']),
        install_requires=[
            'asgiref==3.4.1',
            'certifi==2021.5.30',
            'charset-normalizer==2.0.4',
            'coreapi==2.3.3',
            'coreschema==0.0.4',
            'dill==0.3.4',
            'Django==3.2.7',
            'djangorestframework==3.12.4',
            'drf-yasg==1.20.0',
            'idna==3.2',
            'inflection==0.5.1',
            'itypes==1.2.0',
            'Jinja2==3.0.1',
            'MarkupSafe==2.0.1',
            'numpy==1.21.2',
            'packaging==21.0',
            'pandas==1.3.2',
            'pyparsing==2.4.7',
            'python-dateutil==2.8.2',
            'pytz==2021.1',
            'requests==2.26.0',
            'ruamel.yaml==0.17.16',
            'ruamel.yaml.clib==0.2.6',
            'six==1.16.0',
            'sqlparse==0.4.1',
            'uritemplate==3.0.1',
            'urllib3==1.26.6'
        ]
    )
