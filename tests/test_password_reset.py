from playwright.sync_api import Page, expect


def test_password_reset(page: Page) -> None:
    page.goto("http://localhost:5000/")

    page.get_by_role("link", name="Login").click()
    expect(page).to_have_title("Flask Blog - Login")

    page.get_by_role("link", name="Forgot Password?").click()
    expect(page).to_have_title("Flask Blog - Reset Password")

    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("jkaganda@gmail.com")

    page.get_by_role("button", name="Request Password Reset").click()
    expect(page).to_have_title("Flask Blog - Login")
    expect(page.get_by_role("main")).to_contain_text("An email has been sent with instructions to reset your password.")

    page.get_by_role("link", name="Home").click()
