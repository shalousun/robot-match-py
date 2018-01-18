JZLSH = rs[rs.column_name == 'JZLSH']
KH = rs[rs.column_name == 'KH']
KLX = rs[rs.column_name == 'KLX']
GTHSJ = rs[rs.column_name == 'GTHSJ']
GHLB = rs[rs.column_name == 'GHLB']
SFJZ = rs[rs.column_name == 'SFJZ']
XM = rs[rs.column_name == 'XM']
XB = rs[rs.column_name == 'XB']
CSRQ = rs[rs.column_name == 'CSRQ']
KSBM = rs[rs.column_name == 'KSBM']
KSMC = rs[rs.column_name == 'KSMC']
GHYSGH = rs[rs.column_name == 'GHYSGH']
GHYSXM = rs[rs.column_name == 'GHYSXM']
GHF = rs[rs.column_name == 'GHF']
ZLF = rs[rs.column_name == 'ZLF']
GHSXH = rs[rs.column_name == 'GHSXH']
tb_mz_ghmxb_y = pd.concat([JZLSH, KH, KLX, GTHSJ, GHLB, SFJZ, XM,
                           XB, CSRQ, KSBM, KSMC, GHYSGH, GHYSXM, GHF,
                           ZLF, GHSXH])
tb_mz_ghmxb_y.to_csv("D:/robot-match-py/data1/tb_mz_ghmxb_y.csv",index=False)