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
      <h1>Task Scheduler</h1>
      <TaskForm onTaskCreated={handleTaskCreated} />
      <TaskList refreshTrigger={refreshTrigger} />
    </div>
  );
};

export default App;



