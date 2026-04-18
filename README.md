# One2N SRE Bootcamp - Milestone 1

This project is part of the One2N SRE Bootcamp journey.  
In this milestone, I have built a simple REST API and tested it locally before moving towards production concepts.

---

## 📌 About Project

This is a basic REST API application for managing student data.  
It supports basic CRUD operations like creating, reading, updating, and deleting student records.

I built this to understand how APIs work and how backend services are structured.

---

## ⚙️ Tech Stack

- Python
- FastAPI
- Uvicorn
- Swagger UI for testing APIs

---

## 📁 Project Structure
app/
├── main.py
├── routers/
├── models/
├── schemas/
├── database/

## 🚀 How to run this project

### 1. Clone the repository
```bash
git clone https://github.com/VamshiAdep/one2n-sre-service.git
cd one2n-sre-service

2. Create virtual environment
python -m venv venv
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Run the server
uvicorn app.main:app --reload

🌐 API Testing

After running the server, open:

Swagger UI:
http://127.0.0.1:8000/docs

📌 API Endpoints
Method	Endpoint	Description
GET	/students	Get all students
GET	/students/{id}	Get student by id
POST	/students	Create new student
PUT	/students/{id}	Update student
DELETE	/students/{id}	Delete student
