#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('testHome.html')

@app.route('/urlSchema', methods=['GET'])
def urlSchema():
    return render_template('urlSchema.html')

if __name__ == '__main__':
    app.run()
