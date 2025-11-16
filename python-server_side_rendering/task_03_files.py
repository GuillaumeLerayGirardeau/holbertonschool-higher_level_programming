#!/usr/bin/python3

from flask import Flask, render_template, request
import os
import json
import csv

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
    if not source or not os.path.exists(source):
        products = []
        return render_template('product_display.html', products = products)

    ext = os.path.splitext(source)[1].lower()
    try:
        with open(source, 'r', encoding='utf-8') as f:
            if ext == '.json':
                products = json.load(f)
            elif ext == '.csv':
                data = csv.DictReader(f)
                products = [row for row in data]
    except Exception:
        products = []

    id = request.args.get('id')
    if id is None:
        return render_template('product_display.html', products = products)
    else:
        if any(id in p.id for p in products):
            return render_template('product_display.html', products = products[id])
        else:
            return render_template('product_display.html', products = products[id])


if __name__ == '__main__':
    app.run(debug=True, port=5000)