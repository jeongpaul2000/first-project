export async function GET(req: Request) {
  const { searchParams } = new URL(req.url);
  const query = searchParams.get("q")?.toLowerCase() || "";

  // fake "database"
  const data = ["apple", "banana", "grape", "orange", "pineapple"];

  const results = data.filter(item =>
    item.toLowerCase().includes(query)
  );

  return Response.json(results);
}