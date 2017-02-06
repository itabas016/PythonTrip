# coding=utf-8
import cx_Oracle

CONNSTRING = 'system/S$cur1ty1@icdb'

con = cx_Oracle.connect(CONNSTRING)
print(con.version)

curs = conn.cursor()
QUERYSQL = 'select u.username, s.tablespace_name, u.created, u.account_status ' + 'from dba_users u ' + 'inner join dba_segments s on s.owner = u.username ' + 'where u.username like ''BD_%'' and s.tablespace_name like ''DATALRG%'' ' + 'group by s.tablespace_name, u.username, u.created, u.account_status ' +  'order by u.created desc;'
curs.execute(QUERYSQL)
con.close()