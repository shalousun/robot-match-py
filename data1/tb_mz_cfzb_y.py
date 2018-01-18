CFH = rs[rs.column_name == 'CFH']
JZLSH = rs[rs.column_name == 'JZLSH']
KH = rs[rs.column_name == 'KH']
KLX = rs[rs.column_name == 'KLX']
CFLX = rs[rs.column_name == 'CFLX']
JZKSDM = rs[rs.column_name == 'JZKSDM']
JZKSMC = rs[rs.column_name == 'JZKSMC']
KFYSGH = rs[rs.column_name == 'KFYSGH']
KFYSXM = rs[rs.column_name == 'KFYSXM']
KFRQ = rs[rs.column_name == 'KFRQ']
HZXM = rs[rs.column_name == 'HZXM']
HZXB = rs[rs.column_name == 'HZXB']
FB = rs[rs.column_name == 'FB']
CFJE = rs[rs.column_name == 'CFJE']
ZXKSBM = rs[rs.column_name == 'ZXKSBM']
ZXKSMC = rs[rs.column_name == 'ZXKSMC']
tb_mz_cfzb_y = pd.concat([CFH, JZLSH, KH, KLX, CFLX, JZKSDM, JZKSMC,
                          KFYSGH, KFYSXM, KFRQ, HZXM, HZXB, FB, CFJE, ZXKSBM, ZXKSMC])
tb_mz_cfzb_y.to_csv("D:/robot-match-py/data1/tb_mz_cfzb_y.csv",index=False)
