from flask import Flask,render_template
import psycopg2


conn = psycopg2.connect(
    host = 'localhost',
    dbname = 'myduka_db',
    user = 'postgres',
    password = 'ianojr',
    port = 5432
)
cur = conn.cursor()


app = Flask(__name__)

# The first route is the slash alone.
@app.route('/')
def hello():
    return render_template("index.html")



#Easy one.
@app.route('/home')
def home():
    return '<h1>Hello!</h1> <br> <h3>Welcome Home</h3>'

@app.route('/products')
def display_products():
    cur.execute("select * from products;")
    products = cur.fetchall()
    return render_template('products.html',prods=products)

@app.route('/sales')
def display_sales():
    cur.execute("select * from sales;")
    sales = cur.fetchall()
    return render_template('sales.html', sales = sales)

app.run(debug = True)