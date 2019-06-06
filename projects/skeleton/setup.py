# try:
# 	from setuptools import setup
# except ImportError:
# 	from distutils.core import setup
# 
# config = {
# 	'description': 'My First Python Project',
# 	'author': 'suzhenyu',
# 	'url': 'URL to get it at.',
# 	'download_url': 'Where to download it.',
# 	'author_email': '983424749@qq.com',
# 	'version': '0.1',
# 	'install_requires': ['nose'],
# 	'packages': ['Name'],
# 	'scripts': [],
# 	'name': 'projectname'
# }
# 
# setup(**config)


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)