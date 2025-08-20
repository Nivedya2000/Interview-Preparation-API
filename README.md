# 📝 Interview Preparation API

A Django REST API to help candidates prepare for technical interviews.  
It supports **user registration, JWT authentication, admin-managed categorized questions**, and **RESTful APIs** to manage interview questions.

---

## 🚀 Features
- 🔐 **User Registration & Login** with JWT Authentication  
- 🛠 **Admin Panel** for managing questions  
- 📡 **REST API Endpoints** to list, add, and retrieve questions  
- 🏷 **Categorization** of questions (Python, SQL, Django, Other)  
- ⚡ Built using **Django REST Framework (DRF)**  

---

## 🛠 Tech Stack
- **Python 3.x**
- **Django 4.x**
- **Django REST Framework**
- **SQLite** (default) / **PostgreSQL** (optional)
- **JWT Authentication** (`djangorestframework-simplejwt`)

---

## 📂 Project Structure
```
interview-api/
├── interview_api/         # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── api/                   # Main API app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── .env                   # Environment variables (not committed)
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR-USERNAME/interview-prep-api.git
cd interview-prep-api
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variables
Create a `.env` file:
```env
SECRET_KEY=your_secret_key_here
DEBUG=True
```

### 5️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create Superuser
```bash
python manage.py createsuperuser
```

### 7️⃣ Run the Server
```bash
python manage.py runserver
```
API runs at: **http://127.0.0.1:8000/**

---

## 📡 API Endpoints

| Method | Endpoint                 | Description                        | Auth Required |
|--------|---------------------------|------------------------------------|---------------|
| POST   | `/api/register/`         | Register a new user                | ❌ No          |
| POST   | `/api/token/`            | Obtain JWT token                   | ❌ No          |
| GET    | `/api/questions/`        | List all questions                 | ❌ No          |
| POST   | `/api/questions/`        | Create new question (Admin only)   | ✅ Yes         |
| GET    | `/api/questions/<id>/`   | Retrieve question by ID            | ❌ No          |

---

## 🔐 Authentication
This project uses **JWT Authentication**.  
To access protected routes:
1. Obtain a token via `/api/token/`
2. Add it to request headers:
   ```
   Authorization: Bearer <your_access_token>
   ```

---

## 🧪 Testing
- Use **Postman / curl** to test endpoints  
- Example: Register a user
```bash
curl -X POST http://127.0.0.1:8000/api/register/ -H "Content-Type: application/json" -d '{"username": "testuser", "email": "test@example.com", "password": "testpass123"}'
```

---

## 📌 Notes
- Default database: **SQLite**  
- For PostgreSQL, update `DATABASES` in `settings.py`  
- Keep your `.env` file safe and **never commit it**  
- License: **MIT** (free to use and modify)

---

## 🤝 Contributing
Contributions are welcome!  
1. Fork the repo  
2. Create a new branch (`feature-xyz`)  
3. Commit changes and push  
4. Open a Pull Request  

---

## 📜 License
This project is licensed under the **MIT License**.
# Interview-Preparation-API
# Interview-Preparation-API
# Interview-Preparation-API
