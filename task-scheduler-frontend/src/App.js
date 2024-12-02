import './index.css';
import React, { useState } from 'react';
import TaskForm from './components/TaskForm';
import TaskList from './components/TaskList';

const App = () => {
  const [refreshTrigger, setRefreshTrigger] = useState(false);

  const handleTaskCreated = () => {
    setRefreshTrigger(!refreshTrigger);
  };

  return (
    <div>
      <h3 
        className='mb-4 text-3xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl'
      >
        <span 
          className="text-transparent bg-clip-text bg-gradient-to-r to-emerald-600 from-sky-400">
            Task Scheduler
        </span>
      </h3>
      <TaskForm onTaskCreated={handleTaskCreated} />
      <TaskList refreshTrigger={refreshTrigger} />
    </div>
  );
};

export default App;



