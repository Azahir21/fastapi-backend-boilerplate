# FastAPI Backend Boilerplate

A **beginner-friendly**, production-ready RESTful API boilerplate using FastAPI, SQLAlchemy, JWT authentication, and clean architecture patterns.

> 🎯 **Perfect for newcomers** who want to learn modern Python backend development with best practices built-in!

## 🚀 Features

- **🏗️ Clean Architecture**: Easy-to-understand Repository, Service, Controller pattern
- **🔐 JWT Authentication**: Secure login system with user roles (admin/user)
- **📊 Database**: PostgreSQL with SQLAlchemy ORM (no complex migrations!)
- **📚 Auto Documentation**: Interactive API docs that update automatically
- **🔒 Built-in Security**: Password hashing, CORS, input validation
- **📝 Smart Logging**: See what's happening in your app with detailed logs
- **🐳 Docker Ready**: One command to run everything
- **🧪 Testing Setup**: Learn testing with pre-configured examples
- **⚡ High Performance**: Async/await for fast API responses

## 🎓 How This Boilerplate Works

### 📊 Data Flow Explained (For Beginners)

When a user makes a request to your API, here's what happens:

```
1. 📨 Request comes in → 2. 🛡️ Middleware checks → 3. 🎯 Controller receives → 4. 🧠 Service processes → 5. 💾 Repository talks to DB → 6. 📤 Response goes back
```

**Detailed Flow:**

1. **User sends request** (e.g., login with username/password)
2. **Middleware checks** if request is valid and user is authenticated
3. **Controller** receives the request and extracts data
4. **Service** contains your business logic (e.g., "check if password is correct")
5. **Repository** talks to the database (e.g., "find user by username")
6. **Response** goes back through the same chain with success/error message

### 🏗️ Architecture Made Simple

```
📁 Your API Structure:
├── 🎯 routes/          → "What URLs your API responds to"
├── 🎮 controllers/     → "Handles requests and responses"
├── 🧠 services/        → "Your business logic lives here"
├── 💾 repositories/    → "Talks to the database"
├── 📋 schemas/         → "Defines what data looks like"
├── 🗃️ models/          → "Database table definitions"
└── 🛡️ middleware/      → "Security and validation"
```

## 📁 Project Structure

```
fastapi-backend-boilerplate/
├── .env.example                # 🔧 Copy this to .env and add your settings
├── docker-compose.yaml         # 🐳 One-command setup with Docker
├── Makefile                   # 🚀 Simple commands (make dev, make test)
├── requirements.txt           # 📦 All the Python packages you need
└── src/                       # 💻 All your code lives here
    ├── main.py                # 🚪 The entry point - starts your API
    ├── config/                # ⚙️ Settings and database setup
    │   ├── config.py          # 📝 App configuration
    │   └── database.py        # 🗄️ Database connection
    ├── controllers/           # 🎮 Handle HTTP requests
    │   └── auth_controller.py # 🔐 Login/register logic
    ├── services/              # 🧠 Your business logic
    │   └── auth_service.py    # 🔐 Authentication business rules
    ├── repositories/          # 💾 Database operations
    │   └── user_repository.py # 👤 User database operations
    ├── models/                # 🗃️ Database table definitions
    │   └── user.py            # 👤 User table structure
    ├── schemas/               # 📋 Data validation rules
    │   └── auth.py            # 🔐 Login/register data rules
    ├── routes/                # 🛣️ API endpoints
    │   ├── auth.py            # 🔐 /login, /register endpoints
    │   └── admin.py           # 👑 Admin-only endpoints
    └── utils/                 # 🔨 Helper functions
        ├── auth.py            # 🔐 JWT token creation/validation
        ├── logger.py          # 📝 Logging setup
        └── response.py        # 📤 Standardized API responses
```

## 🚀 Getting Started (Step by Step)

### Prerequisites (What You Need First)

- **Python 3.9+** → [Download here](https://python.org)
- **PostgreSQL** → [Download here](https://postgresql.org) OR use Docker (easier!)
- **Git** → [Download here](https://git-scm.com)

### 🎯 Quick Start (Recommended for Beginners)

**Option 1: Docker (Easiest - Everything is set up for you!)**

```bash
# 1. Get the code
git clone https://github.com/Azahir21/fastapi-backend-boilerplate.git
cd fastapi-backend-boilerplate

# 2. Start everything with one command!
make docker-up

# 3. Open your browser and go to:
# http://localhost:8080/swagger (to see your API documentation)
# http://localhost:8080/ping (to test if it works)
```

**Option 2: Local Development (More control)**

```bash
# 1. Get the code
git clone https://github.com/Azahir21/fastapi-backend-boilerplate.git
cd fastapi-backend-boilerplate

# 2. Create a virtual environment (keeps things organized)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install all dependencies
make install

# 4. Set up your environment variables
cp .env.example .env
# Edit .env file with your database details

# 5. Set up the database
make migrate  # Creates all tables
make seed     # Adds sample data (including admin user)

# 6. Start your API server
make dev

# 7. Test it works:
# Open http://localhost:8080/swagger in your browser
```

## ⚙️ Configuration (Environment Variables)

Create a `.env` file and customize these settings:

```bash
# 🗄️ Database Settings (where your data is stored)
DB_HOST=localhost           # Database server location
DB_PORT=5432                # Database port
DB_USER=postgres            # Database username
DB_PASSWORD=postgres        # Database password
DB_NAME=fastapi_boilerplate # Your database name

# 🔐 Security Settings (keep these secret!)
JWT_SECRET=change-this-to-something-very-secret  # Used to encrypt tokens
JWT_EXPIRY_HOURS=72        # How long login tokens last

# 🚀 Server Settings
SERVER_PORT=8080           # What port your API runs on
SERVER_HOST=0.0.0.0        # Server host
SERVER_ENV=development     # development or production

# 👑 Default Admin User (created automatically)
DEFAULT_ADMIN_USERNAME=admin
DEFAULT_ADMIN_EMAIL=admin@example.com
DEFAULT_ADMIN_PASSWORD=admin123

# 📝 Logging
LOG_LEVEL=INFO             # How detailed logs should be
```

## 📚 API Documentation & Testing

### 🌐 Interactive Documentation

Once your server is running, visit these URLs:

- **Swagger UI**: `http://localhost:8080/swagger`
  - 🎮 Interactive API playground - test endpoints directly!
- **ReDoc**: `http://localhost:8080/redoc`
  - 📖 Beautiful, detailed documentation

### 🧪 Quick Test - Is It Working?

```bash
# Test the health check
curl http://localhost:8080/ping

# Expected response:
{"status": "OK", "message": "Server is running", "timestamp": "2025-01-15T10:30:00"}
```

## 🔐 Authentication System (How Login Works)

### 📋 Available Endpoints

| Method | Endpoint                | What It Does            | Need Login? | Need Admin? |
| ------ | ----------------------- | ----------------------- | ----------- | ----------- |
| POST   | `/api/v1/auth/register` | Create new user account | ❌          | ❌          |
| POST   | `/api/v1/auth/login`    | Login and get token     | ❌          | ❌          |
| GET    | `/api/v1/auth/profile`  | Get your user info      | ✅          | ❌          |
| GET    | `/api/v1/admin/test`    | Admin-only test         | ✅          | ✅          |

### 🎯 How to Use the Authentication System

#### 1. 📝 Register a New User

```bash
curl -X POST "http://localhost:8080/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "password123"
  }'
```

**What happens:**

- Password gets encrypted and stored safely
- User account is created with "user" role
- You get a success message

#### 2. 🔑 Login to Get Your Token

```bash
curl -X POST "http://localhost:8080/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "password": "password123"
  }'
```

**Response:**

```json
{
  "status": "success",
  "message": "Login successful",
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer",
    "user": {
      "id": 1,
      "username": "johndoe",
      "email": "john@example.com",
      "role": "user"
    }
  }
}
```

**💡 Save that `access_token` - you'll need it for protected endpoints!**

#### 3. 🔒 Access Protected Endpoints

```bash
curl -X GET "http://localhost:8080/api/v1/auth/profile" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN_HERE"
```

### 👑 Default Admin Account

For testing, there's a pre-created admin account:

- **Username:** `admin`
- **Password:** `admin123`
- **Email:** `admin@example.com`

## 🛠️ Development Commands (Your Toolkit)

```bash
# 🚀 Running the server
make dev                # Start development server (auto-reloads on changes)
make run                # Start production server

# 📦 Dependencies
make install            # Install all Python packages

# 🗄️ Database operations
make migrate            # Create/update database tables
make seed               # Add sample data (including admin user)

# 🧪 Testing & quality
make test               # Run all tests
make lint               # Check code quality
make format             # Auto-format your code
make clean              # Clean up cache files

# 🐳 Docker commands
make docker-build       # Build Docker image
make docker-up          # Start everything with Docker
make docker-down        # Stop Docker containers
make docker-logs        # See what's happening in containers
make docker-shell       # Access container terminal
make docker-clean       # Remove Docker containers and images
```

## 🔄 Working With the Database

### 🗃️ Understanding Models (Database Tables)

Models define what your database tables look like. Here's the User model:

```python
# src/models/user.py
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="user")  # "user" or "admin"
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
```

### 🔧 Simple Migrations (No Alembic Complexity!)

Instead of complex migration tools, this boilerplate uses a simple approach:

1. **Edit your models** in `src/models/`
2. **Add migration logic** in `src/database/migrations.py`:

```python
def migrate():
    """Add your database changes here"""
    try:
        # This creates all tables based on your models
        create_tables()

        # Add custom changes here:
        with engine.connect() as conn:
            # Example: Add new column
            conn.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS phone VARCHAR(20);"))

            # Example: Create index
            conn.execute(text("CREATE INDEX IF NOT EXISTS idx_users_phone ON users(phone);"))

            conn.commit()

    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise
```

3. **Run migrations:**

```bash
make migrate
```

## 📈 Adding New Features (Step-by-Step Guide)

Let's say you want to add a "Posts" feature where users can create blog posts:

### 1. 🗃️ Create the Model (Database Table)

```python
# src/models/post.py
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship
    author = relationship("User", back_populates="posts")
```

### 2. 📋 Create Schemas (Data Validation)

```python
# src/schemas/post.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PostCreate(BaseModel):
    title: str
    content: str

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    author_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
```

### 3. 💾 Create Repository (Database Operations)

```python
# src/repositories/post_repository.py
from sqlalchemy.orm import Session
from src.models.post import Post
from src.schemas.post import PostCreate

class PostRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_post(self, post_data: PostCreate, author_id: int) -> Post:
        post = Post(
            title=post_data.title,
            content=post_data.content,
            author_id=author_id
        )
        self.db.add(post)
        self.db.commit()
        self.db.refresh(post)
        return post

    def get_user_posts(self, author_id: int) -> list[Post]:
        return self.db.query(Post).filter(Post.author_id == author_id).all()
```

### 4. 🧠 Create Service (Business Logic)

```python
# src/services/post_service.py
from src.repositories.post_repository import PostRepository
from src.schemas.post import PostCreate, PostResponse

class PostService:
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    def create_post(self, post_data: PostCreate, author_id: int) -> PostResponse:
        post = self.post_repository.create_post(post_data, author_id)
        return PostResponse.from_orm(post)

    def get_my_posts(self, author_id: int) -> list[PostResponse]:
        posts = self.post_repository.get_user_posts(author_id)
        return [PostResponse.from_orm(post) for post in posts]
```

### 5. 🎮 Create Controller (Handle Requests)

```python
# src/controllers/post_controller.py
from fastapi import Depends, HTTPException, status
from src.services.post_service import PostService
from src.schemas.post import PostCreate, PostResponse
from src.utils.response import success_response

class PostController:
    def __init__(self, post_service: PostService = Depends()):
        self.post_service = post_service

    def create_post(self, post_data: PostCreate, current_user_id: int):
        post = self.post_service.create_post(post_data, current_user_id)
        return success_response(
            data=post,
            message="Post created successfully"
        )

    def get_my_posts(self, current_user_id: int):
        posts = self.post_service.get_my_posts(current_user_id)
        return success_response(
            data=posts,
            message="Posts retrieved successfully"
        )
```

### 6. 🛣️ Create Routes (API Endpoints)

```python
# src/routes/posts.py
from fastapi import APIRouter, Depends
from src.controllers.post_controller import PostController
from src.schemas.post import PostCreate
from src.middleware.auth_middleware import get_current_user

router = APIRouter(prefix="/api/v1/posts", tags=["Posts"])

@router.post("/")
def create_post(
    post_data: PostCreate,
    current_user = Depends(get_current_user),
    controller: PostController = Depends()
):
    return controller.create_post(post_data, current_user.id)

@router.get("/my-posts")
def get_my_posts(
    current_user = Depends(get_current_user),
    controller: PostController = Depends()
):
    return controller.get_my_posts(current_user.id)
```

### 7. 🔌 Register Routes in Main App

```python
# src/main.py (add this)
from src.routes import posts

app.include_router(posts.router)
```

### 8. 🔄 Run Migration

```bash
make migrate  # This will create the posts table
```

Now you have a complete Posts feature! 🎉

## 🧪 Testing Your API

### 🎯 Manual Testing with Swagger

1. **Start your server:** `make dev`
2. **Open Swagger:** `http://localhost:8080/swagger`
3. **Try the endpoints:**
   - Click on an endpoint
   - Click "Try it out"
   - Fill in the data
   - Click "Execute"

### 🤖 Automated Testing

```bash
# Run all tests
make test

# Run specific test file
python -m pytest tests/test_auth.py -v

# Run with coverage report
python -m pytest tests/ --cov=src --cov-report=html
```

**Example test:**

```python
# tests/test_auth.py
def test_register_user(client):
    response = client.post("/api/v1/auth/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "success"
```

## 🚀 Deployment (Going Live)

### 🐳 Docker Deployment (Recommended)

```bash
# 1. Build your application
make docker-build

# 2. Start in production mode
make docker-up

# 3. Check if everything is working
make docker-logs

# 4. Your API is now live at http://your-server:8080
```

### 🖥️ Manual Deployment

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set up production environment
cp .env.example .env
# Edit .env with production settings

# 3. Run migrations
make migrate

# 4. Start production server
make run
```

## 🏗️ Architecture Deep Dive

### 🔄 Request Lifecycle (What Happens When Someone Calls Your API)

```
📨 HTTP Request
     ↓
🛡️ Middleware (Auth, CORS, etc.)
     ↓
🛣️ Route (matches URL to function)
     ↓
🎮 Controller (receives request, calls service)
     ↓
🧠 Service (business logic, calls repository)
     ↓
💾 Repository (database operations)
     ↓
🗄️ Database (PostgreSQL)
     ↓
📤 Response (goes back up the chain)
```

### 🧩 Component Responsibilities

- **🛣️ Routes** → "Which function handles this URL?"
- **🎮 Controllers** → "Extract data from request, call service, format response"
- **🧠 Services** → "Business rules and logic"
- **💾 Repositories** → "How to get/save data from database"
- **📋 Schemas** → "What data is valid?"
- **🗃️ Models** → "Database table structure"
- **🛡️ Middleware** → "Security, logging, error handling"

## 📋 Best Practices & Tips

### ✅ Code Quality Tips

1. **Use Type Hints Everywhere**

   ```python
   def get_user(user_id: int) -> User:
       return db.query(User).filter(User.id == user_id).first()
   ```

2. **Handle Errors Gracefully**

   ```python
   try:
       user = get_user(user_id)
       if not user:
           raise HTTPException(status_code=404, detail="User not found")
   except Exception as e:
       logger.error(f"Error getting user: {e}")
       raise HTTPException(status_code=500, detail="Internal server error")
   ```

3. **Use Async for I/O Operations**
   ```python
   async def create_user(user_data: UserCreate) -> User:
       # Database operations should be async when possible
       return await repository.create_user(user_data)
   ```

### 🔒 Security Best Practices

1. **Never store plain text passwords**
2. **Always validate input data with Pydantic schemas**
3. **Use environment variables for secrets**
4. **Log security events**
5. **Keep JWT secrets secure and rotate them**

### 📈 Performance Tips

1. **Use database indexes for frequently queried fields**
2. **Implement pagination for large datasets**
3. **Use async/await for I/O operations**
4. **Cache frequently accessed data**
5. **Monitor your API performance**

## 🆘 Troubleshooting

### ❌ Common Issues & Solutions

**Problem:** `ModuleNotFoundError: No module named 'src'`
**Solution:** Make sure you're in the project directory and virtual environment is activated

**Problem:** Database connection error
**Solution:** Check your `.env` file has correct database credentials and PostgreSQL is running

**Problem:** JWT token invalid
**Solution:** Check if JWT_SECRET in `.env` matches between token creation and validation

**Problem:** Permission denied errors
**Solution:** Make sure your user has proper database permissions

### 🔍 Debugging Tips

1. **Check the logs:**

   ```bash
   # Local development
   tail -f logs/app.log

   # Docker
   make docker-logs
   ```

2. **Test individual components:**

   ```bash
   # Test database connection
   python -c "from src.config.database import engine; print(engine.execute('SELECT 1').scalar())"

   # Test specific endpoint
   curl -v http://localhost:8080/ping
   ```

3. **Use the debugger:**
   ```python
   import pdb; pdb.set_trace()  # Add this line where you want to debug
   ```

## 🤝 Contributing

Want to improve this boilerplate? Here's how:

1. **Fork the repository** on GitHub
2. **Create a feature branch:** `git checkout -b feature/amazing-feature`
3. **Make your changes** and test them
4. **Commit your changes:** `git commit -m 'Add some amazing feature'`
5. **Push to the branch:** `git push origin feature/amazing-feature`
6. **Open a Pull Request** and describe what you've added

### 🐛 Found a Bug?

1. Check if the issue already exists
2. Create a new issue with:
   - Clear description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - Your environment details

## 📄 License

This project is licensed under the MIT License - feel free to use it for learning or commercial projects!

## 🙏 Acknowledgments

This boilerplate is built on top of amazing open-source projects:

- **[FastAPI](https://fastapi.tiangolo.com/)** → The web framework that makes APIs fast and easy
- **[SQLAlchemy](https://www.sqlalchemy.org/)** → Powerful Python SQL toolkit and ORM
- **[Pydantic](https://pydantic-docs.helpmanual.io/)** → Data validation using Python type hints
- **[Loguru](https://loguru.readthedocs.io/)** → Makes Python logging simple and beautiful
- **[Uvicorn](https://www.uvicorn.org/)** → Lightning-fast ASGI server
- **[Docker](https://www.docker.com/)** → Makes deployment and development consistent

---

**🎉 Happy coding! If this boilerplate helped you, consider giving it a star ⭐**

**💬 Questions? Open an issue or discussion - we're here to help!**
