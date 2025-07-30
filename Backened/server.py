from venv import logger

from fastapi import FastAPI, HTTPException
import Connection  # This is fine
from pydantic import BaseModel
from typing import List
from datetime import datetime,date
import traceback


app = FastAPI()



class Data(BaseModel):
    amount: float
    category: str
    notes: str
class Dat(BaseModel):
    start_date:date
    end_date:date
@app.get('/expenses/{expense_date}', response_model=List[Data])
def get_data(expense_date: date):
    res = Connection.fetch_all_data(expense_date)  # ✅ Use function directly
    return res

@app.post("/expenses/{expense_date}")
def add_update(expense_date: date, expenses: List[Data]):
    try:
        Connection.delete_exp(expense_date)
        for expense in expenses:
            Connection.insert_exp(expense_date, expense.amount, expense.category, expense.notes)
        return {"message": "Expenses updated successfully"}
    except Exception as e:
        print("Exception in POST /expense:", e)
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.post('/analytics')
def get_sum(date_dat:Dat):
    resul=Connection.get_summ(date_dat.start_date,date_dat.end_date)
    if resul is None:
        raise  HTTPException(status_code=500,detail='No data recieve from backened')
    total=sum([val['total'] for val in resul])

    data={}
    for num in resul:
        percentage=(num['total']/total)*100 if total != 0 else 0
        data[num['category']]={
            'total':num['total'],
            'percentage':percentage,
        }

    return data
@app.get('/yearmonth')
def get_by_month():
    resul=Connection.get_month_data()
    return resul