JZLSH = rs[rs.column_name == 'JZLSH']
SFJSSJ = rs[rs.column_name == 'SFJSSJ']
KDKSBM = rs[rs.column_name == 'KDKSBM']
KDKSMC = rs[rs.column_name == 'KDKSMC']
KDYSBH = rs[rs.column_name == 'KDYSBH']
KDYSXM = rs[rs.column_name == 'KDYSXM']
SFXMLBBM = rs[rs.column_name == 'SFXMLBBM']
MXXMBM = rs[rs.column_name == 'MXXMBM']
MXXMMC = rs[rs.column_name == 'MXXMMC']
MXXMDJ = rs[rs.column_name == 'MXXMDJ']
MXXMSL = rs[rs.column_name == 'MXXMSL']
MXXMYSJE = rs[rs.column_name == 'MXXMYSJE']
MXXMSSJE = rs[rs.column_name == 'MXXMSSJE']
tb_zy_sfmxb_y = pd.concat([JZLSH, SFJSSJ, KDKSBM, KDKSMC, KDYSBH, KDYSXM,
                           SFXMLBBM, MXXMBM, MXXMMC, MXXMDJ, MXXMSL, MXXMYSJE, MXXMSSJE])
tb_zy_sfmxb_y.to_csv("D:/robot-match-py/data1/tb_zy_sfmxb_y.csv",index=False)
