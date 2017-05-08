<<<<<<< HEAD
=======
# -*- coding: utf-8 -*-
>>>>>>> 3f7fff04f4efd05b38f89bf2d4a3b89337ccafac
from setuptools import setup, find_packages
from pip.req import parse_requirements
import re, ast

<<<<<<< HEAD
# get version from __version__ variable in frappe/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('frappe/__init__.py', 'rb') as f:
=======
# get version from __version__ variable in erpnext/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('erpnext/__init__.py', 'rb') as f:
>>>>>>> 3f7fff04f4efd05b38f89bf2d4a3b89337ccafac
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

requirements = parse_requirements("requirements.txt", session="")

setup(
<<<<<<< HEAD
	name='frappe',
	version=version,
	description='Metadata driven, full-stack web framework',
	author='Frappe Technologies',
	author_email='info@frappe.io',
=======
	name='erpnext',
	version=version,
	description='Open Source ERP',
	author='Frappe Technologies',
	author_email='info@erpnext.com',
>>>>>>> 3f7fff04f4efd05b38f89bf2d4a3b89337ccafac
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=[str(ir.req) for ir in requirements],
	dependency_links=[str(ir._link) for ir in requirements if ir._link]
)
