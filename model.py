import requests

API_URL = "https://api-inference.huggingface.co/models/taroii/sonnet-generator"
headers = {"Authorization": "Bearer ****INSERT CODE HERE****"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
