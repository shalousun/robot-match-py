tb_lis_jybg_x = pd.read_csv("D:/robot-match-py/data1/tb_lis_jybg_x.csv")
tb_lis_jybg_y = pd.read_csv("D:/robot-match-py/data1/tb_lis_jybg_y.csv")
tb_lis_jyjgzb_x = pd.read_csv("D:/robot-match-py/data1/tb_lis_jyjgzb_x.csv")
tb_lis_jyjgzb_y = pd.read_csv("D:/robot-match-py/data1/tb_lis_jyjgzb_y.csv")
tb_lis_ymjg_x = pd.read_csv("D:/robot-match-py/data1/tb_lis_ymjg_x.csv")
tb_lis_ymjg_y = pd.read_csv("D:/robot-match-py/data1/tb_lis_ymjg_y.csv")
tb_mz_cfmx_x = pd.read_csv("D:/robot-match-py/data1/tb_mz_cfmx_x.csv")
tb_mz_cfmx_y = pd.read_csv("D:/robot-match-py/data1/tb_mz_cfmx_y.csv")
tb_mz_cfzb_x = pd.read_csv("D:/robot-match-py/data1/tb_mz_cfzb_x.csv")
tb_mz_cfzb_y = pd.read_csv("D:/robot-match-py/data1/tb_mz_cfzb_y.csv")
tb_mz_ghmxb_x = pd.read_csv("D:/robot-match-py/data1/tb_mz_ghmxb_x.csv")
tb_mz_ghmxb_y = pd.read_csv("D:/robot-match-py/data1/tb_mz_ghmxb_y.csv")
tb_mz_jsb_x = pd.read_csv("D:/robot-match-py/data1/tb_mz_jsb_x.csv")
tb_mz_jsb_y = pd.read_csv("D:/robot-match-py/data1/tb_mz_jsb_y.csv")
tb_mz_jzjl_x = pd.read_csv("D:/robot-match-py/data1/tb_mz_jzjl_x.csv")
tb_mz_jzjl_y = pd.read_csv("D:/robot-match-py/data1/tb_mz_jzjl_y.csv")
tb_mz_sfmxb_x = pd.read_csv("D:/robot-match-py/data1/tb_mz_sfmxb_x.csv")
tb_mz_sfmxb_y = pd.read_csv("D:/robot-match-py/data1/tb_mz_sfmxb_y.csv")
tb_zy_cydjb_x = pd.read_csv("D:/robot-match-py/data1/tb_zy_cydjb_x.csv")
tb_zy_cydjb_y = pd.read_csv("D:/robot-match-py/data1/tb_zy_cydjb_y.csv")
tb_zy_rydjb_x = pd.read_csv("D:/robot-match-py/data1/tb_zy_rydjb_x.csv")
tb_zy_rydjb_y = pd.read_csv("D:/robot-match-py/data1/tb_zy_rydjb_y.csv")
tb_zy_zyjsb_x = pd.read_csv("D:/robot-match-py/data1/tb_zy_zyjsb_x.csv")
tb_zy_zyjsb_y = pd.read_csv("D:/robot-match-py/data1/tb_zy_zyjsb_y.csv")
tb_zy_zyjzjl_x = pd.read_csv("D:/robot-match-py/data1/tb_zy_zyjzjl_x.csv")
tb_zy_zyjzjl_y = pd.read_csv("D:/robot-match-py/data1/tb_zy_zyjzjl_y.csv")
tb_zy_zyyzmx_x = pd.read_csv("D:/robot-match-py/data1/tb_zy_zyyzmx_x.csv")
tb_zy_zyyzmx_y = pd.read_csv("D:/robot-match-py/data1/tb_zy_zyyzmx_y.csv")
tb_zy_sfmxb_x = pd.read_csv("D:/robot-match-py/data1/tb_zy_sfmxb_x.csv")
tb_zy_sfmxb_y = pd.read_csv("D:/robot-match-py/data1/tb_zy_sfmxb_y.csv")
dataset_x = pd.concat([tb_lis_jybg_x, tb_lis_jyjgzb_x, tb_lis_ymjg_x,
                       tb_mz_cfmx_x, tb_mz_cfzb_x, tb_mz_ghmxb_x,
					   tb_mz_jsb_x, tb_mz_jzjl_x, tb_mz_sfmxb_x,
					   tb_zy_cydjb_x, tb_zy_rydjb_x, tb_zy_zyjsb_x,
					   tb_zy_zyjzjl_x, tb_zy_zyyzmx_x, tb_zy_sfmxb_x],ignore_index = True)
dataset_y = pd.concat([tb_lis_jybg_y, tb_lis_jyjgzb_y, tb_lis_ymjg_y,
                       tb_mz_cfmx_y, tb_mz_cfzb_y, tb_mz_ghmxb_y,
					   tb_mz_jsb_y, tb_mz_jzjl_y, tb_mz_sfmxb_y,
					   tb_zy_cydjb_y, tb_zy_rydjb_y, tb_zy_zyjsb_y,
					   tb_zy_zyjzjl_y, tb_zy_zyyzmx_y, tb_zy_sfmxb_y], ignore_index = True)
dataset_x.data_type = dataset_y.data_type.astype("int64")
data_x = dataset_x.drop(["NUMERIC_PRECISION","CHARACTER_MAXIMUM_LENGTH",
                         "NUMERIC_SCALE"],axis=1)
data_x = dataset_x.drop(["NUMERIC_PRECISION","CHARACTER_MAXIMUM_LENGTH",
                         "NUMERIC_SCALE"],axis=1)
data_y = dataset_y.drop(["data_length","high_value","low_value","data_precision"],axis=1)
data_x.to_csv("D:/robot-match-py/data1/data_x.csv",index=False)
data_y.to_csv("D:/robot-match-py/data1/data_y.csv",index=False)
table_x = data_x.loc[:,["table_name","column_name"]]
table_y = data_y.loc[:,["table_name","column_name"]]
data_x.drop(["table_name","column_name"],axis = 1,inplace = True)
data_y.drop(["table_name","column_name"],axis = 1,inplace = True)
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(data_x, data_y, test_size = 0.3)
reg = MLPRegressor()
reg.fit(train_x, train_y)


