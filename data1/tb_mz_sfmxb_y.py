SFRQ = rs[rs.column_name == 'SFRQ']
JZLSH = rs[rs.column_name == 'JZLSH']
SFJSSJ = rs[rs.column_name == 'SFJSSJ']
MXXMBM = rs[rs.column_name == 'MXXMBM']
MXXMMC = rs[rs.column_name == 'MXXMMC']
MXXMDJ = rs[rs.column_name == 'MXXMDJ']
MXXMSL = rs[rs.column_name == 'MXXMSL']
MXXMYSJE = rs[rs.column_name == 'MXXMYSJE']
MXXMSSJE = rs[rs.column_name == 'MXXMSSJE']
tb_mz_sfmxb_y = pd.concat([JZLSH, SFJSSJ, MXXMBM, MXXMMC, MXXMDJ, MXXMSL,
                           MXXMYSJE, MXXMSSJE])
tb_mz_sfmxb_y.to_csv("D:/robot-match-py/data1/tb_mz_sfmxb_y.csv",index=False)
