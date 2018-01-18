BGRQ = rs[rs.column_name == "BGRQ"]
JCRXM = rs[rs.column_name == "JCRXM"]
JCZBDM = rs[rs.column_name == "JCZBDM"]
JCZBMC = rs[rs.column_name == "JCZBMC"]
JYDLJGJSDW = rs[rs.column_name == "JYDLJGJSDW"]
CKZ = rs[rs.column_name == "CKZ"]
JLDW = rs[rs.column_name == "JLDW"]
SBBM = rs[rs.column_name == "SBBM"]
tb_lis_jyjgzb_y = pd.concat([BGRQ, JCRXM, JCZBDM,
                             JCZBMC, JYDLJGJSDW, CKZ,
                             JLDW, SBBM])
tb_lis_jyjgzb_y.to_csv("D:/robot-match-py/data1/tb_lis_jyjgzb_y.csv",index=False)
