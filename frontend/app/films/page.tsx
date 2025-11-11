import Link from "next/link"
import { api } from "@/lib/api"


interface Film { id: number; title: string; description?: string; runtime_min?: number; thumbnail_url?: string }


export default async function FilmsPage() {
const films = await api<Film[]>("/api/films")
return (
<main className="p-6 grid gap-4">
<h2 className="text-2xl font-semibold">Films</h2>
<section className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
{films.map(f => (
<article key={f.id} className="border border-white/10 rounded-lg p-4 bg-white/5">
<h3 className="font-semibold">{f.title}</h3>
<p className="text-sm opacity-80">{f.description || "No description"}</p>
<p className="text-xs opacity-60 mt-1">Runtime: {f.runtime_min || "TBD"} min</p>
<Link className="underline mt-2 inline-block" href={`#`}>Play</Link>
</article>
))}
</section>
</main>
)
}
