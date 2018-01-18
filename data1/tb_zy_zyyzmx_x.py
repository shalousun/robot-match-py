YLJGZZJGDM = rs[rs.column_name == "YLJGZZJGDM"]
YZBH = rs[rs.column_name == "YZBH"]
ZYH = rs[rs.column_name == "ZYH"]
XM = rs[rs.column_name == "XM"]
XB = rs[rs.column_name == "XB"]
BQMC = rs[rs.column_name == "BQMC"]
KSDM = rs[rs.column_name == "KSDM"]
KSMC = rs[rs.column_name == "KSMC"]
YZKLZGH = rs[rs.column_name == "YZKLZGH"]
YZKLZQM = rs[rs.column_name == "YZKLZQM"]
YZKLRQSJ = rs[rs.column_name == "YZKLRQSJ"]
ZXYZZGH = rs[rs.column_name == "ZXYZZGH"]
ZXYZZQM = rs[rs.column_name == "ZXYZZQM"]
YZZXRQSJ = rs[rs.column_name == "YZZXRQSJ"]
YZTZRQSJ = rs[rs.column_name == "YZTZRQSJ"]
connect = get_connect()
mss_sql = SqlServerProvider(connect)
rs = mss_sql.get_view_fields_info("emr_zyzd")
ZDLX = rs[rs.column_name == "ZDLX"]
connect = get_connect()
mss_sql = SqlServerProvider(connect)
rs = mss_sql.get_view_fields_info("z_yz")
yzlr = rs[rs.column_name == "yzlr"]
pcms = rs[rs.column_name == "pcms"]
jl = rs[rs.column_name == "jl"]
dwsl = rs[rs.column_name == "dwsl"]
dj = rs[rs.column_name == "dj"]
tb_zy_zyyzmx_x = pd.concat([YLJGZZJGDM, YZBH, ZYH, XM, XB, BQMC, KSDM,
                            KSMC, YZKLZGH, YZKLZQM, YZKLRQSJ, ZXYZZGH,
                            ZXYZZQM, YZZXRQSJ, YZTZRQSJ, yzlr, ZDLX,
                            pcms, jl, dwsl, dj])
tb_zy_zyyzmx_x.to_csv("D:/robot-match-py/data1/tb_zy_zyyzmx_x.csv",index=False)
