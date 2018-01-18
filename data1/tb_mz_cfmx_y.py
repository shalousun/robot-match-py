CFH = rs[rs.column_name == 'CFH']
JZLSH = rs[rs.column_name == 'JZLSH']
KH = rs[rs.column_name == 'KH']
KLX = rs[rs.column_name == 'KLX']
tb_mz_cfmx_y = pd.concat([CFH, JZLSH, KH, KLX])
tb_mz_cfmx_y.to_csv("D:/robot-match-py/data1/tb_mz_cfmx_y.csv",index=False)
