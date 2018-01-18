ZZJGDM = rs[rs.column_name == "ZZJGDM"]
BAH = rs[rs.column_name == "BAH"]
JSSJ = rs[rs.column_name == "JSSJ"]
ZJE = rs[rs.column_name == "ZJE"]
ZFJE = rs[rs.column_name == "ZFJE"]
YBJE = rs[rs.column_name == "YBJE"]
tb_zy_zyjsb_x = pd.concat([ZZJGDM, BAH, JSSJ, ZJE, ZFJE, YBJE])
tb_zy_zyjsb_x.to_csv("D:/robot-match-py/data1/tb_zy_zyjsb_x.csv",index=False)
