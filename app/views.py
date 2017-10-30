from flask import render_template, flash, redirect, request
from app import app, db
from models import Transaction
from api import tip, post_invoice_API

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
            
            sign = tip(data)
            
            return render_template(
                "dollar.html",
                data=data,
                sign=sign)

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

