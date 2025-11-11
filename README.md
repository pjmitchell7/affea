# affea
Short Film (After Discussion) Streaming Platform
## What this scaffold is

This scaffold gives me the full foundation of **Affea**, a streaming platform for short films. It sets up a working structure where the frontend, backend, database, and storage all connect properly. From the first clone, I can run everything with Docker and immediately get a working system that lists films and can stream video files securely through AWS S3.

The purpose of this setup is to make sure Affea is **modular, scalable, and legally clean** from the start. Each part has a defined responsibility so nothing becomes tangled later when new features like uploads, recommendations, or monetization are added.

---

## Overall Architecture

User →  Next.js (frontend)
                ↓
     (API request via fetch)
                ↓
      Flask API (backend)
      ↓                ↓
 PostgreSQL       AWS S3 (video files)

The platform is built on four main layers:

### 1. Next.js (Frontend)
- Handles everything the user sees and interacts with.
- Built with React for component-based design and Tailwind for styling.
- Uses server-side rendering so pages load quickly and stay SEO-friendly.
- Communicates with the Flask API using simple `fetch` calls.

**Why:** Next.js is fast, flexible, and production-ready. It gives me a clear way to manage routes and pages while keeping room for growth. Using Tailwind also avoids CSS clutter and speeds up styling as I expand the interface.

---

### 2. Flask API (Backend)
- Acts as the communication bridge between the frontend and data.
- Handles authentication, video listings, watchlists, DMCA intake, and file access.
- Generates short-lived presigned URLs from S3 when users stream a video.
- Can be scaled independently or containerized for cloud deployment.

**Why:** Flask is lightweight and readable, which makes it ideal for building REST APIs without over-engineering. It also integrates easily with PostgreSQL and AWS services. Since it is separate from the frontend, it can evolve on its own timeline and handle internal admin tools or analytics without touching the UI layer.

---

### 3. PostgreSQL (Database)
- Stores persistent data: users, films, watchlists, and system logs.
- Interacts through SQLAlchemy models.
- Comes preconfigured inside Docker for quick local setup.

**Why:** Postgres is reliable, open source, and fits perfectly for relational data. Unlike a NoSQL option, it enforces structure and integrity across tables, which is important for managing film ownership, licensing, and user accounts later. It also scales well if Affea grows beyond the prototype stage.

---

### 4. AWS S3 (Storage)
- Holds all actual video files (trailers, short films, etc.).
- The Flask backend never streams raw data directly. Instead, it requests a **presigned URL** from S3 that expires after a set time, keeping access secure.
- Optionally connects to CloudFront for CDN caching later on.

**Why:** S3 is reliable, globally available, and integrates tightly with Python through `boto3`. Using presigned URLs means the API controls access but never becomes a bottleneck or a bandwidth cost center. This separation is critical for legal protection and cost efficiency in streaming.

---

## How the pieces connect

When a user opens Affea:

1. The **Next.js frontend** loads in the browser and calls the **Flask API** for data.
2. Flask queries **PostgreSQL** for film metadata.
3. If the user plays a film, Flask requests a temporary URL from **S3** for that file.
4. Flask returns the signed link to the browser.
5. The **video player** loads the file directly from S3 through that link.

This design keeps security tight and avoids overloading the backend. Only metadata and tokens travel through Flask, while large video streams go straight from AWS.

---

## What this scaffold includes

- Complete **Next.js and Flask integration** through Docker Compose
- Basic health check endpoint (`/api/health`) to verify backend status
- Film listing and creation endpoints with SQLAlchemy models
- Auth endpoints for registration and login (JWT-based)
- DMCA takedown route placeholder for future legal handling
- S3 service for generating presigned URLs for video streaming
- Tailwind and TypeScript setup for cleaner UI and predictable builds
- Example environment files for backend and frontend to reduce guesswork

---

## Why this structure matters

The biggest reason for separating everything this way is **long-term flexibility**.

- If the frontend needs a redesign, it can deploy independently on Vercel without affecting the API.
- If I want to migrate the backend to AWS, Render, or Railway, it just needs environment variable updates.
- The database is interchangeable between local Postgres, Neon, or RDS.
- S3 can later plug into CloudFront or even a multi-region storage plan without rewriting the app.

This pattern also aligns with real production architecture used by platforms like Vimeo or independent streaming sites. It prepares Affea for content ownership policies, DMCA compliance, and secure delivery of private media files.

---

## Getting started locally

1. Copy the example `.env` files for both backend and frontend.
2. Run `docker compose up --build`.
3. Visit `http://localhost:3000` to confirm the health check and film list.
4. Add a test record in the `films` table with an S3 key to test playback.

From there, I can begin adding admin uploads, watchlists, or seat grid visuals without touching the core system design.

---

## Why this matters to Affea’s mission

Affea’s goal is to be a trustworthy place for independent creators to share their films safely and legally. The architecture supports that vision by separating ownership, access, and delivery. Every piece of data has a controlled path, and that control will become critical when enforcing rights, handling takedowns, or scaling to real viewers.
