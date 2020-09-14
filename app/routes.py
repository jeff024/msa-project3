from flask import render_template, request, redirect, url_for, jsonify
from app import app, models, db

Post = models.Post
title = 'My Personal Study NoteBook'

@app.route('/')
def home():
    posts = Post.query.all()
    posts.reverse()
    return render_template("home.html", title=title, posts=posts[:3])

@app.route('/all/')
def all():
    posts = Post.query.all()
    posts.reverse()
    return render_template("home.html", title=title, posts=posts)



@app.route('/post/', methods=['POST'])
def add_item():
    # Get data from form fields title and content
    Title = request.form.get('Title')
    Content = request.form.get('Content')
    
    # Put data into a new post item
    new_post = Post(title=Title, content=Content, author="Jeff")
    
    # Add and commit the changes to the database
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for('home'))

# DELETE (Delete a specific post id)
@app.route('/post/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    
    # Check if post exists
    if (post != None):
        msg = {
            'message': 'Delete successful'
        }
        db.session.delete(post)
        db.session.commit()
        return jsonify(msg), 200
	
    # post does not exist
    msg = {
        'message': 'post not found'
    }
    return jsonify(msg), 204

@app.route('/AboutMe/')
def aboutMe():
    return render_template("aboutMe.html")

# GET / UPDATE ID
@app.route('/post/<int:id>', methods=['GET', 'POST'])
def view_post(id):
    if (request.method == "GET"):
        post = Post.query.filter_by(id=id).first()
        return render_template('detail.html', post=post)
    elif (request.method == "POST"):
        taskId = request.form.get('taskId')
        taskName = request.form.get('taskName')
        taskDescription = request.form.get('taskDescription')

        task = Task.query.filter_by(id=id).first()
        if (task != None):
            task.name = taskName
            task.description = taskDescription
            db.session.add(task)
            db.session.commit()
        return redirect(url_for('index'))