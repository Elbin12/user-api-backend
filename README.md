# User API - DRF Machine Task

A RESTful API for managing users, built with Django and Django REST Framework.

---

## ✅ Features

- Create a new user
- List users with:
  - **Pagination**
  - **Case-insensitive name search** (first name or last name substring match)
  - **Sorting** on any field (e.g., `age`, `first_name`, etc.)
- Retrieve, update, or delete a specific user
- Custom pagination with support for `limit` and `page` query parameters
- Fully tested with Django test framework

---

## 📁 Project Structure

```
user-api-backend/
├── users/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── tests.py
├── backend/  # Project root
│   ├── settings.py
│   ├── urls.py
```

---

## 🛠 Setup

1. Clone the repository:

```bash
git clone https://github.com/Elbin12/user-api-backend.git
cd user-api-backend/
```
2. Set up a virtual environment and activate it:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```
3. Install dependencies:

```bash
pip install -r requirements.txt
```
4. Create .env file in `user-api-backend/` directory:
```env
SECRET_KEY=django-insecure-o3g_&2vrk66g%-xd%d1l%8hucap*%sjf0+!lofh6n6b*v=vrj-

DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=user-backend!
DB_HOST=user-backend-db.cq3sgkm4ui6j.us-east-1.rds.amazonaws.com
DB_PORT=5432
```
5. Start the Django development server:
```bash
python manage.py runserver
```

---

## 🔗 API Endpoints

### 📄 List / Create Users

**URL**: `/api/users/`  
**Methods**: `GET`, `POST`

#### GET: List Users (with optional filters)

Supports:

| Query Param | Description                                          |
|-------------|------------------------------------------------------|
| `page`      | Page number for pagination (default: 1)              |
| `limit`     | Items per page (default: 5)                          |
| `name`      | Search first/last name (substring, case-insensitive) |
| `sort`      | Sort by field, use `-fieldname` for descending       |

✅ **Example**:
```bash
GET /api/users?page=1&limit=10&name=James&sort=-age
```

#### POST: Create User

Required Fields:

- `first_name`
- `last_name`
- `company_name`
- `age`
- `city`
- `state`
- `zip`
- `email`
- `web`

Example request:

```json
{
  "first_name": "Alice",
  "last_name": "Wonderland",
  "company_name": "Tech Co",
  "age": 28,
  "city": "Wonder City",
  "state": "WC",
  "zip": "12345",
  "email": "alice@example.com",
  "web": "http://alice.com"
}
```

---

### 🔍 Retrieve / Update / Delete a User

**URL**: `/api/users/<id>/`  
**Methods**: `GET`, `PUT`, `DELETE`

---

## 🧪 Running Tests

Tests are written using Django’s built-in test framework.

To run tests:

```bash
python manage.py test
```

Tests include:

- Creating a user
- Listing users with pagination, filtering, sorting
- Retrieving a user
- Updating and deleting a user

🔐 The test database is created automatically and destroyed after tests — **no changes are made to your development database**.

---

## 🙋‍♂️ Contact

Created by Elbin  
Feel free to reach out if you have any questions!