YLJGDM = rs[rs.column_name == "YLJGDM"]
YZMXID = rs[rs.column_name == "YZMXID"]
JZLSH = rs[rs.column_name == "JZLSH"]
XM = rs[rs.column_name == "XM"]
XB = rs[rs.column_name == "XB"]
BQ = rs[rs.column_name == "BQ"]
XDKSBM = rs[rs.column_name == "XDKSBM"]
XDKSMC = rs[rs.column_name == "XDKSMC"]
XDRGH = rs[rs.column_name == "XDRGH"]
XDRXM = rs[rs.column_name == "XDRXM"]
YZXDSJ = rs[rs.column_name == "YZXDSJ"]
ZXRGH = rs[rs.column_name == "ZXRGH"]
ZXRXM = rs[rs.column_name == "ZXRXM"]
YZZXSJ = rs[rs.column_name == "YZZXSJ"]
YZZZSJ = rs[rs.column_name == "YZZZSJ"]
YZSM = rs[rs.column_name == "YZSM"]
YZLB = rs[rs.column_name == "YZLB"]
YYPD = rs[rs.column_name == "YYPD"]
JL = rs[rs.column_name == "JL"]
MCSL = rs[rs.column_name == "MCSL"]
XMDJ = rs[rs.column_name == "XMDJ"]
tb_zy_zyyzmx_y = pd.concat([YLJGDM, YZMXID, JZLSH, XM, XB, BQ, XDKSBM,
                            XDKSMC, XDRGH, XDRXM, YZXDSJ, ZXRGH,
                            ZXRXM, YZZXSJ, YZZZSJ, YZSM, YZLB,
                            YYPD, JL, MCSL, XMDJ])
tb_zy_zyyzmx_y.to_csv("D:/robot-match-py/data1/tb_zy_zyyzmx_y.csv",index=False)
