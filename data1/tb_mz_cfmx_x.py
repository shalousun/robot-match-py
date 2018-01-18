h_cfh = rs[rs.column_name == 'h_cfh']
m_ghxh = rs[rs.column_name == 'm_ghxh']
connect = get_connect()
mss_sql = SqlServerProvider(connect)
rs = mss_sql.get_view_fields_info("RS_ResidentInfo")
JKKH = rs[rs.column_name == 'JKKH']
TYPE = rs[rs.column_name == 'TYPE']
tb_mz_cfmx_x = pd.concat([h_cfh, m_ghxh, JKKH, TYPE])
tb_mz_cfmx_x.to_csv("D:/robot-match-py/data1/tb_mz_cfmx_x.csv",index=False)
