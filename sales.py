import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    dbname = 'myduka_db',
    user = 'postgres',
    password = 'ianojr',
    port = 5432
)
cur = conn.cursor()

def display_products():
    cur.execute("select * from sales;")
    #not necessary to be rows
    rows = cur.fetchall()
    return rows
conn.commit()