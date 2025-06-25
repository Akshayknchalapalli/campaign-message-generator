import google.generativeai as genai
import os
from typing import Optional, List
from dotenv import load_dotenv

load_dotenv()

class GoogleAIService:
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY environment variable is required")
        
        # Add debugging information
        print(f"Initializing Google AI with API key: {self.api_key[:10]}...")
        
        try:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-2.5-flash')
            
            # Test the connection with a simple request
            test_response = self.model.generate_content("Hello")
            print("✅ Google AI service initialized successfully!")
            
        except Exception as e:
            print(f"❌ Failed to initialize Google AI service: {e}")
            raise e
        
    def generate_campaign_message(self, prompt: str, industry: Optional[str] = None, 
                                 target_audience: Optional[str] = None, 
                                 tone: Optional[str] = None) -> str:
        """
        Generate a smart campaign message using Google's Generative AI
        
        Args:
            prompt: The main prompt for the campaign message
            industry: The industry context (e.g., real estate, e-commerce, etc.)
            target_audience: The target audience description
            tone: The desired tone (e.g., professional, friendly, urgent, etc.)
        """
        
        # Build a comprehensive prompt for better results
        system_prompt = f"""
        You are an expert marketing copywriter specializing in creating compelling campaign messages.
        
        Create a persuasive and engaging campaign message based on the following requirements:
        
        Main Prompt: {prompt}
        Industry: {industry or 'General'}
        Target Audience: {target_audience or 'General consumers'}
        Tone: {tone or 'Professional and engaging'}
        
        Requirements:
        1. Keep the message concise but impactful (50-150 words)
        2. Include a clear call-to-action
        3. Use persuasive language that resonates with the target audience
        4. Maintain the specified tone throughout
        5. Focus on benefits and value proposition
        6. Make it memorable and shareable
        
        Return only the campaign message without any additional formatting or explanations.
        """
        
        try:
            response = self.model.generate_content(system_prompt)
            return response.text.strip()
        except Exception as e:
            error_msg = f"Error generating message: {str(e)}"
            print(f"❌ {error_msg}")
            return error_msg
    
    def generate_multiple_variations(self, prompt: str, count: int = 3, 
                                   industry: Optional[str] = None,
                                   target_audience: Optional[str] = None,
                                   tone: Optional[str] = None) -> List[str]:
        """
        Generate multiple variations of a campaign message
        """
        variations = []
        for i in range(count):
            variation_prompt = f"{prompt} (Variation {i+1})"
            message = self.generate_campaign_message(
                variation_prompt, industry, target_audience, tone
            )
            variations.append(message)
        return variations
    
    def analyze_campaign_effectiveness(self, message: str) -> dict:
        """
        Analyze the effectiveness of a campaign message
        """
        analysis_prompt = f"""
        Analyze the following campaign message for effectiveness:
        
        "{message}"
        
        Provide a brief analysis covering:
        1. Clarity and readability
        2. Emotional appeal
        3. Call-to-action strength
        4. Target audience alignment
        5. Overall persuasiveness
        
        Rate each aspect from 1-10 and provide a brief explanation.
        """
        
        try:
            response = self.model.generate_content(analysis_prompt)
            return {
                "message": message,
                "analysis": response.text.strip()
            }
        except Exception as e:
            return {
                "message": message,
                "analysis": f"Error analyzing message: {str(e)}"
            } 