import pprint
from user_courses.model import Datum, UserCourses


def select_courses(user_courses: UserCourses) -> Datum:
    courses = [
        course.name for course in user_courses.data
    ]

    input_message = f"Choose Course ({'/'.join(map(str, range(len(user_courses.data))))}): "
    chosen = int(input(input_message))
    return user_courses.data[chosen]