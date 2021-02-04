import sqlite3
conn = sqlite3.connect('base/data.sqlite')
cursor = conn.cursor()
cursor.execute('''
create table if not exists NewUsers(id integer,
 username text,
 phonenumber integer,
  code integer)
''')

create table if not exists IdentifiedUsers(id integer,
 status integer)
''')

create table if not exists RandomNumbers(id integer,
 random_number integer)
''')

conn.commit()


