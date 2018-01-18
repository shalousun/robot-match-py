YLJGDM = rs[rs.column_name == "YLJGDM"]
ZYID = rs[rs.column_name == "ZYID"]
STFSJ = rs[rs.column_name == "STFSJ"]
ZFY = rs[rs.column_name == "ZFY"]
YBFWWZF = rs[rs.column_name == "YBFWWZF"]
YBZFJE = rs[rs.column_name == "YBZFJE"]
tb_zy_zyjsb_y = pd.concat([YLJGDM, ZYID, STFSJ, ZFY, YBFWWZF, YBZFJE])
tb_zy_zyjsb_y.to_csv("D:/robot-match-py/data1/tb_zy_zyjsb_y.csv",index=False)
