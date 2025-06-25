from fastapi import APIRouter
from app.models.message_generator import MessageGenerator
from app.schemas.message import (
    MessageRequest, MessageResponse, 
    MultipleMessagesRequest, MultipleMessagesResponse,
    MessageAnalysisRequest, MessageAnalysisResponse,
    ServiceStatusResponse
)

router = APIRouter()
message_generator = MessageGenerator()

@router.post("/generate-message", response_model=MessageResponse)
async def generate_message(request: MessageRequest):
    """Generate a single campaign message using Google AI"""
    message = message_generator.generate_message(
        prompt=request.prompt,
        industry=request.industry,
        target_audience=request.target_audience,
        tone=request.tone
    )
    return MessageResponse(message=message)

@router.post("/generate-multiple-messages", response_model=MultipleMessagesResponse)
async def generate_multiple_messages(request: MultipleMessagesRequest):
    """Generate multiple variations of a campaign message"""
    messages = message_generator.generate_multiple_variations(
        prompt=request.prompt,
        count=request.count,
        industry=request.industry,
        target_audience=request.target_audience,
        tone=request.tone
    )
    return MultipleMessagesResponse(messages=messages)

@router.post("/analyze-message", response_model=MessageAnalysisResponse)
async def analyze_message(request: MessageAnalysisRequest):
    """Analyze the effectiveness of a campaign message"""
    analysis_result = message_generator.analyze_message(request.message)
    return MessageAnalysisResponse(
        message=analysis_result["message"],
        analysis=analysis_result["analysis"]
    )

@router.get("/service-status", response_model=ServiceStatusResponse)
async def get_service_status():
    """Get the status of the Google AI service"""
    status = message_generator.get_service_status()
    return ServiceStatusResponse(**status)