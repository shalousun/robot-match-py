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
        sql = ""
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
        conn = cx_Oracle.connect("username", "password", "localhost" + ':' + 1521 + '/' + "edu")
        return conn
    except (cx_Oracle.DatabaseError) as ex:
        print(ex)


if __name__ == '__main__':
    print("main")
    connect = get_connect()
    oracle_provider = OracleProvider(connect)
    oracle_provider.get_fields_info("hello")
