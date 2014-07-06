try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'description',
        'author': 'Abelardo Vieira Mota',
        'url': 'http://abevieiramota.com',
        'download_url': 'download_url',
        'author_email': 'abevieiramota@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['collapsible_tree'],
        'scripts': ['bin/papoca.py'],
        'name': 'NAME'
}

setup(**config)
