YLJGZZJGDM = rs[rs.column_name == "YLJGZZJGDM"]
ZYH = rs[rs.column_name == "ZYH"]
KSDM = rs[rs.column_name == "KSDM"]
KSMC = rs[rs.column_name == "KSMC"]
ZYYSGH = rs[rs.column_name == "ZYYSGH"]
ZYYSMC = rs[rs.column_name == "ZYYSMC"]
CYRQSJ = rs[rs.column_name == "CYRQSJ"]
CYZD = rs[rs.column_name == "CYZD"]
tb_zy_cydjb_x = pd.concat([YLJGZZJGDM, ZYH, KSDM, KSMC,
                           ZYYSGH, ZYYSMC, CYRQSJ, CYZD])
tb_zy_cydjb_x.to_csv("D:/robot-match-py/data1/tb_zy_cydjb_x.csv",index=False)
