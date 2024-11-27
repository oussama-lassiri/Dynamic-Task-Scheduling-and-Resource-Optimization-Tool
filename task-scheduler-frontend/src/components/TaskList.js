import React, { useEffect, useState } from 'react';
import API from '../api';
import { Trash2, CheckSquare, XSquare } from 'lucide-react';

const TaskList = ({ onTaskUpdate  }) => {
    const [tasks, setTasks] = useState([]);
    const [filter, setFilter] = useState('All');
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
  
    //loading all the Tasks 
    const fetchTasks = async () => {
      try {
        setLoading(true);
        const response = await API.get(`/get-tasks`);
        setTasks(response.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching tasks:', error);
        setError('Failed to load tasks');
        setLoading(false);
      }
    };
  
    useEffect(() => {
      fetchTasks();
    }, []);

    // Changing the status of a task
    const toggleTaskStatus = async(id, currentStatus) => {
      try {
        const response = await API.patch(
          `/update-task/${id}`,
          { status: currentStatus === 'Pending' ? 'Completed' : 'Pending' },
          {
            headers: {
              'Content-Type': 'application/json', 
            },
          }
        );
        console.log('Task updated', response.data);
        fetchTasks();
      }catch (error) {
        console.error('error updating the task', error);
      }
    };

    const getFilteredTasks = () =>{
      return tasks.filter((task) => {
        if (filter === 'All') return true;

        const taskStatus = task.status.trim().toLowerCase();
        const filterStatus = filter.trim().toLowerCase();

        return taskStatus = filterStatus;
      }
    )
    }
    
    const deleteTask = async (id) => {
      try {
        await API.delete(`/delete-task/${id}`);
        console.log('Task deleted');
        setTasks((prevTasks) => prevTasks.filter((task) => task.id !== id));
      } catch(error) {
        console.error('Error deleting task:', error);
        // setError("Failed to delete task");
      }
    }

    useEffect(() => {
      fetchTasks();
    }, []);
    

    if (loading) return <p className="text-gray-500">Laoding tasks...</p>;
    if (error) return <p className="text-red-500">{error}</p>
  
    return (
      <div className='p-4'>
        <h3 className="text-xl font-bold mb-4">Task List</h3>

        <div className="mb-4">
          <label htmlFor="filter" className="mr-2">Filter:</label>
          <select 
            id="filter"
            value={filter} 
            onChange={(e) => setFilter(e.target.value)}
            className="border rounded p-1"
          >
            <option value="All">All</option>
            <option value="Pending">Pending</option>
            <option value="Completed">Completed</option>
          </select>
        </div>

        {getFilteredTasks().length === 0 ? (<p className='text-gray-500'>No tasks available!</p>) : (
          <ul className='space-y-2'>
            {getFilteredTasks().map((task) => (
              <li 
                key={task.id}
                className={`
                  flex justify-between items-center p-3 border rounded
                  ${task.status === 'Completed' ? 'bg-green-50' : 'bg-white'}
                  `}
                >
              <div>
                <strong className="mr-2">{task.title}</strong>
                <span className="text-gray-600">{task.description}</span>
                <span 
                  className={`
                    ml-2 px-2 py-1 rounded text-xs 
                    ${task.status === 'Completed' ? 'bg-green-200' : 'bg-yellow-200'}
                  `}
                >
                  {task.status}
                </span>
              </div>
              <div>
                <button 
                  onClick={() => toggleTaskStatus(task.id, task.status)}
                  className={`
                    p-2 rounded 
                    ${task.status === 'Pending' 
                      ? 'bg-green-100 hover:bg-green-200' 
                      : 'bg-yellow-100 hover:bg-yellow-200'}
                  `}
                  title={task.status === 'Pending' ? 'Mark as Completed' : 'Mark as Pending'}
                  >
                {task.status === 'Pending' ? 'Mark as completed' : 'Mark as pending'}
                </button>
                <button 
                  onClick={() => deleteTask(task.id)}
                  className='p-2 rounded bg-red-100 hover: bg-red-200'
                  title="Delete Task"
                >
                <Trash2 />
                </button>
              </div>
              
              </li>
            ))}
          </ul>)}
      </div>
    );
  };
  

export default TaskList;
