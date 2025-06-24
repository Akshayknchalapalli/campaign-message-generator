from fastapi import FastAPI
from app.api.endpoints import router
from app.utils.data_loader import load_data, preprocess_data
from app.models.message_generator import MessageGenerator

app = FastAPI()
message_generator = MessageGenerator()
app.include_router(router)

@app.on_event("startup")
async def startup_event():
    message_generator.load_and_preprocess_data("app/data/real_estate_campaign_message_prompts.csv")
    message_generator.train()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)