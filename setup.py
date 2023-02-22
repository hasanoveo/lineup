from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in lineup/__init__.py
from lineup import __version__ as version

setup(
	name="lineup",
	version=version,
	description="Lineup Customization",
	author="Lineup",
	author_email="lineup@example.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
