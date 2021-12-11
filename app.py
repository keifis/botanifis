from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.m_plant'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Plant(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), nullable=False)

@app.route('/')
def index():
    print("testest", flush=True)
    data = Plant.query.all()
    return render_template('plant.html',data=data)

#以下追加↓	
@app.route('/add', methods=['POST'])
def add():
    print("testest", flush=True)
    name = request.form['name']
    new_plant = Plant(name=name)
    db.session.add(new_plant)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/del_plant/<int:id>')
def del_plant(id):
    del_data = Plant.query.filter_by(id=id).first()
    db.session.delete(del_data)
    db.session.commit()
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True)