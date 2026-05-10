# Northwind Full-Stack

A full-stack e-commerce demo built on the classic Northwind dataset.

- **Frontend** — React, Redux, React Router, Reactstrap
- **Backend** — Django REST Framework, PostgreSQL, Docker

---

## Project Structure

```
northwind-fullstack/
├── frontend/   # React + Redux SPA
└── backend/    # Django REST API + PostgreSQL
```

---

## Backend

The backend runs entirely via Docker Compose — no local Python setup needed.

### Setup

```bash
cd backend
cp .env.example .env   # fill in your values
docker compose up --build
```

The API will be available at `http://localhost:3001`.  
On first start, migrations and seed data run automatically.

### Stack

| Layer    | Technology              |
|----------|-------------------------|
| API      | Django 6 + DRF          |
| Database | PostgreSQL 16 (Docker)  |
| Auth     | Session-based           |

---

## Frontend

### Setup

```bash
cd frontend
npm install
npm start
```

The app will be available at `http://localhost:3000`.

> Make sure the backend is running first.

### Stack

| Layer         | Technology             |
|---------------|------------------------|
| UI            | React 18 + Reactstrap  |
| State         | Redux                  |
| Routing       | React Router           |
| HTTP          | Axios                  |

---

## Features

- Category and product listing
- Product detail page
- Add / update products
- Shopping cart with Redux state management
