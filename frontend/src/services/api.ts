const API_BASE = "http://localhost:8000/api/v1";

export async function fetchApi(endpoint: string) {
  try {
    const res = await fetch(`${API_BASE}${endpoint}`);
    if (!res.ok) throw new Error(`Status ${res.status}`);
    return await res.json();
  } catch (e) {
    console.warn("API fallback for", endpoint, e);
    return null;
  }
}
