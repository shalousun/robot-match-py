h_cfh = rs[rs.column_name == 'h_cfh']
m_ghxh = rs[rs.column_name == 'm_ghxh']
h_lxbm = rs[rs.column_name == 'h_lxbm']
ksbm = rs[rs.column_name == 'ksbm']
ysbm = rs[rs.column_name == 'ysbm']
h_cfrq = rs[rs.column_name == 'h_cfrq']
fylb = rs[rs.column_name == 'fylb']
h_cfhj = rs[rs.column_name == 'h_cfhj']
zxks = rs[rs.column_name == 'zxks']
connect = get_connect()
mss_sql = SqlServerProvider(connect)
rs = mss_sql.get_view_fields_info("RS_ResidentInfo")
JKKH = rs[rs.column_name == 'JKKH']
TYPE = rs[rs.column_name == 'TYPE']
XM = rs[rs.column_name == 'XM']
XB = rs[rs.column_name == 'XB']
tb_mz_cfzb_x = pd.concat([h_cfh, m_ghxh, JKKH, TYPE, h_lxbm, ksbm, ksbm,
                          ysbm, ysbm, h_cfrq, XM, XB, fylb, h_cfhj, zxks, zxks])
tb_mz_cfzb_x.to_csv("D:/robot-match-py/data1/tb_mz_cfzb_x.csv",index=False)