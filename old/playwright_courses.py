from playwright.sync_api import sync_playwright, expect

from config import settings
from tools.routes import AppRoute

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(AppRoute.REGISTRATION)

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill(settings.test_user.email)

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill(settings.test_user.username)

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill(settings.test_user.password)

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path="../browser-state.json")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()

    page.goto(AppRoute.COURSES)

    title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(title).to_have_text('Courses')

    icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_visible()

    text = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(text).to_have_text('There is no results')

    description_text = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(description_text).to_have_text('Results from the load test pipeline will be displayed here')
