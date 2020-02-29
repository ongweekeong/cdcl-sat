from cdcl import solve
from util import *
from io import read_input
from os import listdir

TEST_DIR = "../test/test/"

def main():
	count = 0

	for file in listdir(TEST_DIR):
		count += 1
		F = read_input(TEST_DIR + file)
		result = solve(F)

		if check(F, result, file):
			print(file + " ok")
		else:
			print(file + " FAIL")
			print("F: " + str(F))
			print("Result: " + str(result))

def check(F, result, file):
	if "uuf" in file:
		return not result[0]

	if not result[0]:
		return False
	
	tau = set(result[1])

	for clause in F:
		if set(clause).intersection(tau) == set():
			return False
		
	return True

main()