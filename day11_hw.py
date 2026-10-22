
from tracker import create_record
from datetime import datetime
import json


records = [
    create_record("Kochi", "Visited Fort Kochi", "05-06-2022"),
    create_record("Munnar", "Enjoyed the mountains", "15-12-2023"),
    create_record("Alappuzha", "Enjoyed the backwaters", "20-01-2024")
]


for record in records:
    date_object = datetime.strptime(
        record["visit_date"], "%d-%m-%Y"
    ).date()

    record["visit_date"] = date_object.strftime("%B %d, %Y")


json_data = json.dumps(records, indent=4)

print("JSON Data:")
print(json_data)

python_records = json.loads(json_data)


print("\nIndividual Travel Records:")
for record in python_records:
    print(
        f"City: {record['city']}, "
        f"Comment: {record['comment']}, "
        f"Visit Date: {record['visit_date']}"
    )
