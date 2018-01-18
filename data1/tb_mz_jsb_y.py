JSJLID = rs[rs.column_name == 'JSJLID']
KH = rs[rs.column_name == 'KH']
KLX = rs[rs.column_name == 'KLX']
JZLSH = rs[rs.column_name == 'JZLSH']
JSFPH = rs[rs.column_name == 'JSFPH']
FYJSSJ = rs[rs.column_name == 'FYJSSJ']
FYJSZJE = rs[rs.column_name == 'FYJSZJE']
SSJE = rs[rs.column_name == 'SSJE']
tb_mz_jsb_y = pd.concat([JSJLID, KH, KLX, JZLSH, JSFPH, FYJSSJ, FYJSZJE, SSJE])
tb_mz_jsb_y.to_csv("D:/robot-match-py/data1/tb_mz_jsb_y.csv",index=False)
