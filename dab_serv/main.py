import psycopg2 as pg
from jinja2 import Environment, FileSystemLoader, Template

table_heads = ('ID', 'Name', 'Age', 'Address')
table_heads_rus = ('ID', 'Имя', 'Возраст', 'Адрес')

data = []

db_conn = pg.connect('dbname=my_db user=user password=passwd host=127.0.0.1 port=5432')

cur = db_conn.cursor()
cur.execute('SELECT id, name, age, address FROM vb.people')
for row in cur:
    data.append(row)
db_conn.close()

print(data)

env = Environment(loader=FileSystemLoader('gb_lessons/templates'))
template = env.get_template('experience.htm')

html = template.render(theads=table_heads_rus, people_list=data)
print(html)