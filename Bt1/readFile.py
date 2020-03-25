import argparse

import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk import word_tokenize,sent_tokenize

arr = []
def open_file(file_name): #add a flag value for to consider making an array or not later on
	f = open(file_name,"r")
	f1 = f.readlines()
	# nltk.download('punkt')
	for x in f1:
		arr.append(sent_tokenize(x))

def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("filename" , help = "this will read some file", type = str)

	args = parser.parse_args()
	if args.filename:
		open_file(args.filename)
		print(arr)

if __name__ == '__main__':
	Main()
