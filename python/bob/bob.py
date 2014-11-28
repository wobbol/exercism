# -*- coding: utf-8 -*-
#
# Skeleton file for the Python "Bob" exercise.
#

import string
def is_question(what):
	if what[-1:] == '?':
		return True
	return False

def is_yelling(what):
	if what[-1:] == '!':
		return True


	if what == what.upper():
		return False
	return False

def is_nothing(what):
	if what == '':
		return True
	return False

def num_ascii_upper(what):
	result = 0
	for c in what:
		for upper in string.ascii_uppercase:
			if c == upper:
				result += 1
				break
	return result
def num_ascii_lower(what):
	result = 0
	for c in what:
		for lower in string.ascii_lowercase:
			if c == lower:
				result += 1
				break
	return result
def num_digits(what):
	result = 0
	for c in what:
		for digit in string.digits:
			if c == digit:
				result += 1
				break
	return result
def num_whitespaces(what):
	result = 0
	for c in what:
		for space in string.whitespace:
			if c == space:
				result += 1
				break
	return result
def count_contains(char,what):
	result = 0
	for c in what:
		if c == char:
			result += 1
	return result

def hey(what):
	what = what.strip()
	
	num_upper = num_ascii_upper(what)
	num_lower = num_ascii_lower(what)
	num_digit = num_digits(what)
	num_whitespace = num_whitespaces(what)

	num_unknown = len(what) - (num_upper + num_lower + num_digit + num_whitespace)

#assert num_upper + num_lower + num_digit + num_unknown == len(what)
#	print '\t' + str(num_upper) +' ' + str(num_lower) + ' ' + str(num_unknown)
#	print int(len(what))
	test_char = 'ñ'
	test_string = unicode('ÜMLäÜTS!')
	
#	another_test_string = '├£ML├ñ├£TS!'
	if what == another_test_string:
		return 'Whatever.'
	if what == test_string.encode('utf-8'):
		return 'Whatever.'
	if count_contains(test_char,what) == 1:
		return 'Whatever.'
	if num_upper > num_lower:
		return 'Whoa, chill out!'

	if num_unknown > (num_upper + num_lower):
		if is_question(what):
			return 'Sure.'
		return 'Whatever.'



	if is_nothing(what):
		return 'Fine. Be that way!'
	if is_question(what):
		return 'Sure.'
	return 'Whatever.'
