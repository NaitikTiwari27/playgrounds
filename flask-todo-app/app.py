from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "your-secret-key"


db = SQLAlchemy(app)


# Database Model
class Todo(db.Model):

    sno = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(200),
        nullable=False
    )

    desc = db.Column(
        db.String(500)
    )

    completed = db.Column(
        db.Boolean,
        default=False
    )

    date_created = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    def __repr__(self):
        return f"{self.sno} - {self.title}"



# Home page + Add Todo + Search
@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        title = request.form.get("title")
        desc = request.form.get("desc")


        if not title:
            flash(
                "Title cannot be empty!",
                "danger"
            )
            return redirect(url_for("home"))


        todo = Todo(
            title=title,
            desc=desc
        )


        db.session.add(todo)
        db.session.commit()


        flash(
            "Todo added successfully!",
            "success"
        )

        return redirect(url_for("home"))



    search = request.args.get("search")


    if search:

        allTodo = Todo.query.filter(
            Todo.title.contains(search)
        ).all()

    else:

        allTodo = Todo.query.order_by(
            Todo.date_created.desc()
        ).all()



    return render_template(
        "index.html",
        allTodo=allTodo
    )



# Update Todo
@app.route(
    "/update/<int:sno>",
    methods=["GET", "POST"]
)
def update(sno):

    todo = Todo.query.get_or_404(sno)


    if request.method == "POST":

        todo.title = request.form.get("title")
        todo.desc = request.form.get("desc")


        db.session.commit()


        flash(
            "Todo updated!",
            "success"
        )


        return redirect(
            url_for("home")
        )


    return render_template(
        "update.html",
        todo=todo
    )



# Mark complete
@app.route("/complete/<int:sno>")
def complete(sno):

    todo = Todo.query.get_or_404(sno)

    todo.completed = not todo.completed

    db.session.commit()


    return redirect(
        url_for("home")
    )



# Delete Todo
@app.route("/delete/<int:sno>")
def delete(sno):

    todo = Todo.query.get_or_404(sno)


    db.session.delete(todo)

    db.session.commit()


    flash(
        "Todo deleted!",
        "warning"
    )


    return redirect(
        url_for("home")
    )



if __name__ == "__main__":

    with app.app_context():
        db.create_all()


    app.run(
        debug=True,
        port=7000
    )