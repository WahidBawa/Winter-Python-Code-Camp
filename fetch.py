import xlrd
import os
from dotenv import load_dotenv

load_dotenv()

loc = ("discord.xlsx")
def fetch():
	user_db = dict()
	os.system(os.getenv('COMMAND'))
	wb = xlrd.open_workbook("discord.xlsx")
	sheet = wb.sheet_by_index(1)
	for i in range(sheet.nrows - 1, 0, -1):
		if sheet.cell_value(i, sheet.ncols - 1) not in user_db:
			user_db[sheet.cell_value(i, sheet.ncols - 1)] = sheet.cell_value(i, sheet.ncols - 2)

	return user_db

user_db = fetch()
def verify_user(new_user_id):
	global user_db
	if new_user_id in user_db:
		return (True, user_db[new_user_id])
	user_db = fetch()
	return (True, user_db[new_user_id]) if new_user_id in user_db else (False, "")


def check_user_name(discord_tag):
	if str(discord_tag) in user_db.keys():
		return user_db[discord_tag]

grades = {}
def download_grades():
	global grades
	os.system(os.getenv('FETCH_MARKS'))
	wb = xlrd.open_workbook("grades.xlsx")
	sheet = wb.sheet_by_index(0)
	for i in range(1, sheet.nrows):
		grades[sheet.cell_value(i, 3)] = []
		for j in range(4, sheet.ncols):
			grades[sheet.cell_value(i, 3)].append(sheet.cell_value(i, j))

download_grades()