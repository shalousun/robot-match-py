YLJGDM = rs[rs.column_name == 'YLJGDM']
ZYH = rs[rs.column_name == 'ZYH']
XM = rs[rs.column_name == 'XM']
XB = rs[rs.column_name == 'XB']
MZYSGH = rs[rs.column_name == 'MZYSGH']
MZYSXM = rs[rs.column_name == 'MZYSXM']
ZYYSBH = rs[rs.column_name == 'ZYYSBH']
ZYYSXM = rs[rs.column_name == 'ZYYSXM']
RYKSBM = rs[rs.column_name == 'RYKSBM']
RYKSMC = rs[rs.column_name == 'RYKSMC']
RYZDBM = rs[rs.column_name == 'RYZDBM']
RYZDMC = rs[rs.column_name == 'RYZDMC']
RYSJ = rs[rs.column_name == 'RYSJ']
tb_zy_rydjb_y = pd.concat([YLJGDM, ZYH, XM, XB, MZYSGH, MZYSXM, ZYYSBH,
                           ZYYSXM, RYKSBM, RYKSMC, RYZDBM, RYZDMC, RYSJ])
tb_zy_rydjb_y.to_csv("D:/robot-match-py/data1/tb_zy_rydjb_y.csv",index=False)
