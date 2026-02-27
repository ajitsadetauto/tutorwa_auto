import time
import pytest

# ---------- Global Variables ----------
Teacher_email = "tutorwand.teacher2@wcschool.in"
Teacher_pass = "India$123"

Student_email = "testven_81@mailinator.com"
Student_pass = "Test@123"
# --------------------------------------


@pytest.mark.userregister
def test_user_register(page_obj):
    print("1st test loaded successfully")
    page_obj.login_function(Teacher_email, Teacher_pass)


@pytest.mark.fastrack
def test_assign_fastrack(page_obj):
    page_obj.assign_fastrack_test()
    page_obj.fastrack_review_question()


@pytest.mark.fastrack
def test_schedule_page(page_obj):
    page_obj.schedule_page_data()


@pytest.mark.fastrack
def test_feedback_page(page_obj):
    page_obj.feedback_page()


