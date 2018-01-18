YLJGDM = rs[rs.column_name == "YLJGDM"]
ZYH = rs[rs.column_name == "ZYH"]
CYKSBM = rs[rs.column_name == "CYKSBM"]
CYKSMC = rs[rs.column_name == "CYKSMC"]
ZYYSGH = rs[rs.column_name == "ZYYSGH"]
ZYYSXM = rs[rs.column_name == "ZYYSXM"]
CYSJ = rs[rs.column_name == "CYSJ"]
CYZDMC = rs[rs.column_name == "CYZDMC"]
tb_zy_cydjb_y = pd.concat([YLJGDM, ZYH, CYKSBM, CYKSMC,
                           ZYYSGH, ZYYSXM, CYSJ, CYZDMC])
tb_zy_cydjb_y.to_csv("D:/robot-match-py/data1/tb_zy_cydjb_y.csv",index=False)
