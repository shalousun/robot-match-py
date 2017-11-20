# -*- coding: utf-8 -*-
import os
import cx_Oracle
import pandas as pd
os.environ['NLS_LANG'] = '.AL32UTF8'


class OracleProvider:
    def __init__(self, connection):
        self.connect = connection

    def get_tables(self):
        sql = ""
        try:
            cursor = self.connect.cursor()
            cursor.execute(sql)
            rs = cursor.fetchall()
            return rs
        except cx_Oracle.DatabaseError as ex:
            print(ex)

    def get_fields_info(self, table_name):
        if table_name.strip() == "":
            sql = "select distinct column_name, data_type,data_length,nullable,high_value,low_value, data_precision" \
                  " from user_tab_cols"
        else:
            sql = "select distinct column_name,data_type, data_length,nullable,high_value, low_value,data_precision " \
                  "from user_tab_cols where table_name ="+table_name
        try:
            cursor = self.connect.cursor()
            cursor.execute(sql)
            rs = cursor.fetchall()
            return rs
        except cx_Oracle.DatabaseError as ex:
            print(ex)
        finally:
            cursor.close()
            self.connect.close()


def get_connect():
    try:
        conn = cx_Oracle.connect("sjzx_jyk_hd", "boco#1234", "192.168.15.222:1521/orcl")
        return conn
    except cx_Oracle.DatabaseError as ex:
        print(ex)


if __name__ == '__main__':
    print("main")
    connect = get_connect()
    oracle_provider = OracleProvider(connect)
    rs = oracle_provider.get_fields_info("")
    rs_dataframe = pd.DataFrame(list(rs), columns=['column_name', 'data_type', 'data_length', 'nullable',
                                                   'high_value', 'low_value', 'data_precision'])
    print(rs_dataframe)
