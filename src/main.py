import pprint
# from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import input_dialog

from user_courses import UserCourses, get_user_courses, select_course



if __name__ == "__main__":
    bearer_token: str = input_dialog(
        title='Bearer Token',
        text="Please enter your bearer token. Example: Bearer XXX.YYY.ZZZ"
    ).run()
    user_courses = get_user_courses(bearer_token)
    selected_course = select_course(user_courses)
    pprint.pprint(selected_course)
