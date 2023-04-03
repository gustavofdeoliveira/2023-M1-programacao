import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Header from './components/header/header';
import ContainerCard from './components/container-card/container-card';
import reportWebVitals from './reportWebVitals';
import Table from './components/table/table';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(

  <React.StrictMode>
    <Header />
    <Table />
    <ContainerCard />
  </React.StrictMode>
);

reportWebVitals();
