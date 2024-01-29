from playwright.sync_api import Page, expect


def test_create_new_post(page: Page) -> None:
    page.goto("http://localhost:5000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("jkaganda@gmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("password")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("link", name="New Post", exact=True).click()
    expect(page).to_have_title("Flask Blog - New Post")

    page.get_by_label("Title").click()
    page.get_by_label("Title").fill("Swimming Practice")
    page.get_by_label("Content").click()
    page.get_by_label("Content").fill("Swimming is a great sport to play if you want to get fit.")
    page.get_by_role("button", name="Post").click()

    expect(page).to_have_title("Flask Blog")
    expect(page.get_by_role("main")).to_contain_text("Your post has been created!")

    page.get_by_role("link", name="Logout").click()


def test_update_post(page: Page) -> None:
    page.goto("http://localhost:5000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("jkaganda@gmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("password")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("link", name="Swimming Practice").click()
    expect(page).to_have_title("Flask Blog - Swimming Practice")

    page.get_by_role("link", name="Update").click()
    expect(page).to_have_title("Flask Blog - Update Post")

    page.get_by_label("Title").click()
    page.get_by_label("Title").fill("Swimming Practice Updated")
    page.get_by_label("Content").click()
    page.get_by_label("Content").fill("Swimming is a great sport to play if you want to get fit. Updated")

    page.get_by_role("button", name="Post").click()
    expect(page).to_have_title("Flask Blog - Swimming Practice Updated")
    expect(page.get_by_role("main")).to_contain_text("Your post has been updated!")

    page.get_by_role("link", name="Logout").click()


def test_delete_post(page: Page) -> None:
    page.goto("http://localhost:5000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("jkaganda@gmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("password")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("link", name="Swimming Practice Updated").click()
    expect(page).to_have_title("Flask Blog - Swimming Practice Updated")

    page.get_by_role("button", name="Delete").click()
    expect(page.locator("#deleteModalLabel")).to_contain_text("Delete Post?")

    page.get_by_label("Delete Post?").get_by_role("button", name="Delete").click()
    expect(page).to_have_title("Flask Blog")
    expect(page.get_by_role("main")).to_contain_text("Your post has been deleted")

    page.get_by_role("link", name="Logout").click()
