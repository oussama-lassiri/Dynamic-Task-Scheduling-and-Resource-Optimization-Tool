import React, { useEffect, useState } from 'react';
import API from '../api';

const TaskList = ({ refreshTrigger }) => {
    const [tasks, setTasks] = useState([]);
  
    const fetchTasks = async () => {
      try {
        const response = await API.get(`/get-tasks`);
        setTasks(response.data);
      } catch (error) {
        console.error('Error fetching tasks:', error);
      }
    };
  
    useEffect(() => {
      fetchTasks();
    }, [refreshTrigger]);

    const toggleTaskStatus = async(id, currentStatus) => {
      try {
        const response = await API.patch(
          `/update-task/${id}`,
          { status: currentStatus === 'Pending' ? 'Completed' : 'Pending' },
          {
            headers: {
              'Content-Type': 'application/json', // Ensure headers are included
            },
          }
        );
        console.log('Task updated', response.data);
        fetchTasks();
      }catch (error) {
        console.error('error updating the task', error);
      }
    };

    const [filter, setFilter] = useState('all');

    const filteredTasks = tasks.filter((task) =>
      filter === 'all' || task.status === filter
    );

    const deleteTask = async (id) => {
      try {
        await API.delete(`/delete=task/${id}`);
        console.log('Task deleted');
        fetchTasks();
      } catch(error) {
        console.error('Error deleting task:', error);
      }
    }
  
    return (
      <div>
        <h3>Task List</h3>
        <select onChange={(e) => setFilter(e.target.value)}>
          <option value="All">All</option>
          <option value="Pending">Pending</option>
          <option value="Completed ">Completed</option>
        </select>
        <ul>
          {tasks.map((task) => (
            <li key={task.id}>
              <strong>{task.title}</strong>: {task.description} - {task.status}
            <button onClick={() => toggleTaskStatus(task.id, task.status)}>
              {task.status === 'Pending' ? 'Mark as completed' : 'mark as pending'}
            </button>
            <button onClick={() => deleteTask(task.id)}>Delete</button>
            </li>
          ))}
        </ul>
      </div>
    );
  };
  

export default TaskList;
