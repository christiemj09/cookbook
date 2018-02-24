"""
Install cookbook.
"""

def main():
	try:
		from setuptools import setup
	except ImportError:
		from distutils.core import setup

	config = {
		'description': 'Save script invocations in a database and allow them to be run from queries',
		'author': 'Matt Christie',
		'download_url': 'https://github.com/christiemj09/cookbook.git',
		'author_email': 'christiemj09@gmail.com',
		'version': '0.1',
		'install_requires': [],
		'packages': ['cookbook'],
		'scripts': [],
		'entry_points': {
		    'console_scripts': []
		},
		'name': 'cookbook'
	}

	setup(**config)	

if __name__ == '__main__':
	main()
