import { useState } from 'react'
import './App.css'

function App() {
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");

  const handleSubmit = async () => {
    try {
      // Convert comma-separated string to number array
      const values = input
        .split(",")
        .map((v) => parseFloat(v.trim()))
        .filter((v) => !isNaN(v));

      const response = await fetch("http://127.0.0.1:8000/test", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ values }),
      });

      const data = await response.json();

      // Show everything as one text block
      setOutput(JSON.stringify(data, null, 2));
    } catch (e) {
      setOutput("Error calling backend");
    }
  };

  return (
    <div style={{ padding: 40 }}>
      <h1>Data Processor</h1>

      <input
        type="text"
        placeholder="Enter numbers separated by commas"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        style={{ width: 300, marginRight: 10 }}
      />

      <button onClick={handleSubmit}>Submit</button>

      <div style={{ marginTop: 20 }}>
        <p>
          Mean: {output}
        </p>
      </div>
    </div>
  );
}

export default App;
