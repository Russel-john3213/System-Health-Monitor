# Write a comment instructing it to import your chosen framework
# Import FastAPI and datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

# Write a comment to initialize the application
# Initialize the FastAPI application
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)

# Write a comment to create a GET route at /api/health
# Create a GET route at /api/health
@app.get("/api/health")
def get_health():
    # Write a comment inside that route to return a dictionary with a "status" message and the current time
    # Return a dictionary with a status message and the current timestamp
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }