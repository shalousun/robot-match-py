YLJGDM = rs[rs.column_name == "YLJGDM"]
CISID = rs[rs.column_name == "CISID"]
HZXM = rs[rs.column_name == "HZXM"]
JZKSBM = rs[rs.column_name == "JZKSBM"]
JZKSMC = rs[rs.column_name == "JZKSMC"]
CYKSBM = rs[rs.column_name == "CYKSBM"]
CYKSMC = rs[rs.column_name == "CYKSMC"]
RYSJ = rs[rs.column_name == "RYSJ"]
CYSJ = rs[rs.column_name == "CYSJ"]
tb_zy_zyjzjl_y = pd.concat([YLJGDM, CISID, HZXM, JZKSBM, JZKSMC, CYKSBM,
                            CYKSMC, RYSJ, CYSJ])
tb_zy_zyjzjl_y.to_csv("D:/robot-match-py/data1/tb_zy_zyjzjl_y.csv",index=False)
