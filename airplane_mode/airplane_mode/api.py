# import requests
#
# base_url = "http://localhost:8000"
# endpoint = "/api/resource/Airport Shop"
#
# headers = {
# 	"Authorization": "token cee43e2cb262c29:2b3a3acfe55933e",
# 	"Content-Type": "application/json"
# }
# params = {
#     "fields": '["*"]'  # Fetch all fields
# }
# import pdb;pdb.set_trace()
# data = {
# 	"shop_name": "Shop 2",
# 	"shop_type": "Stall",
# 	"location": "Terminal A",
# 	"is_enabled": 1,
# 	"shop_number": "A1",
# 	"airport": "Jamnagar Airport",
# 	"area": 100,
# 	"tenant": "First Floor",
# 	"rent_amount": 50000
# }
#
# response = requests.post(f"{base_url}{endpoint}", headers=headers, json=data)
#
# # response = requests.get(f"{base_url}{endpoint}", headers=headers, params=params)
#
# print("Status Code:", response.status_code)
# print("Response JSON:", response.json())
#
# # Api Secret: 2b3a3acfe55933e
# # Api key : cee43e2cb262c29
