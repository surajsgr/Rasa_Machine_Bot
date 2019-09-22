import psycopg2
import pandas as pd

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
conn = psycopg2.connect(host="0.0.0.0", user="postgres", password="12345", port="5434",dbname='testdb1')
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()

psql="SET datestyle = dmy;"
cursor.execute(psql)

df = pd.read_csv('master.tsv', sep='\t')
df.fillna('N', inplace=True)
df.drop(df.columns[df.columns.str.contains('Unnamed',case = False)], axis = 1,inplace=True)
df['EAN'] = df['EAN'].astype(float)
df.to_csv('main.csv', sep='~', index=False, float_format = '%.0f')
#
psql="""

select * from machine



"""
# SELECT CEILING(Extract(month from Date_1)) as mon from machine
cursor.execute(psql)
N=cursor.fetchall()
for i in N:
    for j in i:
        print(j)

with open('main.csv','r') as f:
   next(f)
   cursor.copy_from(f, 'machine', sep='~')


conn.commit()