import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';

function App() {
  const [inventory, setInventory] = useState([]);
  const [history, setHistory] = useState([]);
  const [query, setQuery] = useState('');

  useEffect(() => {
    // Example: load inventory for a steamid stored in localStorage
    const steamid = localStorage.getItem('steamid');
    if (steamid) {
      axios.get(`/inventory?steamid=${steamid}`).then((res) => {
        setInventory(res.data);
      });
    }
  }, []);

  const searchItem = () => {
    axios.get(`/prices?item=${query}`).then((res) => {
      setHistory(res.data);
    });
  };

  const chartData = {
    labels: history.map((h) => new Date(h.created_at).toLocaleDateString()),
    datasets: [
      {
        label: 'Price',
        data: history.map((h) => h.price),
        borderColor: 'rgba(75,192,192,1)',
        fill: false,
      },
    ],
  };

  return (
    <div>
      <h1>Estordia</h1>
      <div>
        <input value={query} onChange={(e) => setQuery(e.target.value)} />
        <button onClick={searchItem}>Search</button>
      </div>
      <h2>Inventory</h2>
      <ul>
        {inventory.map((item) => (
          <li key={item.appid}>{item.name}</li>
        ))}
      </ul>
      <div style={{ width: '600px', height: '300px' }}>
        <Line data={chartData} />
      </div>
    </div>
  );
}

export default App;
