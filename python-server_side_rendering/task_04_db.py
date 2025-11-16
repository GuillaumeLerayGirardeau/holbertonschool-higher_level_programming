#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

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
    try:
        with open('items.json', encoding='utf-8') as f:
            data = json.load(f)
            items = data.get('items', [])
    except Exception:
        items = []
    return render_template('items.html', items = items)

@app.route('/products')
def products():
    source = request.args.get('source')
    if not source:
        products = []
        return render_template('product_display.html', products = products)

    try:
        if source == 'json':
            with open('products.json', 'r', encoding='utf-8') as f:
                products = json.load(f)
        elif source == 'csv':
            with open('products.csv', 'r', encoding='utf-8') as f:
                data = csv.DictReader(f)
                products = []
                for row in data:
                    row['id'] = int(row['id'])
                    products.append(row)
        elif source == 'sql':
            products = read_sqlite()
        else:
            products = "Wrong source"
    except Exception:
        products = []

    if isinstance(products, str):
        return render_template('product_display.html', products = products)

    id = request.args.get('id')
    if id is None:
        return render_template('product_display.html', products = products)
    else:
        try:
            id = int(id)
        except ValueError:
            return render_template('product_display.html', products = "Product not found")

        product = next((p for p in products if p['id'] == id), None)
        if product:
            prod_list = [product]
            return render_template('product_display.html', products = prod_list)
        else:
            return render_template('product_display.html', products = "Product not found")
        
def read_sqlite():

    connection = sqlite3.connect('products.db')
    connection.row_factory = sqlite3.Row  
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    return [dict(row) for row in rows]






if __name__ == '__main__':
    app.run(debug=True, port=5000)