import os
import sys
import re
from textblob import TextBlob

def _getlowercase(x):
	return x.lower()

def _getuppercase(x):
	return	x.upper()

def _getcharcount(x):
	text =(re.sub(r'[\w]+',"",x))
	count =len(text)
	return count

def _getnoncharcount(x):
	text =(re.sub(r'[^\w]+',"",x))
	count =len(text)
	return count

def removeextraspace(x):
	text ="	".join(x.split())
	return	text


def gettokenizedtext(x):
	text = TextBlob(x).words
	return text

