"use client";

import { useState } from "react";

export default function Home() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<string[]>([]);

  const handleSearch = async () => {
    const res = await fetch(`http://localhost:8000/search?q=${query}`);
    const data = await res.json();
    setResults(data);
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>My Search App</h1>

      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search fruit..."
      />

      <button onClick={handleSearch}>Search</button>

      <ul>
        {results.map((item, i) => (
          <li key={i}>{item}</li>
        ))}
      </ul>
    </div>
  );
}