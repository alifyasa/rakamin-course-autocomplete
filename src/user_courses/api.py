import pprint
import requests
from lib import create_header
from .model import UserCourses, user_courses_from_dict

def get_user_courses(bearer_token: str) -> UserCourses:
    url = "https://api.rakamin.com/api/v1/courses?state=enrolled"
    try:
        response = requests.get(url, headers=create_header(bearer_token))
        response.raise_for_status()  # Raises HTTPError for non-200 status codes
        parsed_response = response.json()
        return user_courses_from_dict(parsed_response)
    except requests.exceptions.RequestException as e:
        print("Error occurred during the request:", e)
        # Re-raise the exception with additional context
        raise requests.exceptions.RequestException("Failed to make the request") from e