from flask import render_template, flash, redirect, request, url_for
from app import app, db
from models import Transaction
from api import tip, post_invoice_API
import json

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    

@app.route('/go' , methods=['GET', 'POST'])
def first():
    if request.method == 'POST':
        
        data = Transaction(
            currency=request.form['currency'],
            amount=request.form['amount'],
            description=request.form['description'],
            )
        db.session.add(data)
        db.session.commit()

        if request.form["currency"]=="840":
            tip_data = tip(data)
            data = tip_data[0]
            data['sign']=tip_data[1]
            return render_template(
                'between.html',
                data = data,
                )

        if request.form["currency"]=="978":
            text = post_invoice_API(data)

            
            return render_template(
                "euro.html",
                data=data,
                text = text
                )
        else:
            return render_template("index.html")
        
@app.route('/log')
def log():
    if request.method == 'GET':
        data=Transaction.query.all()
        return render_template('log.html',data=data)

