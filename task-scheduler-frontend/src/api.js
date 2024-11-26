import axios from 'axios';

const API = axios.create({
  baseURL: 'http://127.0.0.1:5000', // Flask backend URL
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
    // Add any default headers you need
  }
});

export default API;