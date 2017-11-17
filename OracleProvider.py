# -*- coding: utf-8 -*-
import cx_Oracle

class OracleProvider:
    def __init__(self, connection):
        self.connect = connection

    def get_tables(self):
        sql = ""
        try:
            cursor = self.connect.cursor()
            row = cursor.excute(sql)
            return row
        except (cx_Oracle.DatabaseError) as ex:
            print(ex)
        finally:
            self.connect.close()

    def get_fields_info(self, table_name):
        if table_name.trip() == "":
            sql = "select distinct column_name，data_type,data_length,nullable,high_value,low_value,data_precision from user_tab_cols"
        else:
            sql = "select distinct column_name，data_type,data_length,nullable,high_value,low_value,data_precision from user_tab_cols where table_name ="+table_name
        try:
            cursor = self.connect.cursor()
            row = cursor.excute(sql)
            return row
        except (cx_Oracle.DatabaseError) as ex:
            print(ex)
        finally:
            self.connect.close()


def get_connect():
    try:
        conn = cx_Oracle.connect("sjzx_jyk_hd", "boco#1234", "192.168.15.222:1521/orcl")
        return conn
    except (cx_Oracle.DatabaseError) as ex:
        print(ex)


if __name__ == '__main__':
    print("main")
    connect = get_connect()
    oracle_provider = OracleProvider(connect)
    oracle_provider.get_fields_info("hello")
