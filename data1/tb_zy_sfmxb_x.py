z_bah = rs[rs.column_name == 'z_bah']
z_sfrq = rs[rs.column_name == 'z_sfrq']
ksbm = rs[rs.column_name == 'ksbm']
ysbm = rs[rs.column_name == 'ysbm']
fylb = rs[rs.column_name == 'fylb']
connect = get_connect()
mss_sql = SqlServerProvider(connect)
rs = mss_sql.get_view_fields_info("ksbmk")
ksmc = rs[rs.column_name == 'ksmc']
connect = get_connect()
mss_sql = SqlServerProvider(connect)
rs = mss_sql.get_view_fields_info("czyk")
czymc = rs[rs.column_name == 'czymc']
connect = get_connect()
mss_sql = SqlServerProvider(connect)
rs = mss_sql.get_view_fields_info("EMR_ZY_FYMX")
XMDM_HIS = rs[rs.column_name == 'XMDM_HIS']
XMMC_HIS = rs[rs.column_name == 'XMMC_HIS']
XMDJ = rs[rs.column_name == 'XMDJ']
XMSL = rs[rs.column_name == 'XMSL']
XMJE = rs[rs.column_name == 'XMJE']
tb_zy_sfmxb_x = pd.concat([z_bah, z_sfrq, ksbm, ksmc, ysbm, czymc,
                           fylb, XMDM_HIS, XMMC_HIS, XMDJ, XMSL, XMJE, XMJE])
tb_zy_sfmxb_x.to_csv("D:/robot-match-py/data1/tb_zy_sfmxb_x.csv",index=False)