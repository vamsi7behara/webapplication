import os
from forms import  AddForm , DelForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from tabulate import tabulate

#
app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

############################################
        # SQL DATABASE AND MODELS

##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

####model####

class Donor(db.Model):
    __tablename__ = 'donors'
    id = db.Column(db.Integer,primary_key = True)
    bloodtype= db.Column(db.Text)
    name = db.Column(db.Text)


    def __init__(self,name,bloodtype):
        self.name = name
        self.bloodtype=bloodtype
    def __repr__(self):
        return f"{self.id} Donor name: {self.name}. bloodtype: {self.bloodtype}"


#### VIEW FUNCTIONS __ HAVE forms
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add',methods=['GET','POST'])
def add_donor():

    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        bloodtype=form.bloodtype.data
        new_donor = Donor(name,bloodtype)
        db.session.add(new_donor)
        db.session.commit()
        return redirect(url_for('list_donor'))

    return render_template('add.html',form=form)


@app.route('/list')
def list_donor():
    donors = Donor.query.all()
    return render_template('list.html', donors=donors)


@app.route('/delete',methods=['GET','POST'])
def del_donor():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        donor = Donor.query.get(id)
        name = form.name.data
        db.session.delete(donor)
        db.session.commit()
        return redirect(url_for('list_donted'))
    return render_template('delete.html', form = form)

@app.route('/donated')
def list_donted():
    donors = Donor.query.all()
    return render_template('donatedlist.html', donors=donors)


if __name__ == '__main__':
    app.run(debug=True)
