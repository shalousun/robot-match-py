input_date = rs[rs.column_name == "input_date"]
doc_inspec = rs[rs.column_name == "doc_inspec"]
item_code = rs[rs.column_name == "itemname"]
inspec_name = rs[rs.column_name == "inspec_name"]
units = rs[rs.column_name == "units"]
ranges = rs[rs.column_name == "ranges"]
instrument = rs[rs.column_name == "instrument"]
tb_lis_jyjgzb_x = pd.concat([input_date, doc_inspec, item_code,
                             inspec_name, units, ranges,
                             units, instrument])
tb_lis_jyjgzb_x.to_csv("D:/robot-match-py/data1/tb_lis_jyjgzb_x.csv",index=False)
