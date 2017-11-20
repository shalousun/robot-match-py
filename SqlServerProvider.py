# -*- coding: utf-8 -*-
import os

os.environ['NLS_LANG'] = '.AL32UTF8'
import pymssql
import pandas as pd


class SqlServerProvider:
    def __init__(self, connect):
        self.connect = connect

    def get_tables(self):
        sql = ""
        try:
            cursor = self.connect.cursor()
            cursor.execute(sql)
            rs = cursor.fetchall()
            return rs
        except Exception as e:
            print(e)

    def get_fields_info(self, table_name):

        if table_name and table_name.strip():
            # table_name is not None AND table_nameg is not empty or blank
            sql = "SELECT C.COLUMN_NAME, C.table_name, C.DATA_TYPE, C.CHARACTER_MAXIMUM_LENGTH, C.NUMERIC_PRECISION ," \
                  " C.NUMERIC_SCALE, C.IS_NULLABLE , CASE  WHEN Z.CONSTRAINT_NAME IS NULL THEN 0 ELSE 1 END AS IsPartOfPrimaryKey " \
                  "FROM INFORMATION_SCHEMA.COLUMNS C OUTER APPLY ( SELECT CCU.CONSTRAINT_NAME FROM " \
                  "INFORMATION_SCHEMA.TABLE_CONSTRAINTS TC JOIN INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE CCU ON " \
                  "CCU.CONSTRAINT_NAME = TC.CONSTRAINT_NAME WHERE TC.TABLE_SCHEMA = C.TABLE_SCHEMA " \
                  "AND TC.TABLE_NAME = C.TABLE_NAME AND TC.CONSTRAINT_TYPE = 'PRIMARY KEY' " \
                  "AND CCU.COLUMN_NAME = C.COLUMN_NAME ) Z WHERE C.TABLE_NAME = '" + table_name + " '"
        else:
            # table_name is None OR table_name is empty or blank
            sql = "SELECT C.COLUMN_NAME, C.table_name, C.DATA_TYPE, C.CHARACTER_MAXIMUM_LENGTH, C.NUMERIC_PRECISION ," \
                  " C.NUMERIC_SCALE, C.IS_NULLABLE , CASE  WHEN Z.CONSTRAINT_NAME IS NULL THEN 0 ELSE 1 END AS IsPartOfPrimaryKey " \
                  "FROM INFORMATION_SCHEMA.COLUMNS C OUTER APPLY ( SELECT CCU.CONSTRAINT_NAME FROM " \
                  "INFORMATION_SCHEMA.TABLE_CONSTRAINTS TC JOIN INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE CCU ON " \
                  "CCU.CONSTRAINT_NAME = TC.CONSTRAINT_NAME WHERE TC.TABLE_SCHEMA = C.TABLE_SCHEMA " \
                  "AND TC.TABLE_NAME = C.TABLE_NAME AND TC.CONSTRAINT_TYPE = 'PRIMARY KEY' " \
                  "AND CCU.COLUMN_NAME = C.COLUMN_NAME ) Z "
        try:
            cursor = self.connect.cursor()
            cursor.execute(sql)
            rs = cursor.fetchall()
            print(rs)
            return rs
        except Exception as ex:
            print(ex)
        finally:
            self.connect.close()


def get_connect():
    try:
        conn = pymssql.connect(host='192.168.15.99',
                               user='sa',
                               password='boco#1234',
                               database='lis6')
        return conn
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    connect = get_connect()
    mss_sql = SqlServerProvider(connect)
    mss_sql.get_fields_info("bact_biochem")
