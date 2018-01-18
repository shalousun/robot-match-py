YLJGZZJGDM = rs[rs.column_name == 'YLJGZZJGDM']
ZYH = rs[rs.column_name == 'ZYH']
XM = rs[rs.column_name == 'XM']
XB = rs[rs.column_name == 'XB']
JZYSGH = rs[rs.column_name == 'JZYSGH']
JZYSQM = rs[rs.column_name == 'JZYSQM']
ZYYSGH = rs[rs.column_name == 'ZYYSGH']
ZYYSQM = rs[rs.column_name == 'ZYYSQM']
KSDM = rs[rs.column_name == 'KSDM']
BQMC = rs[rs.column_name == 'BQMC']
RYRQSJ = rs[rs.column_name == 'RYRQSJ']
connect = get_connect()
mss_sql = SqlServerProvider(connect)
rs = mss_sql.get_view_fields_info("emr_zyzd")
ZYZD_JBBM = rs[rs.column_name == 'ZYZD_JBBM']
ZYZDMC = rs[rs.column_name == 'ZYZDMC']
tb_zy_rydjb_x = pd.concat([YLJGZZJGDM, ZYH, XM, XB, JZYSGH, JZYSQM, ZYYSGH,
                           ZYYSQM, KSDM, BQMC, ZYZD_JBBM, ZYZDMC, RYRQSJ])
tb_zy_rydjb_x.to_csv("D:/robot-match-py/data1/tb_zy_rydjb_x.csv",index=False)
