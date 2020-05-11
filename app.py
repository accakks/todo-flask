from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://akku:akku@localhost:5432/todoapp'

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

db.create_all()

@app.route('/')
def index():
    print()
    return render_template('index.html', data=Todo.query.all())


@app.route('/todos/create', methods=['POST'])
def create_todo():
    description = request.get_json()['description']
    new_item = Todo(description=description)
    db.session.add(new_item)
    db.session.commit()
    return jsonify({
        'description': new_item.description

    })

if __name__ == "__main__":
        app.run(debug=True)
