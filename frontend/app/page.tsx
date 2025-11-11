import { api } from "@/lib/api"


export default async function Home() {
const health = await api<{ status: string }>("/api/health")
return (
<main className="p-6">
<h1 className="text-3xl font-bold">Affea</h1>
<p className="mt-2">Backend status: {health.status}</p>
</main>
)
}
