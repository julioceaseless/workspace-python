#!/usr/bin/env python3
"""
Display birthday message and special message for leapies
"""
from datetime import datetime


def check_leap(year):
	""" check if birth year is leap """
	return ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)

def is_feb_29(month, day):
	""" check if it is feb 29"""
	return (month == datetime.now().month == 2)\
		and (day == datetime.now().day == 29)

def is_birthday(month, day):
	""" check month and day"""
	return (month == datetime.now().month\
		and day == datetime.now().day)
def main():
	""" main function """
	is_leap_year = check_leap(datetime.now().year)
	
	# get birth date from user
	birth_date = input("Enter date of birth (format: DD-MM-YY): ")
	date_month_year = birth_date.split("-")

	b_day, b_month, b_year = date_month_year 

	is_leapie = check_leap(int(b_year)) and is_feb_29(int(b_month), int(b_day))
	
	#  message for leapie
	if (is_leapie and is_leap_year):
		print("Happy Birthday Leapie")
	elif is_birthday(int(b_month), int(b_day)):
		print("Happy birthday")
	else:
		print("Wait for your birthday!")
if __name__ == "__main__":
	main()
