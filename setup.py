from setuptools import setup

setup(
    name='defexpand',
    version='0.1.0',
    description='Generalizes definitions using DBpedia ontology and WordNet',
    author='Pond Premtoon',
    author_email='varot@mit.edu',
    url='https://github.com/infolab-csail/defexpand.git',
    packages=[
        'defexpand'
    ],
    install_requires=[
        'nltk',
        'elasticstart'
    ],
    dependency_links=[
        'git+https://github.com/infolab-csail/elasticstart.git#egg=elasticstart'
    ],
    package_data = {
        'defexpand': ['data/*']
    }
)
