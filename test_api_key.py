#!/usr/bin/env python3
"""
Simple test script to verify Google AI API key functionality
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv

def test_google_api_key():
    """Test the Google AI API key"""
    
    # Load environment variables
    load_dotenv()
    
    # Get API key
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        print("❌ No API key found in .env file")
        return False
    
    print(f"🔑 Found API key: {api_key[:10]}...")
    
    try:
        # Configure the API
        genai.configure(api_key=api_key)
        
        # Create a model instance
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Test with a simple prompt
        print("🧪 Testing API with simple prompt...")
        response = model.generate_content("Say 'Hello, API is working!'")
        
        print("✅ API Key is working!")
        print(f"📝 Response: {response.text}")
        return True
        
    except Exception as e:
        print(f"❌ API Key test failed: {e}")
        
        # Provide specific troubleshooting steps
        if "API_KEY_INVALID" in str(e):
            print("\n🔧 Troubleshooting steps for API_KEY_INVALID:")
            print("1. Go to https://makersuite.google.com/app/apikey")
            print("2. Check if your API key has restrictions")
            print("3. Make sure 'Generative Language API' is enabled")
            print("4. Verify billing is set up at https://console.cloud.google.com/billing")
            print("5. Try creating a new API key")
        
        elif "quota" in str(e).lower():
            print("\n🔧 Troubleshooting steps for quota issues:")
            print("1. Check your billing status")
            print("2. Verify API quotas at https://console.cloud.google.com/apis/api/generativelanguage.googleapis.com/quotas")
        
        return False

if __name__ == "__main__":
    print("🚀 Testing Google AI API Key...")
    test_google_api_key() 