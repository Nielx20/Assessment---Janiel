import time
import requests


def create_users(name, job):
    url = “https: // reqres. in /api/users”
    data = {“name”: name, “job”: job}


start_time = time.time()
response = request.post(url, data=data)
end_time = time.time()

if response.status_code == 201:
    response_data = response.json()
    user_name = response_data[“name”]
    user_job = response_data[“job”]
    user_id = response_data[“id”]
    created_at = response_data[“createdAt”]
    time_spent = end_time - start_time

    return user_name, user_job, user_id, created_at, time_spent
