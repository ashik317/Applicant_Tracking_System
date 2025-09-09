# Applicant_Tracking_System

Django REST Framework ভিত্তিক Job Portal / Applicant Tracking System (ATS)।  
Docker Compose দিয়ে PostgreSQL, Redis, Celery, Flower সব একসাথে রান হয়।  

---

## 🚀 Features
- Django 5 + DRF
- JWT Authentication (SimpleJWT)
- PostgreSQL + Redis integration
- Celery worker + Celery Beat + Flower monitoring
- Swagger & ReDoc API Documentation (drf-spectacular)

---

## 🛠 Tech Stack
- **Backend:** Django, DRF, SimpleJWT
- **Database:** PostgreSQL
- **Cache/Broker:** Redis
- **Async:** Celery, Celery Beat
- **Monitoring:** Flower
- **Docs:** drf-spectacular (Swagger + ReDoc)
- **Containerization:** Docker, Docker Compose

---

## ⚙️ Setup (Docker)

```bash
# 1. Clone repo
git clone https://github.com/<your-username>/Applicant_Tracking_System.git
cd Applicant_Tracking_System

# 2. Create .env file
cp .env.example .env

# 3. Build & start
docker compose up -d --build

# 4. Run migrations & create superuser
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
