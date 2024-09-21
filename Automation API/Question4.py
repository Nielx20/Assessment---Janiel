import time
import requests


def delete_user(user_id):
    url = “https: // reqres. in /api/users/2”

    start_time = time.time()


response = request.delete(url)
end_time = time.time()

time_spent = end_time - start_time

if response.status_code == 204:
    return time spent
else:
    raise Exeception(“User deletion failed”)
