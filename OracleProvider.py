# -*- coding: utf-8 -*-
import os
import cx_Oracle
import pandas as pd
import DataProcessor as df
import numpy as np
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
        if table_name and table_name.strip():
            # table_name is not None AND table_nameg is not empty or blank
            sql = "SELECT COL.table_name, col.column_name, col.data_type, COL.data_length," \
                  "CASE COL.nullable WHEN 'Y' THEN '1' ELSE '0' end as \"nullable\", COL.high_value," \
                  " COL.low_value, COL.data_precision, CASE uc.constraint_type " \
                  "WHEN 'P' THEN '1' ELSE '0' END AS \"PRIMARY_KEY\" FROM user_tab_columns col LEFT JOIN " \
                  "user_cons_columns ucc ON ucc.table_name = col.table_name AND ucc.column_name = col.column_name " \
                  "LEFT JOIN user_constraints uc ON uc.constraint_name = ucc.constraint_name AND uc.constraint_type = 'P' " \
                  "where  COL.TABLE_NAME = '" + table_name + "'"
        else:
            # table_name is None OR table_name is empty or blank
            sql = "SELECT COL.table_name, col.column_name, col.data_type, COL.data_length," \
                  "CASE COL.nullable WHEN 'Y' THEN '1' ELSE '0' end as \"nullable\", COL.high_value," \
                  " COL.low_value, COL.data_precision , CASE uc.constraint_type " \
                  "WHEN 'P' THEN 'yes' ELSE '' END AS \"PRIMARY_KEY\" FROM user_tab_columns col LEFT JOIN " \
                  "user_cons_columns ucc ON ucc.table_name = col.table_name AND ucc.column_name = col.column_name " \
                  "LEFT JOIN user_constraints uc ON uc.constraint_name = ucc.constraint_name AND uc.constraint_type = 'P'"
        result_list = []
        try:
            cursor = self.connect.cursor()
            cursor.execute(sql)
            rs = cursor.fetchall()
            for row in rs:
                # tuple to list
                tem = list(row)
                # convert data type value
                tem[2] = df.proccess_data_type(row[2])
                result_list.append(tem)
            return result_list
        except cx_Oracle.DatabaseError as ex:
            print(ex)
        finally:
            cursor.close()
            self.connect.close()

    def get_data_info(self, table_name):
        col_sql = "SELECT COL.table_name, col.column_name, col.data_type, COL.data_length," \
                  "CASE COL.nullable WHEN 'Y' THEN '1' ELSE '0' end as \"nullable\", COL.high_value," \
                  " COL.low_value, COL.data_precision, CASE uc.constraint_type " \
                  "WHEN 'P' THEN '1' ELSE '0' END AS \"PRIMARY_KEY\" FROM user_tab_columns col LEFT JOIN " \
                  "user_cons_columns ucc ON ucc.table_name = col.table_name AND ucc.column_name = col.column_name " \
                  "LEFT JOIN user_constraints uc ON uc.constraint_name = ucc.constraint_name AND uc.constraint_type = 'P' " \
                  "where  COL.TABLE_NAME = '" + table_name + "'"
        all_sql = "select * from " + table_name
        col_list = []

        data_list = []
        try:
            cursor = self.connect.cursor()
            cursor.execute(col_sql)
            rs = cursor.fetchall()
            for row in rs:
                # tuple to list
                tem = list(row)
                # convert data type value
                tem[2] = df.proccess_data_type(row[2])
                #对每个column进行统计
                col_name = tem[1]
                if tem[2] == 2:
                    data_sql = "SELECT '" + col_name + "' as column_name,round(max("+ col_name +"),2),round(min(" \
                               + col_name +"),2),round(avg("+ col_name +"),2),round(stddev("+ col_name \
                               +"),2),round(variance("+ col_name +"),2) from " + table_name
                else:
                    data_sql = "SELECT '" + col_name + "' as column_name,round(max(vsize(" + col_name + ")),2),round(min(vsize(" \
                               + col_name + ")),2),round(avg(vsize(" + col_name + ")),2),round(stddev(vsize(" + col_name \
                               + ")),2),round(variance(vsize(" + col_name + ")),2) from " + table_name
                cursor.execute(data_sql)
                rs_data = cursor.fetchall()
                list_data = list(rs_data[0])
                data_list.append(list_data)
                col_list.append(tem)
            df_col = pd.DataFrame(data = col_list,columns=['table_name', 'column_name', 'data_type', 'data_length', 'nullable',
                                                 'high_value', 'low_value', 'data_precision', 'primary_key'])
            df_data = pd.DataFrame(data=data_list, columns=['column_name', 'max', 'min', 'avg', 'stddev', 'varience'])
            df_col = df_col.merge(df_data, on='column_name', how='left')
            return df_col
        except cx_Oracle.DatabaseError as ex:
            print(ex)
        finally:
            cursor.close()
            self.connect.close()

def get_connect():
    try:
        #conn = cx_Oracle.connect("sjzx_hxk", "boco#1234", "192.168.15.222:1521/orcl")
        conn = cx_Oracle.connect("ylfw", "123456", "192.168.15.98:1521/orcl")
        return conn
    except cx_Oracle.DatabaseError as ex:
        print(ex)



if __name__ == '__main__':
    connect = get_connect()
    oracle_provider = OracleProvider(connect)
    rs = oracle_provider.get_data_info("TB_LIS_YMJG")