# 🚀 One2N SRE Bootcamp

This repository is part of the **One2N SRE Bootcamp journey**, where I am learning how to build, containerize, and deploy production-ready backend systems step by step.

---

# 📌 Milestone 1 — REST API Development (Local Setup)

## 📖 Overview
In this milestone, I built a simple REST API for managing **student data** and tested it locally.

The goal was to understand:
- How backend APIs are structured
- How CRUD operations work
- How FastAPI handles requests and responses

---

## ⚙️ Tech Stack
- Python 3.12
- FastAPI
- Uvicorn
- Swagger UI

---

## 📁 Project Structure


app/
├── main.py
├── routers/
├── models/
├── schemas/
├── database/


---

## 🚀 How to Run Locally

### 1. Clone Repository
```bash
git clone https://github.com/VamshiAdep/one2n-sre-service.git
cd one2n-sre-service
2. Create Virtual Environment
python -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Start Server
uvicorn app.main:app --reload
🌐 API Documentation

Swagger UI:

http://127.0.0.1:8000/docs
📌 API Endpoints
Method	Endpoint	Description
GET	/students	Get all students
GET	/students/{id}	Get student by ID
POST	/students	Create student
PUT	/students/{id}	Update student
DELETE	/students/{id}	Delete student
🐳 Milestone 2 — Containerize REST API (Docker)
📖 Overview

In this milestone, I containerized the REST API using Docker to make it portable and production-ready.

This helped me understand:

Docker image creation
Multi-stage builds
Environment variable injection
Running applications inside containers
⚙️ Tech Stack
Docker
Python 3.12
FastAPI
Uvicorn
🐳 Docker Image Details
Image Name: one2n-api
Version: 1.0.0
Type: Multi-stage build
Base Image: python:3.12-slim
🚀 How to Run Using Docker
1. Build Docker Image
docker build -t one2n-api:1.0.0 .
2. Run Container
docker run -d -p 8000:8000 \
-e APP_ENV=dev \
-e DATABASE_URL=your_database_url \
one2n-api:1.0.0
3. Check Running Containers
docker ps
4. View Logs
docker logs <container_id>
🌐 API Access (Inside Docker)

Swagger UI:

http://localhost:8000/docs
⚙️ Makefile Commands

To simplify operations:

make build     # Build Docker image
make run       # Run container
make logs      # View logs
make stop      # Stop container
make clean     # Remove containers + images
