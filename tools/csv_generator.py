from dbmanager import get_expenses
import csv

def generate_csv(file_path):
    """"""
    expenses= get_expenses()
    if not expenses:
        return 0
    with open(file_path,mode='w',newline='',encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "description", "amount", "date", "category"])
        writer.writeheader()
        writer.writerows(expenses)
    return 1