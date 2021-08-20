import setuptools

with open("README.MD",'r') as file:
		long_description = file.read()

setuptools.setup(
	name='preprocess_iampossible', #this should be unique 
	version = '0.0.1',
	author = 'Sandip Palodkar',
	#author_email ='sandippalodkar7@gmail.com',
	description = 'This is preprocessing package',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifier = [
    'programming Language :: Python :: 3',
    'Licence ::OSI Approved :: MIT Licence',
    "Operating System :: OS Independent"
	],
	python_requires = '>=3.5'
)