from Backened import Connection
import pytest
import datetime

def test_connection_result():
    conn = Connection
    conn.insert_exp('9999-10-02', 60, 'test', 'it is a uni test to check data if it work alright')

    result = conn.fetch_all_data('9999-10-02')

    assert result[-1]['amount'] == 60.0
    assert result[-1]['category'] == 'test'
    assert result[-1]['expense_date'] == datetime.date(9999, 10, 2)
    assert result[-1]['notes'] == 'it is a uni test to check data if it work alright'


    conn.delete_exp('9999-10-02')

    result = conn.fetch_all_data('9999-10-02')
    assert len(result) ==  0

    result=conn.get_summ('2000-08-01','2000-09-01')
    assert len(result) == 0

    result=conn.get_month_data()
    assert len(result) != 0