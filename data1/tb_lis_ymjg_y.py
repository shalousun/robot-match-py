BGDH = rs[rs.column_name == "BGDH"]
XJDH = rs[rs.column_name == "XJDH"]
YMDM = rs[rs.column_name == "YMDM"]
YMMC = rs[rs.column_name == "YMMC"]
JCJG = rs[rs.column_name == "JCJG"]
tb_lis_ymjg_y = pd.concat([BGDH, XJDH, YMDM, YMMC, JCJG])
tb_lis_ymjg_y.to_csv("D:/robot-match-py/data1/tb_lis_ymjg_y.csv",index=False)
