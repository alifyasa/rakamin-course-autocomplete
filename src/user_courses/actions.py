from prompt_toolkit.shortcuts import radiolist_dialog

from .model import UserCourses, Datum


def select_course(user_courses: UserCourses) -> Datum:
    result = radiolist_dialog(
        title="Choose Course",
        text="Which course to autocomplete? (Press Tab to switch focus)",
        values=[
            (idx, course.name) for idx, course in enumerate(user_courses.data)
        ]
    ).run()
    return user_courses.data[int(result)]