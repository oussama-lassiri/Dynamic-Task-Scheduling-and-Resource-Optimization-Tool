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
    return jsonify([{"id": task.id, "title": task.title, "description": task.description, "status": task.status}for task in tasks])

@main.route('/update-task/<int:task_id>', methods=['PATCH', 'OPTIONS'])
def update_task(task_id):
    if request.method == 'OPTIONS':  # Handle preflight request
        return '', 204  # HTTP 204 No Content
    data = request.get_json()
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    task.status = data.get('status', task.status)
    db.session.commit()
    return jsonify({"id": task.id, "title": task.title, "description": task.description, "status": task.status})


@main.route('/delete-task/<int:task_id>', methods=['DELETE', 'OPTIONS'])
def delete_task(task_id):
    if request.method == 'OPTIONS':  # Handle preflight request
        return '', 204  # HTTP 204 No Content
    
    task = Task.query.get(task_id)
    
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    db.session.delete(task)
    db.session.commit()
    
    return jsonify({"message": "Task deleted"})
