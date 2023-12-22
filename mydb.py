# import psycopg2
# conn = psycopg2.connect("dbname='myduka_db' user='postgres' host='localhost' password='ianojr'")

# cur = conn.cursor()
# cur.execute()

# cur.execute("select * from preducts;")

# rows = cur.fetchall()
# print(rows)

import psycopg2


hostname = "localhost"
database = "myduka_db"
owner = "postgres"
password = "ianojr"
port_id = 5432

conn = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = owner,
    password = password,
    port = port_id
)
cur = conn.cursor()
def display_products():
    cur.execute("select * from products;")
    #not necessary to be rows
    rows = cur.fetchall()
    return rows

# insert = ("""INSERT INTO public.products(name, buying_price, selling_price, quantity)
# 	VALUES ('Xbox',90000, 10000, 5);""")
# cur.execute(insert)
conn.commit()