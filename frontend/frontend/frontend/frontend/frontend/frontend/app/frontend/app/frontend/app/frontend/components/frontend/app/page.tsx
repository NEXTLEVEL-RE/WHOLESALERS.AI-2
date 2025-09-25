import ThemeToggle from "@/components/theme-toggle";

const API = process.env.NEXT_PUBLIC_GPT_CORE_URL ?? "http://127.0.0.1:8000";

export default function Home() {
  return (
    <main className="min-h-screen p-6">
      <header className="flex items-center justify-between">
        <h1 className="text-2xl font-bold">
          Wholesalers.<span className="text-indigo-500">AI</span>
        </h1>
        <ThemeToggle />
      </header>

      <section className="mt-16 max-w-2xl">
        <h2 className="text-4xl font-extrabold">Your AI wholesale OS</h2>
        <p className="mt-3 text-lg text-[color:var(--muted)]">
          Frontend (Next.js) + Backend (FastAPI). Set <code>NEXT_PUBLIC_GPT_CORE_URL</code> to your API.
        </p>

        <div className="mt-6">
          <a
            href={`${API}/healthz`}
            className="inline-block rounded-md bg-indigo-600 px-5 py-3 font-semibold text-white hover:bg-indigo-500"
          >
            Check API Health
          </a>
        </div>
      </section>
    </main>
  );
}
