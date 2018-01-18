YLJGZZJGDM = rs[rs.column_name == "YLJGZZJGDM"]
ZYH = rs[rs.column_name == "ZYH"]
XM = rs[rs.column_name == "XM"]
CY_KSDM = rs[rs.column_name == "KSDM"]
KSMC = rs[rs.column_name == "KSMC"]
RYRQSJ = rs[rs.column_name == "RYRQSJ"]
CYRQSJ = rs[rs.column_name == "CYRQSJ"]
connect = get_connect()
mss_sql = SqlServerProvider(connect)
rs = mss_sql.get_view_fields_info("emr_ryjl")
BQMC = rs[rs.column_name == "BQMC"]
RY_KSDM = rs[rs.column_name == "KSDM"]
tb_zy_zyjzjl_x = pd.concat([YLJGZZJGDM, ZYH, XM, RY_KSDM, BQMC, CY_KSDM, 
                            KSMC, RYRQSJ, CYRQSJ])
tb_zy_zyjzjl_x.to_csv("D:/robot-match-py/data1/tb_zy_zyjzjl_x.csv",index=False)
