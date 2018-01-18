m_sfxh = rs[rs.column_name == 'm_sfxh']
m_ghxh = rs[rs.column_name == 'm_ghxh']
m_sjh = rs[rs.column_name == 'm_sjh']
m_sfrq = rs[rs.column_name == 'm_sfrq']
m_sfje = rs[rs.column_name == 'm_sfje']
connect = get_connect()
mss_sql = SqlServerProvider(connect)
rs = mss_sql.get_view_fields_info("RS_ResidentInfo")
JKKH = rs[rs.column_name == 'JKKH']
TYPE = rs[rs.column_name == 'TYPE']
tb_mz_jsb_x = pd.concat([m_sfxh, JKKH, TYPE, m_ghxh, m_sjh, m_sfrq, m_sfje,
                         m_sfje])
tb_mz_jsb_x.to_csv("D:/robot-match-py/data1/tb_mz_jsb_x.csv",index=False)