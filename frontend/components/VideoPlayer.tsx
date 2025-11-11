'use client'
import { useEffect, useState } from 'react'


export default function VideoPlayer({ filmId }: { filmId: number }) {
const [url, setUrl] = useState<string | null>(null)
useEffect(() => {
fetch(`${process.env.NEXT_PUBLIC_API_BASE}/api/films/${filmId}/stream`).then(r => r.json()).then(j => setUrl(j.url))
}, [filmId])
if (!url) return <div>Loading...</div>
return (
<video src={url} controls className="w-full h-auto rounded-lg" />
)
}
