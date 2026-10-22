
from tripdata import get_trip
from datetime import datetime
import json


trips = [
    get_trip("Kochi", "15-05-2023", "Visited Fort Kochi"),
    get_trip("Munnar", "20-12-2024", "Enjoyed the mountains"),
    get_trip("Alappuzha", "10-01-2025", "Enjoyed the backwaters")
]

for trip in trips:
    date_object = datetime.strptime(trip["date"], "%d-%m-%Y").date()
    trip["date"] = date_object.strftime("%B %d, %Y")

json_data = json.dumps(trips, indent=4)

print(json_data)
