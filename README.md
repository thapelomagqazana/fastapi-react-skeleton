# FastAPI + React (Vite, TypeScript) + PostgreSQL Skeleton

A **full-stack starter boilerplate** designed to accelerate development with **FastAPI**, **React (Vite + TypeScript)**, and **PostgreSQL**, featuring built-in **JWT Authentication**, **User CRUD**, **Alembic migrations**, and **Dockerized deployment**.

This skeleton serves as a reusable foundation to kickstart scalable and secure web applications with clear modularity and best practices.

---

## 🚀 Tech Stack

| Layer        | Technology                  |
|--------------|-----------------------------|
| Backend     | FastAPI, SQLAlchemy, Alembic, JWT (python-jose), Passlib |
| Frontend    | React, Vite, TypeScript, Axios, React Router |
| Database    | PostgreSQL                  |
| DevOps      | Docker, Docker Compose      |
| Auth        | JWT-based Authentication    |

---

## 🎯 Project Goals

✅ Provide a reusable and extendable full-stack boilerplate.  
✅ Implement common features used in modern web applications:  
   - User registration (Sign Up).  
   - Authentication (Sign In/Sign Out) with JWT.  
   - Protected and authorized routes.  
   - User CRUD operations (Create, Read, Update, Delete).  
✅ Build a modular and scalable backend architecture.  
✅ Deliver a responsive and type-safe frontend with Vite + React.  
✅ Offer out-of-the-box Docker support for easy setup and deployment.  
✅ Auto-manage database migrations using Alembic.  
✅ Seed initial data automatically.  

---

## 📁 Project Structure

```
fastapi-react-skeleton/
├── backend/
│   ├── app/              # FastAPI app (API, DB, Core)
│   ├── alembic/          # Alembic migrations
│   ├── Dockerfile        # Backend Dockerfile
├── frontend/
│   ├── src/              # React + TypeScript app
│   ├── Dockerfile        # (Optional) Frontend Dockerfile
├── docker-compose.yml    # Docker Compose for full-stack
├── README.md             # Project documentation
```

---

## 🏗️ Features

✅ **Backend (FastAPI)**:
- JWT Authentication.
- User CRUD APIs.
- Auth-protected routes.
- Alembic migrations.
- PostgreSQL integration.
- Dockerized service.

✅ **Frontend (React + Vite + TypeScript)**:
- JWT token storage.
- Protected frontend routes.
- Login, Profile, and Home pages.
- API integration with Axios.

✅ **Infrastructure**:
- Multi-container Docker setup.
- PostgreSQL database.
- Seeding initial data on startup.

---

## 🛠️ Getting Started

### 1️⃣ Clone the repo:
```bash
git clone https://github.com/your-username/fastapi-react-skeleton.git
cd fastapi-react-skeleton
```

### 2️⃣ Configure environment variables
Create `.env` files in both `backend/` and `frontend/`.

### 3️⃣ Run with Docker Compose:
```bash
docker-compose up --build
```

### 4️⃣ Access:
- Backend: `http://localhost:8000`
- Frontend: `http://localhost:5173`

---

## 📌 Planned Improvements
- [ ] Add user roles (admin/user).
- [ ] Refresh token support.
- [ ] Email verification on sign-up.
- [ ] CI/CD pipeline with GitHub Actions.
- [ ] Production-ready Docker optimization.

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the project and submit pull requests.

---

## 📝 License

This project is open-source under the [MIT License](LICENSE).

---