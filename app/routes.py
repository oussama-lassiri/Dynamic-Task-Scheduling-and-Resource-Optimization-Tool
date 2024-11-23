from flask import Blueprint, request, jsonify
from .models import db, User, Task

main = Blueprint('main', __name__)

@main.route('/create-task', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(title=data['title'], description=data.get('description', ''), status='Pending')
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"id": new_task.id, "title": new_task.title, "description": new_task.description, "status": new_task.status}), 201


@main.route('/get-tasks', methods= ['GET'])
def get_task():
    tasks = Task.query.all()
    return jsonify([{"id": task.id, "title": task.title, "status": task.status}for task in tasks])