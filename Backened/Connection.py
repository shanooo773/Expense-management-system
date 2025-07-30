import mysql.connector
from contextlib import contextmanager
from datetime import date
from logging import Formatter, getLogger, DEBUG, FileHandler, info

logger= getLogger('Connection')
logger.setLevel(DEBUG)

fil= FileHandler('logger.log')
form= Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fil.setFormatter(form)

logger.addHandler(fil)

@contextmanager
def get_cursor(commit=False):
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='1122',
        database='expense_manager'
    )
    cursor=conn.cursor(dictionary=True)

    yield cursor

    if commit:
        conn.commit()
    cursor.close()
    conn.close()

def fetch_all_data(expense_date):
    logger.info(f'Fetch all data for {expense_date}')
    with get_cursor() as cursor:
        cursor.execute('SELECT * FROM expenses WHERE expense_date = %s',(expense_date,))
        res=cursor.fetchall()
        return res

def delete_exp(expense_date):
    logger.info(f'Delete data by date {expense_date}')
    with get_cursor(commit=True) as cursor:
        cursor.execute('DELETE FROM expenses WHERE expense_date = %s',(expense_date,))

def insert_exp(dates,amount,category,notes):
    logger.info(f'Insert data {dates} -- {amount} -- {category} -- {notes}')
    if isinstance(dates, date):
        dates = dates.isoformat()
    with get_cursor(commit=True) as cursor:
        cursor.execute('INSERT INTO expenses (expense_date,amount,category,notes) VALUES (%s, %s, %s, %s)', (dates,amount,category,notes))

def get_summ(start_date,end_date):
    logger.info(f'Get summary from {start_date} to {end_date}')
    with get_cursor() as cursor:
        cursor.execute('SELECT category,sum(amount) as total FROM expenses WHERE expense_date BETWEEN %s and %s GROUP BY category',(start_date,end_date))
        answer=cursor.fetchall()
        return answer

def get_month_data():
    logger.info('Get data analytics by month')
    with get_cursor() as cursor:
        cursor.execute('SELECT DATE_FORMAT(expense_date, %s) AS month,SUM(amount) AS total_expense FROM expenses GROUP BY DATE_FORMAT(expense_date, %s) ORDER BY month',('%M %Y','%M %Y'))
        answer=cursor.fetchall()
        return answer
# insert_exp('2024-09-01','60','Food',' for enjoy')
# delete_exp('2024-09-01')
#
# ans=fetch_all_data('2024-09-01')
if __name__ == "__main__":
    expenses = get_month_data()
    print(expenses)
    # # delete_expenses_for_date("2024-08-25")
    # summary = get_summ("2024-08-01", "2024-08-05")
    # for record in summary:
    #     print(record)