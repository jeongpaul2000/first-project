type SearchResultsProps = {
  results: string[];
};

export default function SearchResults({ results }: SearchResultsProps) {
  return (
    <ul>
      {results.map((item, index) => (
        <li key={index}>{item}</li>
      ))}
    </ul>
  );
}