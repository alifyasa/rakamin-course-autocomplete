from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Composition:
    exam: int
    reading: int
    homework: int
    attendance: int
    final_project: int

    @staticmethod
    def from_dict(obj: Any) -> 'Composition':
        assert isinstance(obj, dict)
        exam = int(from_str(obj.get("exam")))
        reading = int(from_str(obj.get("reading")))
        homework = int(from_str(obj.get("homework")))
        attendance = int(from_str(obj.get("attendance")))
        final_project = int(from_str(obj.get("final_project")))
        return Composition(exam, reading, homework, attendance, final_project)

    def to_dict(self) -> dict:
        result: dict = {}
        result["exam"] = from_str(str(self.exam))
        result["reading"] = from_str(str(self.reading))
        result["homework"] = from_str(str(self.homework))
        result["attendance"] = from_str(str(self.attendance))
        result["final_project"] = from_str(str(self.final_project))
        return result


@dataclass
class Datum:
    id: int
    name: str
    description: str
    category: str
    price: float
    discount_percentage: float
    initial_price: float
    picture_url: str
    image_partner_url: None
    starts_at: None
    ends_at: None
    composition: Composition
    difficulty: str
    whatsapp_group_url: str
    maximum_student: None
    visibility: str
    specialization: str
    batch: int
    code: None
    course_type: str
    tutor_companies: List[Any]
    schedules: List[Any]
    features: List[Any]
    early_bird_date: None
    video_url: str
    video_thumbnail_url: None
    created_at: datetime
    course_modules_count: int
    module_sessions_count: int
    user_courses_count: int
    course_group_url: str
    progress_state: str
    duration: float
    is_assessment: bool
    lock_previous_question: bool
    competency: None
    total_xp: int
    promo_code: None
    claimed_state: None
    state: str
    onboard_state: str
    progress_percentage: float

    @staticmethod
    def from_dict(obj: Any) -> 'Datum':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        description = from_str(obj.get("description"))
        category = from_str(obj.get("category"))
        price = from_float(obj.get("price"))
        discount_percentage = from_float(obj.get("discount_percentage"))
        initial_price = from_float(obj.get("initial_price"))
        picture_url = from_str(obj.get("picture_url"))
        image_partner_url = from_none(obj.get("image_partner_url"))
        starts_at = from_none(obj.get("starts_at"))
        ends_at = from_none(obj.get("ends_at"))
        composition = Composition.from_dict(obj.get("composition"))
        difficulty = from_str(obj.get("difficulty"))
        whatsapp_group_url = from_str(obj.get("whatsapp_group_url"))
        maximum_student = from_none(obj.get("maximum_student"))
        visibility = from_str(obj.get("visibility"))
        specialization = from_str(obj.get("specialization"))
        batch = int(from_str(obj.get("batch")))
        code = from_none(obj.get("code"))
        course_type = from_str(obj.get("course_type"))
        tutor_companies = from_list(lambda x: x, obj.get("tutor_companies"))
        schedules = from_list(lambda x: x, obj.get("schedules"))
        features = from_list(lambda x: x, obj.get("features"))
        early_bird_date = from_none(obj.get("early_bird_date"))
        video_url = from_str(obj.get("video_url"))
        video_thumbnail_url = from_none(obj.get("video_thumbnail_url"))
        created_at = from_datetime(obj.get("created_at"))
        course_modules_count = from_int(obj.get("course_modules_count"))
        module_sessions_count = from_int(obj.get("module_sessions_count"))
        user_courses_count = from_int(obj.get("user_courses_count"))
        course_group_url = from_str(obj.get("course_group_url"))
        progress_state = from_str(obj.get("progress_state"))
        duration = from_float(obj.get("duration"))
        is_assessment = from_bool(obj.get("is_assessment"))
        lock_previous_question = from_bool(obj.get("lock_previous_question"))
        competency = from_none(obj.get("competency"))
        total_xp = from_int(obj.get("total_xp"))
        promo_code = from_none(obj.get("promo_code"))
        claimed_state = from_none(obj.get("claimed_state"))
        state = from_str(obj.get("state"))
        onboard_state = from_str(obj.get("onboard_state"))
        progress_percentage = from_float(obj.get("progress_percentage"))
        return Datum(id, name, description, category, price, discount_percentage, initial_price, picture_url, image_partner_url, starts_at, ends_at, composition, difficulty, whatsapp_group_url, maximum_student, visibility, specialization, batch, code, course_type, tutor_companies, schedules, features, early_bird_date, video_url, video_thumbnail_url, created_at, course_modules_count, module_sessions_count, user_courses_count, course_group_url, progress_state, duration, is_assessment, lock_previous_question, competency, total_xp, promo_code, claimed_state, state, onboard_state, progress_percentage)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["description"] = from_str(self.description)
        result["category"] = from_str(self.category)
        result["price"] = to_float(self.price)
        result["discount_percentage"] = to_float(self.discount_percentage)
        result["initial_price"] = to_float(self.initial_price)
        result["picture_url"] = from_str(self.picture_url)
        result["image_partner_url"] = from_none(self.image_partner_url)
        result["starts_at"] = from_none(self.starts_at)
        result["ends_at"] = from_none(self.ends_at)
        result["composition"] = to_class(Composition, self.composition)
        result["difficulty"] = from_str(self.difficulty)
        result["whatsapp_group_url"] = from_str(self.whatsapp_group_url)
        result["maximum_student"] = from_none(self.maximum_student)
        result["visibility"] = from_str(self.visibility)
        result["specialization"] = from_str(self.specialization)
        result["batch"] = from_str(str(self.batch))
        result["code"] = from_none(self.code)
        result["course_type"] = from_str(self.course_type)
        result["tutor_companies"] = from_list(lambda x: x, self.tutor_companies)
        result["schedules"] = from_list(lambda x: x, self.schedules)
        result["features"] = from_list(lambda x: x, self.features)
        result["early_bird_date"] = from_none(self.early_bird_date)
        result["video_url"] = from_str(self.video_url)
        result["video_thumbnail_url"] = from_none(self.video_thumbnail_url)
        result["created_at"] = self.created_at.isoformat()
        result["course_modules_count"] = from_int(self.course_modules_count)
        result["module_sessions_count"] = from_int(self.module_sessions_count)
        result["user_courses_count"] = from_int(self.user_courses_count)
        result["course_group_url"] = from_str(self.course_group_url)
        result["progress_state"] = from_str(self.progress_state)
        result["duration"] = to_float(self.duration)
        result["is_assessment"] = from_bool(self.is_assessment)
        result["lock_previous_question"] = from_bool(self.lock_previous_question)
        result["competency"] = from_none(self.competency)
        result["total_xp"] = from_int(self.total_xp)
        result["promo_code"] = from_none(self.promo_code)
        result["claimed_state"] = from_none(self.claimed_state)
        result["state"] = from_str(self.state)
        result["onboard_state"] = from_str(self.onboard_state)
        result["progress_percentage"] = to_float(self.progress_percentage)
        return result


@dataclass
class Pagination:
    current_page: int
    next_page: None
    prev_page: None
    size: int
    total_pages: int
    total_count: int

    @staticmethod
    def from_dict(obj: Any) -> 'Pagination':
        assert isinstance(obj, dict)
        current_page = from_int(obj.get("current_page"))
        next_page = from_none(obj.get("next_page"))
        prev_page = from_none(obj.get("prev_page"))
        size = from_int(obj.get("size"))
        total_pages = from_int(obj.get("total_pages"))
        total_count = from_int(obj.get("total_count"))
        return Pagination(current_page, next_page, prev_page, size, total_pages, total_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["current_page"] = from_int(self.current_page)
        result["next_page"] = from_none(self.next_page)
        result["prev_page"] = from_none(self.prev_page)
        result["size"] = from_int(self.size)
        result["total_pages"] = from_int(self.total_pages)
        result["total_count"] = from_int(self.total_count)
        return result


@dataclass
class UserCourses:
    data: List[Datum]
    pagination: Pagination

    @staticmethod
    def from_dict(obj: Any) -> 'UserCourses':
        assert isinstance(obj, dict)
        data = from_list(Datum.from_dict, obj.get("data"))
        pagination = Pagination.from_dict(obj.get("pagination"))
        return UserCourses(data, pagination)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_list(lambda x: to_class(Datum, x), self.data)
        result["pagination"] = to_class(Pagination, self.pagination)
        return result


def user_courses_from_dict(s: Any) -> UserCourses:
    return UserCourses.from_dict(s)


def user_courses_to_dict(x: UserCourses) -> Any:
    return to_class(UserCourses, x)
