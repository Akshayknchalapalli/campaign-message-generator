
from fastapi import APIRouter
from app.models.message_generator import MessageGenerator
from app.schemas.message import MessageRequest, MessageResponse

router = APIRouter()
message_generator = MessageGenerator()

@router.post("/generate-message", response_model=MessageResponse)
async def generate_message(request: MessageRequest):
    prompt = request.prompt
    print("prompt", prompt)
    message = message_generator.generate_message(prompt)
    return MessageResponse(message=message)