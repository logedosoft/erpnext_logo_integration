# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in erpnext_logo_entegrasyon/__init__.py
from erpnext_logo_entegrasyon import __version__ as version

setup(
	name='erpnext_logo_entegrasyon',
	version=version,
	description='ERPNext-Logo ERP entegrasyonu',
	author='Logedosoft Business Solutions',
	author_email='info@logedosoft.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
