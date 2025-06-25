from fastapi import FastAPI
from app.api.endpoints import router
from app.models.message_generator import MessageGenerator

app = FastAPI(title="Campaign Message Generator", 
              description="Smart campaign message generation using Google AI",
              version="2.0.0")

# Initialize the message generator
message_generator = MessageGenerator()
app.include_router(router)

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Campaign Message Generator API",
        "version": "2.0.0",
        "description": "Smart campaign message generation using Google AI",
        "endpoints": {
            "generate_message": "/generate-message",
            "generate_multiple_messages": "/generate-multiple-messages", 
            "analyze_message": "/analyze-message",
            "service_status": "/service-status",
            "docs": "/docs"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    status = message_generator.get_service_status()
    return {
        "status": "healthy" if status["is_initialized"] else "unhealthy",
        "google_ai_available": status["api_available"]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)