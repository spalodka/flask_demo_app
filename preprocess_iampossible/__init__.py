from preprocess_iampossible import utils

__version__= '0.0.1'

def getlowercase(x):
	return utils._getlowercase(x)

def getuppercase(x):
	return utils._getuppercase(x)

def getcharcount(x):
	return utils._getcharcount(x)

def getnoncharcount(x):
	return utils._getnoncharcount(x)

def removeextraspace(x):
	return	utils.removeextraspace(x)


def gettokenizedtext(x):
	return utils.gettokenizedtext(x)

