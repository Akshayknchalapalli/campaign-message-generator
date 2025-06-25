from app.utils.google_ai_service import GoogleAIService
from typing import Optional, List, Dict

class MessageGenerator:
    def __init__(self):
        """Initialize the message generator with Google AI service"""
        try:
            self.google_ai_service = GoogleAIService()
            self.is_initialized = True
        except Exception as e:
            print(f"Failed to initialize Google AI service: {e}")
            self.is_initialized = False

    def generate_message(self, prompt: str, industry: Optional[str] = None, 
                        target_audience: Optional[str] = None, 
                        tone: Optional[str] = None) -> str:
        """
        Generate a smart campaign message using Google AI
        
        Args:
            prompt: The main prompt for the campaign message
            industry: The industry context (e.g., real estate, e-commerce, etc.)
            target_audience: The target audience description
            tone: The desired tone (e.g., professional, friendly, urgent, etc.)
        """
        if not self.is_initialized:
            return "Error: Google AI service not initialized. Please check your API key."
        
        return self.google_ai_service.generate_campaign_message(
            prompt, industry, target_audience, tone
        )

    def generate_multiple_variations(self, prompt: str, count: int = 3,
                                   industry: Optional[str] = None,
                                   target_audience: Optional[str] = None,
                                   tone: Optional[str] = None) -> List[str]:
        """
        Generate multiple variations of a campaign message
        """
        if not self.is_initialized:
            return ["Error: Google AI service not initialized. Please check your API key."]
        
        return self.google_ai_service.generate_multiple_variations(
            prompt, count, industry, target_audience, tone
        )

    def analyze_message(self, message: str) -> Dict[str, str]:
        """
        Analyze the effectiveness of a campaign message
        """
        if not self.is_initialized:
            return {
                "message": message,
                "analysis": "Error: Google AI service not initialized. Please check your API key."
            }
        
        return self.google_ai_service.analyze_campaign_effectiveness(message)

    def get_service_status(self) -> Dict[str, bool]:
        """
        Get the status of the Google AI service
        """
        return {
            "is_initialized": self.is_initialized,
            "api_available": self.is_initialized
        }


