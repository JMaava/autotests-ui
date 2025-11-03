from playwright.sync_api import sync_playwright, expect

from tools.routes import AppRoute

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        AppRoute.LOGIN,
        wait_until='networkidle'
    )

    new_text = 'New Title'
    page.evaluate(
        """
        (text) => {
            const title = document.getElementById('authentication-ui-course-title-text')
            title.textContent = 'New Text'
        }
        """,
        new_text
    )
