# Campaign Message Generator

A smart campaign message generation API powered by Google's Generative AI (Gemini). This application generates compelling, targeted campaign messages based on your prompts, industry context, target audience, and desired tone.

## Features

- **Smart Message Generation**: Uses Google's Gemini AI to create persuasive campaign messages
- **Multiple Variations**: Generate multiple message variations for A/B testing
- **Message Analysis**: Analyze the effectiveness of your campaign messages
- **Industry-Specific**: Tailor messages for specific industries (real estate, e-commerce, etc.)
- **Audience Targeting**: Customize messages for different target audiences
- **Tone Control**: Specify the desired tone (professional, friendly, urgent, etc.)

## Setup

### Prerequisites

- Python 3.8+
- Google AI API key

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd campaign-message-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your Google AI API key:
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a `.env` file in the root directory:
```bash
cp env.example .env
```
   - Edit `.env` and add your API key:
```
GOOGLE_API_KEY=your_actual_api_key_here
```

4. Run the application:
```bash
python -m app.main
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Generate Single Message
```http
POST /generate-message
```

**Request Body:**
```json
{
  "prompt": "Promote our new luxury condos",
  "industry": "real estate",
  "target_audience": "high-income professionals",
  "tone": "professional"
}
```

**Response:**
```json
{
  "message": "Discover luxury living redefined. Our new premium condos offer unparalleled amenities, stunning city views, and exclusive lifestyle experiences designed for discerning professionals. Limited availability - secure your dream home today. Schedule a private viewing and experience the epitome of sophisticated urban living."
}
```

### Generate Multiple Messages
```http
POST /generate-multiple-messages
```

**Request Body:**
```json
{
  "prompt": "Promote our new luxury condos",
  "count": 3,
  "industry": "real estate",
  "target_audience": "high-income professionals",
  "tone": "professional"
}
```

**Response:**
```json
{
  "messages": [
    "Message variation 1...",
    "Message variation 2...",
    "Message variation 3..."
  ]
}
```

### Analyze Message
```http
POST /analyze-message
```

**Request Body:**
```json
{
  "message": "Your campaign message here..."
}
```

**Response:**
```json
{
  "message": "Your campaign message here...",
  "analysis": "Detailed analysis of message effectiveness..."
}
```

### Service Status
```http
GET /service-status
```

**Response:**
```json
{
  "is_initialized": true,
  "api_available": true
}
```

### Health Check
```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "google_ai_available": true
}
```

## API Documentation

Once the server is running, you can access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Usage Examples

### Real Estate Campaign
```bash
curl -X POST "http://localhost:8000/generate-message" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Promote luxury waterfront condos",
    "industry": "real estate",
    "target_audience": "affluent buyers",
    "tone": "luxury"
  }'
```

### E-commerce Campaign
```bash
curl -X POST "http://localhost:8000/generate-message" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Promote summer sale with 50% off",
    "industry": "e-commerce",
    "target_audience": "budget-conscious shoppers",
    "tone": "urgent"
  }'
```

### SaaS Product Launch
```bash
curl -X POST "http://localhost:8000/generate-message" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Launch new project management tool",
    "industry": "technology",
    "target_audience": "small business owners",
    "tone": "friendly"
  }'
```

## Configuration Options

### Supported Industries
- real estate
- e-commerce
- technology
- healthcare
- education
- finance
- hospitality
- automotive
- fashion
- food & beverage

### Supported Tones
- professional
- friendly
- urgent
- luxury
- casual
- formal
- enthusiastic
- calm
- authoritative
- conversational

## Error Handling

The API includes comprehensive error handling:
- Invalid API key
- Network connectivity issues
- Rate limiting
- Invalid request parameters

All errors are returned with appropriate HTTP status codes and descriptive messages.

## Development

### Project Structure
```
app/
├── api/
│   └── endpoints.py          # API route definitions
├── models/
│   └── message_generator.py  # Main message generation logic
├── schemas/
│   └── message.py           # Pydantic models for request/response
├── utils/
│   └── google_ai_service.py # Google AI integration
└── main.py                  # FastAPI application entry point
```

### Adding New Features

1. Update the `GoogleAIService` class in `app/utils/google_ai_service.py`
2. Add new methods to `MessageGenerator` in `app/models/message_generator.py`
3. Create new schemas in `app/schemas/message.py`
4. Add new endpoints in `app/api/endpoints.py`

## License

This project is licensed under the MIT License.

## Support

For issues and questions, please open an issue in the repository. 