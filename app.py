from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://akku:akku@localhost:5432/todoapp'

db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default = False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

#db.create_all()



@app.route('/')
def index():
    print()
    return render_template('index.html', data=Todo.query.all())


@app.route('/todos/create', methods=['POST'])
def create_todo():
    error = False
    body = {}
    try:
        description = request.get_json()['description']
        new_item = Todo(description=description)
        db.session.add(new_item)
        db.session.commit()
        body['description'] = new_item.description
      
    except: 
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort (400)
    if not error:
        return jsonify(body)

if __name__ == "__main__":
        app.run(debug=True)
