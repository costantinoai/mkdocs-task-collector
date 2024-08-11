import os
from setuptools import setup, find_packages

# Read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mkdocs-task-collector',
    version='0.1.14',  # Incrementing the version number
    description='A MkDocs plugin to collect TODO, NOTE, and PLACEHOLDER annotations.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Andrea Costantino',
    author_email='andreaivancostantino@outlook.it',
    url='https://github.com/costantinoai/mkdocs-task-collector',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'mkdocs>=1.1'
    ],
    entry_points={
        'mkdocs.plugins': [
            'task-collector = mkdocs_plugins.task_collector:TaskCollectorPlugin',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
    python_requires='>=3.6',
    keywords='mkdocs plugin task todo note placeholder',
    project_urls={
        'Bug Reports': 'https://github.com/costantinoai/mkdocs-task-collector/issues',
        'Source': 'https://github.com/costantinoai/mkdocs-task-collector',
    },
)
