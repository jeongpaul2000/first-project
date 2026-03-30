"use client";

import { useState } from "react";
import SearchResults from "./SearchResults";

export default function SearchBox() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<string[]>([]);

  const handleSearch = async () => {
    const res = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
    const data = await res.json();
    setResults(data);
  };

  return (
    <div>
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search fruit..."
      />
      <button onClick={handleSearch}>Search</button>

      <SearchResults results={results} />
    </div>
  );
}