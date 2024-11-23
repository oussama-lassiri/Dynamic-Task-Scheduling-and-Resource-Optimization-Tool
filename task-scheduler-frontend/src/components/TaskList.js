import React, { useEffect, useState } from 'react';
import API from '../api';

const TaskList = ({ refreshTrigger }) => {
    const [tasks, setTasks] = useState([]);
  
    const fetchTasks = async () => {
      try {
        const response = await API.get('/get-tasks');
        setTasks(response.data);
      } catch (error) {
        console.error('Error fetching tasks:', error);
      }
    };
  
    useEffect(() => {
      fetchTasks();
    }, [refreshTrigger]);
  
    return (
      <div>
        <h3>Task List</h3>
        <ul>
          {tasks.map((task) => (
            <li key={task.id}>
              <strong>{task.title}</strong>: {task.description} - {task.status}
            </li>
          ))}
        </ul>
      </div>
    );
  };
  

export default TaskList;
