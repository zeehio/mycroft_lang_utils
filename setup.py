from setuptools import setup
import os


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


extra_files = package_files('mycroft_lang_utils')

setup(
    name='mycroft_lang_utils',
    version='0.1',
    packages=['test', 'mycroft_lang_utils', 'mycroft_lang_utils.lang'],
    url='',
    license='',
    package_data={'': extra_files},
    include_package_data=True,
    author='jarbasAI',
    author_email='',
    description='language specific parsing and formatting code extracted from mycroft-core'
)
