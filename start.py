from main import run
import pymysql

host = 'localhost'
user = 'root'
password = 'REDACTED_PASSWORD'
db = 'esleague'

conn = pymysql.connect(host=host, user=user, password=password, db=db)

run(conn)
