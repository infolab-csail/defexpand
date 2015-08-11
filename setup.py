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
        'mwparserfromhell',
        'dewiki',
        'unidecode'
    ],
    package_data = {
        'defexpand': ['data/*']
    }
)
