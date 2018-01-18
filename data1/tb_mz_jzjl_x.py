brxh = rs[rs.column_name == 'brxh']
xm = rs[rs.column_name == 'xm']
ysbm = rs[rs.column_name == 'ysbm']
zd = rs[rs.column_name == 'zd']
zdmc = rs[rs.column_name == 'zdmc']
zyxs = rs[rs.column_name == 'zyxs']
fbrq = rs[rs.column_name == 'fbrq']
tb_mz_jzjl_x = pd.concat([brxh, xm, ysbm, zd, zdmc, zyxs, fbrq])
tb_mz_jzjl_x.to_csv("D:/robot-match-py/data1/tb_mz_jzjl_x.csv",index=False)
