from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
from app.utils.data_loader import load_data, preprocess_data
import pandas as pd

class MessageGenerator:
    def __init__(self, model_name="gpt2" , data_path="app/data/real_estate_campaign_message_prompts.csv"):
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        self.train_data = self.load_and_preprocess_data(data_path)

    def load_and_preprocess_data(self, data_path):
        data = load_data(data_path)
        train_data, _ = preprocess_data(data)
        return pd.DataFrame(train_data)


    def train(self):
        # Concatenate prompt and message for each example
        full_texts = [
            prompt + self.tokenizer.eos_token + message + self.tokenizer.eos_token
            for prompt, message in zip(self.train_data['prompt'], self.train_data['message'])
        ]
        inputs = self.tokenizer(full_texts, return_tensors="pt", padding=True, truncation=True)
        labels = inputs['input_ids'].clone()

        self.model.train()
        optimizer = torch.optim.AdamW(self.model.parameters(), lr=5e-5)

        for epoch in range(50):
            optimizer.zero_grad()
            outputs = self.model(**inputs, labels=labels)
            loss = outputs.loss
            loss.backward()
            optimizer.step()
            if (epoch + 1) % 10 == 0:
                print(f"Epoch {epoch+1} loss: {loss.item():.4f}")

    def generate_message(self, prompt):
        self.model.eval()
        inputs = self.tokenizer(prompt, return_tensors="pt")
        input_ids = inputs["input_ids"]
        attention_mask = inputs["attention_mask"]
        
        outputs = self.model.generate(
            input_ids,
            attention_mask=attention_mask,
            max_length=100,
            num_return_sequences=1,
            pad_token_id=self.tokenizer.eos_token_id,
            do_sample=True,
            temperature=0.8,
            top_p=0.9,
            repetition_penalty=1.2,
            no_repeat_ngram_size=3
        )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)


