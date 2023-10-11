"""File for storing the OpenAI APIkey. When running locally replace with api key"""
import os

APIKEY = os.getenv('OPENAI_API_KEY')
