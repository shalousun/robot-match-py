JZLSH = rs[rs.column_name == 'JZLSH']
HZXM = rs[rs.column_name == 'HZXM']
ZZYSGH = rs[rs.column_name == 'ZZYSGH']
JZZDBM = rs[rs.column_name == 'JZZDBM']
JZZDMC = rs[rs.column_name == 'JZZDMC']
ZS = rs[rs.column_name == 'ZS']
FBRQSJ = rs[rs.column_name == 'FBRQSJ']
tb_mz_jzjl_y = pd.concat([JZLSH, HZXM, ZZYSGH, JZZDBM, JZZDMC, ZS, FBRQSJ])
tb_mz_jzjl_y.to_csv("D:/robot-match-py/data1/tb_mz_jzjl_y.csv",index=False)