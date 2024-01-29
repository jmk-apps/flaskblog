import re
from playwright.sync_api import Page, expect


def test_404(page: Page) -> None:
    page.goto("http://localhost:5000/")

    page.goto("http://localhost:5000/invoices") # Note: this route does not exist
    expect(page).to_have_title("Flask Blog - 404")


def test_not_logged_in(page: Page) -> None:
    page.goto("http://localhost:5000/")

    # User was not logged in and tries to access routes that require login. They get redirected to the login page.
    page.goto("http://localhost:5000/login?next=%2Faccount")
    expect(page).to_have_title("Flask Blog - Login")
    page.get_by_role("link", name="Home").click()
    page.get_by_role("link", name="Soccer Practice").click()

    # User tries to update a post without logging in.
    page.goto("http://localhost:5000/login?next=%2Fpost%2F31%2Fupdate")
    expect(page).to_have_title("Flask Blog - Login")
    page.get_by_role("link", name="Home").click()

def test_403(page: Page) -> None:
    page.goto("http://localhost:5000/")

    # User is logged in but tries to update another user's post
    page.get_by_role("link", name="Login").click()
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("jkaganda@gmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("password")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Added Blueprints updated").click()

    page.goto("http://localhost:5000/post/28/update")
    expect(page).to_have_title("Flask Blog - 403")

    page.get_by_role("link", name="Home").click()

