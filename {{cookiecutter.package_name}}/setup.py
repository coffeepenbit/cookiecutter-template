from setuptools import setup, find_packages
import os

CLASSIFIERS = []
INSTALL_REQUIRES = []


def get_about(here):
    about = {}
    about_info_path = os.path.join(here, 'src', '{{cookiecutter.package_name}}', '__version__.py')
    with open(about_info_path,'r', encoding='utf-8' ) as f:
        exec(f.read(), about)

    return about

def get_long_description(here):
    with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

    return long_description


here = os.path.abspath(os.path.dirname(__file__))
about = get_about(here)

setup(
    author_email=about['__author_email__'],
    author=about['__author__'],
    classifiers=CLASSIFIERS,
    description=about['__description__'],
    install_requires=INSTALL_REQUIRES,
    long_description_content_type='text/markdown',
    long_description=get_long_description(here),
    name=about['__title__'],
    package_dir={'': 'src'},
    packages=find_packages('src'),    
    python_requires='>=3.6',
    url=about['__url__'],
    version=about['__version__']
)