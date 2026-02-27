import re
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from tests.page_objects import PageObjects
from config.config import Config
from datetime import datetime
import os

@pytest.fixture(scope="session")
def page_obj(setup_teardown):
    """
    Automatically provides PageObjects instance to tests.
    Tests can directly use page_obj.method_name()
    """
    return PageObjects(setup_teardown)


@pytest.fixture(scope="session")
def setup_teardown(playwright: Playwright, request):

    # ✅ Create timestamp once per execution
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # ✅ Create dynamic video folder
    video_path = os.path.join("videos", timestamp)
    os.makedirs(video_path, exist_ok=True)

    browser = playwright.chromium.launch()

    # ✅ Always record video
    context = browser.new_context(
        record_video_dir=video_path
    )

    page = context.new_page()

    page.set_viewport_size({"width": 1350, "height": 630})
    page = context.new_page()

    # Browser settings
    page.set_viewport_size({"width": 1350, "height": 720})
    page.goto("https://devapp.tutorwand.com/", wait_until="domcontentloaded", timeout=60000)

    page.set_default_navigation_timeout(60000)
    page.set_default_timeout(60000)
    yield page
    context.close()
    browser.close()
