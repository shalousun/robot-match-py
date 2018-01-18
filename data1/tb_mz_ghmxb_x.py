m_ghxh = rs[rs.column_name == 'm_ghxh']
m_ghrq = rs[rs.column_name == 'm_ghrq']
ghlb = rs[rs.column_name == 'ghlb']
ifjz = rs[rs.column_name == 'ifjz']
m_brxm = rs[rs.column_name == 'm_brxm']
ksbm = rs[rs.column_name == 'ksbm']
ysbm = rs[rs.column_name == 'ysbm']
m_ghje = rs[rs.column_name == 'm_ghje']
m_zlje = rs[rs.column_name == 'm_zlje']
ghlsh = rs[rs.column_name == 'ghlsh']
connect = get_connect()
mss_sql = SqlServerProvider(connect)
rs = mss_sql.get_view_fields_info("RS_ResidentInfo")
JKKH = rs[rs.column_name == 'JKKH']
TYPE = rs[rs.column_name == 'TYPE']
XB = rs[rs.column_name == 'XB']
CSRQ = rs[rs.column_name == 'CSRQ']
tb_mz_ghmxb_x = pd.concat([m_ghxh, JKKH, TYPE, m_ghrq, ghlb, ifjz, m_brxm,
                           XB, CSRQ, ksbm, ksbm, ysbm, ysbm, m_ghje,
                           m_zlje, ghlsh])
tb_mz_ghmxb_x.to_csv("D:/robot-match-py/data1/tb_mz_ghmxb_x.csv",index=False)
