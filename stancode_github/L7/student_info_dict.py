"""
File: student_info_dict.py
------------------------------
This program puts data in a text file 
into a nested data structure where key
is the name of each student, and the value
is the dict that stores the student info
"""


# The file name of our target text file
FILE = 'students_info.txt'


def main():
	all_d = {}
	######################
	with open(FILE, 'r') as f:
		for line in f:
			tokens = line.split()
			all_d[tokens[0]] = {'Age': int(tokens[1]), 'Email': tokens[2], 'Food': tokens[3:]}
	######################
	print_out_d(all_d)


def print_out_d(d):
	"""
	: param d: (dict) key of type str is the name of student
				value of type dict is the info of the student
	---------------------------------------------------------------
	This function prints out a nested data structure on console
	"""
	for key, value in d.items():
		print(key, value)
		print('-'*20)



if __name__ == '__main__':
	main()


