# -*- coding: utf-8 -*-
#  数据类型转换，将oracle，mysql,sqlserver的类型统一转为为三种类型
def proccess_data_type(type):
    type = type.upper()
    switcher = {
        "CHAR": 1,
        "NCHAR": 1,
        "VARCHAR": 1,
        "VARCHAR2": 1,
        "NVARCHAR": 1,
        "NVARCHAR2": 1,
        "LONGTEXT": 1,
        "TINYTEXT": 1,

        "NUMBER": 2,
        "NUMERIC": 2,
        "INT": 2,
        "SMALLINT": 2,
        "INTEGER": 2,
        "DECIMAL": 2,
        "FLOAT": 2,
        "DOUBLE PRECISION": 2,
        "BIGINT": 2,
        "TINYINT": 2,
        "DOUBLE": 2,

        "DATE": 3,
        "DATETIME": 3,
        "TIMESTAMP(6)": 3,
        "TIMESTAMP": 3
    }
    return switcher.get(type)

