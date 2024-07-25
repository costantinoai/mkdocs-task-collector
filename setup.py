from setuptools import setup, find_packages

setup(
    name='mkdocs-task-collector',
    version='0.1.1a',
    description='A MkDocs plugin to collect TODO, NOTE, and PLACEHOLDER annotations.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
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
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)

