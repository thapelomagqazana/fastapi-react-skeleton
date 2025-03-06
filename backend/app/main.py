from fastapi import FastAPI
from .api.endpoints import auth, users
from .db.models import Base
from .db.session import engine

# Create tables (optional during development)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Management API",
    description="""
    ## Overview
    This API handles user authentication and management with full CRUD operations.
    
    ### Features:
    - **User Registration**
    - **User Authentication (JWT)**
    - **Role-based Access (admin/user)**
    - **User Update & Deletion**
    - **Logging with metadata (IP, request ID)**

    ### Authentication:
    - Use the `/auth/signin` endpoint to get your **JWT token**.
    - Add the token to the **Authorize** button in Swagger or include it in your headers like:
      ```
      Authorization: Bearer <your_token>
      ```

    ### Tags:
    - **Authentication**: Sign in and sign out.
    - **Users**: Manage users, only admins can manage others.
    """,
    version="1.0.0",
    contact={
        "name": "Your Team",
        "email": "support@example.com",
        "url": "https://example.com/support",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    }
)

# Routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])
