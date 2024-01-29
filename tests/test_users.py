import pytest
import re
from playwright.sync_api import Page, expect


def test_login_logout(page: Page) -> None:
    page.goto("http://localhost:5000/")
    expect(page).to_have_title("Flask Blog")

    page.get_by_role("link", name="Login").click()
    expect(page).to_have_title("Flask Blog - Login")

    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("jkaganda@gmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("password")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Logout").click()

    expect(page).to_have_title("Flask Blog")


def test_registration(page: Page) -> None:
    page.goto("http://localhost:5000/")

    page.get_by_role("link", name="Register").click()
    expect(page).to_have_title("Flask Blog - Register")

    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("James")
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("james@demo.com")
    page.get_by_label("Password", exact=True).click()
    page.get_by_label("Password", exact=True).fill("password")
    page.get_by_label("Confirm Password").click()
    page.get_by_label("Confirm Password").fill("password")

    page.get_by_role("button", name="Sign Up").click()
    expect(page).to_have_title("Flask Blog - Login")

    expect(page.get_by_role("main")).to_contain_text("Your account has been created! You are now able to log in")


def test_example(page: Page) -> None:
    page.goto("http://localhost:5000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("jkaganda@gmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("password")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("link", name="Account").click()
    expect(page).to_have_title("Flask Blog - Account")

    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("John Updated")
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("updated@gmail.com")

    page.get_by_role("button", name="Update").click()
    expect(page).to_have_title("Flask Blog - Account")

    expect(page.get_by_role("main")).to_contain_text("Your account has been updated!")

    page.get_by_role("link", name="Logout").click()
    expect(page).to_have_title("Flask Blog")

