from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(15))
    address = db.Column(db.String(200))

@app.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        email = request.form['email']
        phone = request.form['phone']

        # Email validation
        
        if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email):
             flash("Invalid email format!", "danger")
             return redirect('/add')
        # Phone number validation
        if not phone.isdigit() or len(phone) != 10:
            flash("Invalid phone number! Must be 10 digits.", "danger")
            return redirect('/add')

        # Duplicate email check
        if Contact.query.filter_by(email=email).first():
            flash("Email already exists!", "danger")
            return redirect('/add')
        if Contact.query.filter_by(phone=phone).first():
            flash("Phone number already exists!", "danger")
            return redirect('/add')
        
        contact = Contact(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            email=email,
            phone=phone,
            address=request.form['address']
        )
        db.session.add(contact)
        db.session.commit()
        flash("Contact added successfully!", "success")
        return redirect('/')
    return render_template('add.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    contact = Contact.query.get(id)
    if request.method == 'POST':
        contact.first_name = request.form['first_name']
        contact.last_name = request.form['last_name']
        contact.email = request.form['email']
        contact.phone = request.form['phone']
        contact.address = request.form['address']
        db.session.commit()
        flash("Contact updated successfully!", "success")
        return redirect('/')
    return render_template('update.html', contact=contact)

@app.route('/delete/<int:id>')
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    flash("Contact deleted successfully!", "info")
    return redirect('/')

# ✅ Server start block (must be present!)
if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True)