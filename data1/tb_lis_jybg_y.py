BGRQ = rs[rs.column_name == 'BGRQ']
BRXM = rs[rs.column_name == 'BRXM']
BRXB = rs[rs.column_name == 'BRXB']
BRNL = rs[rs.column_name == 'BRNL']
BQ = rs[rs.column_name == 'BQ']
CH = rs[rs.column_name == 'CH']
SQRGH = rs[rs.column_name == 'SQRGH']
SQRXM = rs[rs.column_name == 'SQRXM']
BGRGH = rs[rs.column_name == 'BGRGH']
BGRXM = rs[rs.column_name == 'BGRXM']
SQKSMC = rs[rs.column_name == 'SQKSMC']
SQRQ = rs[rs.column_name == 'SQRQ']
CJRQ = rs[rs.column_name == 'CJRQ']
JYRQ = rs[rs.column_name == 'JYRQ']
JYJSBH = rs[rs.column_name == 'JYJSBH']
JYJSQM = rs[rs.column_name == 'JYJSQM']
JYYSBH = rs[rs.column_name == 'JYYSBH']
JYYSQM = rs[rs.column_name == 'JYYSQM']
BBDM = rs[rs.column_name == 'BBDM']
BBMC = rs[rs.column_name == 'BBMC']
tb_lis_jybg_y = pd.concat([BGRQ, BRXM, BRXB, BRNL,
                           BQ, CH, SQRGH, SQRXM,
                           BGRGH, BGRXM, SQKSMC, SQRQ,
                           CJRQ, JYRQ, JYJSBH,
                           JYJSQM, JYYSBH, JYYSQM, BBDM,
                           BBMC])
tb_lis_jybg_y.to_csv("D:/robot-match-py/data1/tb_lis_jybg_y.csv",index=False)