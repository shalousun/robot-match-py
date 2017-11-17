# python安装
下载新的python安装包安装即可。windows上安装的时请选择相应的pip来方便后续包的安装。如果python的版本比较新的可能会导致pip直接安装包失败，
找不到对应的版本，这种需要下载到本地再使用pip安装

# 安装numpy&安装matplotlib& scipy
numpy&安装matplotlib& scipy是一些数学相关的库。

## 安装numpy
1. 下载地址：https://pypi.python.org/pypi/numpy（各取所需）
2. 将下载的numpy放到python安装路径的scripts环境下。
3. 使用pip进行安装numpy,命令如下：

```
 pip install D:\ProgramFiles\python27\Scripts\numpy-1.13.3-cp36-none-win_amd64.whl
```
如果python的版本不是很高可以直接使用下列命名安装

```
pip install numpy
```

## 安装scipy

安装同numpy的步骤

```
pip install scipy
```

## 安装matplotlib

```
pip install matplotlib
```


## 安装scikit-learn
scikit-learn是一个机器学习库

```
pip install scikit-learn
```

## 安装pymysql
pymysql是python连接mysql数据库的驱动，需要连接mysql则安装它。

```
pip install pymysql
```
当然也可以mysql官方出品mysql-connector

```
pip install mysql-connector
```


## 安装cx_Oracle

cx_Oracle是Python连接oracle数据库的驱动
```
pip install cx_Oracle
```
## 安装pymssql
pymssql数python连接SQLSERVER数据库的驱动

```
pip install pymssql
```
