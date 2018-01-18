MJZH = rs[rs.column_name == 'MJZH']
SFRQ = rs[rs.column_name == 'SFRQ']
SFXMDM = rs[rs.column_name == 'SFXMDM']
SFXMMC = rs[rs.column_name == 'SFXMMC']
SFXMDJ = rs[rs.column_name == 'SFXMDJ']
SFXMSL = rs[rs.column_name == 'SFXMSL']
SFXMJE = rs[rs.column_name == 'SFXMJE']
tb_mz_sfmxb_x = pd.concat([MJZH, SFRQ, SFXMDM, SFXMMC, SFXMDJ, SFXMSL,
                           SFXMJE, SFXMJE])
tb_mz_sfmxb_x.to_csv("D:/robot-match-py/data1/tb_mz_sfmxb_x.csv",index=False)