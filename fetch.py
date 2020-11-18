import xlrd
import os
from dotenv import load_dotenv

load_dotenv()

loc = ("discord.xlsx")
def fetch():
	user_db = dict()
	os.system(os.getenv('COMMAND'))
	wb = xlrd.open_workbook(loc)
	sheet = wb.sheet_by_index(1)
	for i in range(sheet.nrows - 1, 0, -1):
		if sheet.cell_value(i, sheet.ncols - 1) not in user_db:
			user_db[sheet.cell_value(i, sheet.ncols - 1)] = sheet.cell_value(i, sheet.ncols - 2)

	return user_db

user_db = fetch()
print(user_db)
def verify_user(new_user_id):
	global user_db
	print(user_db)
	if new_user_id in user_db:
		return (True, user_db[new_user_id])
	user_db = fetch()
	print(user_db)
	return (True, user_db[new_user_id]) if new_user_id in user_db else (False, "")
