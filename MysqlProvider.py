# -*- coding: utf-8 -*-
import pymysql
import pymysql.cursors
import pandas as pd


class MysqlProvider:
    def __init__(self, connect):
        self.connect = connect

    def get_tables(self):
        cursor = self.connect.cursor()
        sql = "show table status"
        list_rs = []
        try:
            cursor.execute(sql)
            rs = cursor.fetchall()
            for rec in rs:
                list_rs.append(rec[0])
        except Exception as e:
            print(e)
        finally:
            self.connect.close
        return list_rs

    def get_fields_info(self, table_name):
        cursor = self.connect.cursor()
        sql = "SHOW FULL COLUMNS FROM boco_dady." + table_name

        result_list = []
        try:
            cursor.execute(sql)
            # print(cursor.description)
            rs = cursor.fetchall()
            print(rs)
            rs_dataframe = pd.DataFrame(list(rs), columns=['field', 'type', 'collation', 'null', 'key', 'default',
                                                           'extra', 'privileges', 'comment'])
            print (rs_dataframe)
            for rec in rs:
                print(rec[0])

        except Exception as e:
            print(e)
        finally:
            self.connect.close()
        return result_list

    def get_list_result(self, sql):
        cursor = self.connect.cursor()
        result_list = []
        try:
            cursor.execute(sql)
            columns = cursor.description
            for value in cursor.fetchall():
                tmp = {}
                for (index, column) in enumerate(value):
                    tmp[columns[index][0]] = column
                    result_list.append(tmp)
        except Exception as e:
            print(e)
        finally:
            self.connect.close()
        return result_list


def get_connect():
    # 注意是utf8不是utf-8
    connection = pymysql.connect(host='192.168.15.222', user='root', password='Boco#1234', db='boco_dady', port=3306,
                                 charset='utf8')
    return connection


if __name__ == "__main__":
    connect = get_connect()
    mysql_provider = MysqlProvider(connect)
    mysql_provider.get_fields_info('base_info')
