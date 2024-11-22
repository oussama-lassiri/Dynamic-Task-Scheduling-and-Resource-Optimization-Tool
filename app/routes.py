from flask import Blueprint, request, jsonify
from .models import db, User, Task

main = Blueprint('main', __name__)

@main.route('/create-task', methods= ['POST'])
def create_task():
    data = request.json
    task = Task(title= data['title'], description = data['description'])
    db.session.add(task)
    db.session.commit()
    return jsonify(("Message: Task has been created successfully!")), 201

@main.route('/get-task', methods= ['GET'])
def get_task():
    tasks = Task.query.all()
    return jsonify([{"id": task.id, "title": task.title, "status": task.status}for task in tasks])