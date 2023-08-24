from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
from dotenv import dotenv_values

config = dotenv_values("./config/.env")
tokenizer = AutoTokenizer.from_pretrained(config.get("model_path"))
model = AutoModelForQuestionAnswering.from_pretrained(config.get("tokenizer_path"))
question_answerer = pipeline("question-answering", model=model, tokenizer=tokenizer)
