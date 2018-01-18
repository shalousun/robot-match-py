input_date = rs[rs.column_name == 'input_date']
p_name = rs[rs.column_name == 'p_name']
sex = rs[rs.column_name == 'sex']
age = rs[rs.column_name == 'age']
section = rs[rs.column_name == 'section']
bedno = rs[rs.column_name == 'bedno']
connect = get_connect()
mss_sql = SqlServerProvider(connect)
rs = mss_sql.get_view_fields_info("inspec_general_info_history")
request_no = rs[rs.column_name == 'request_no']
doc_request = rs[rs.column_name == 'doc_request']
doc_check = rs[rs.column_name == 'doc_check']
doc_inspec = rs[rs.column_name == 'doc_inspec']
time_request = rs[rs.column_name == 'time_request']
time_sample_collect = rs[rs.column_name == 'time_sample_collect']
input_date = rs[rs.column_name == 'input_date']
doc_check = rs[rs.column_name == 'doc_check']
doc_inspec = rs[rs.column_name == 'doc_inspec']
sample_barcode = rs[rs.column_name == 'sample_barcode']
sample_name = rs[rs.column_name == 'sample_name']
tb_lis_jybg_x = pd.concat([input_date, p_name, sex, age,
                           section, bedno, request_no, doc_request,
                           doc_check, doc_inspec, section, time_request,
                           time_sample_collect, input_date, doc_check,
                           doc_inspec, doc_check, doc_inspec, sample_barcode,
                           sample_name])
tb_lis_jybg_x.to_csv("D:/robot-match-py/data1/tb_lis_jybg_x.csv",index=False)