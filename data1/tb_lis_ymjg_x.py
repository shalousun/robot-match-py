micro_item_id = rs[rs.column_name == "micro_item_id"]
micro_item_name_cn = rs[rs.column_name == "micro_item_name_cn"]
connect = get_connect()
mss_sql = SqlServerProvider(connect)
rs = mss_sql.get_view_fields_info("inspec_micro_item_combine")
micro_serial_no = rs[rs.column_name == "micro_serial_no"]
combine_sort = rs[rs.column_name == "combine_sort"]
result2 = rs[rs.column_name == "result2"]
tb_lis_ymjg_x = pd.concat([micro_serial_no, combine_sort, micro_item_id,
                           micro_item_name_cn, result2])
tb_lis_ymjg_x.to_csv("D:/robot-match-py/data1/tb_lis_ymjg_x.csv",index=False)
