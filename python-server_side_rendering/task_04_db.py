from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def read_csv(file_path):
    content = []
    with open(file_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            content.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return content

def read_sql():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    rows = cursor.fetchall()
    products = []
    for row in rows:
        products.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        })
    connection.close()
    return products

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = json.load(file)
    return render_template('items.html', items=data['items'])

@app.route('/products')
def products():
    source = request.args.get('source')
    file_path = None

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        file_path = 'products.json'
    elif source == 'csv':
        file_path = 'products.csv'

    if file_path == 'products.json':
        data = read_json(file_path)
    elif file_path == 'products.csv':
        data = read_csv(file_path)
    elif source == 'sql':
        data = read_sql()

    product_id = request.args.get('id', type=int)
    if product_id:
        product = next((item for item in data if item['id'] == product_id), None)
        if product:
            return render_template('product_display.html', products=[product])
        else:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)