from playwright.sync_api import Page, expect


def test_loginform_validation(page: Page) -> None:
    page.goto("http://localhost:5000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("group")).to_contain_text("This field is required.")
    expect(page.get_by_role("group")).to_contain_text("This field is required.")
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("jkaganda@gmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("sjlkfhldshlksj")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_title("Flask Blog - Login")
    expect(page.get_by_role("main")).to_contain_text("Login Unsuccessful. Please check email and password")
    page.get_by_role("link", name="Home").click()


def test_accountUpdateForm_validation(page: Page) -> None:
    page.goto("http://localhost:5000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("jkaganda@gmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("password")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Account").click()
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("")
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("")

    page.get_by_role("button", name="Update").click()
    expect(page).to_have_title("Flask Blog - Account")
    expect(page.get_by_role("group")).to_contain_text("This field is required.")
    expect(page.get_by_role("group")).to_contain_text("This field is required.")
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("TestUser")
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("TestUser@demo.com")

    page.get_by_role("button", name="Update").click()
    expect(page).to_have_title("Flask Blog - Account")
    expect(page.get_by_role("group")).to_contain_text("That username is taken. Please choose a different one.")
    expect(page.get_by_role("group")).to_contain_text("That email is taken. Please choose a different one.")
    page.get_by_role("link", name="Home").click()
    page.get_by_role("link", name="Logout").click()


def test_registerform_validation(page: Page) -> None:
    page.goto("http://localhost:5000/")
    page.get_by_role("link", name="Register").click()
    page.get_by_role("button", name="Sign Up").click()

    expect(page).to_have_title("Flask Blog - Register")
    expect(page.get_by_role("group")).to_contain_text("This field is required.")
    expect(page.get_by_role("group")).to_contain_text("This field is required.")
    expect(page.get_by_role("group")).to_contain_text("This field is required.")
    expect(page.get_by_role("group")).to_contain_text("This field is required.")
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("r")
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("sdffadsfss")
    page.get_by_label("Password", exact=True).click()
    page.get_by_label("Password", exact=True).fill("testing")
    page.get_by_label("Confirm Password").click()
    page.get_by_label("Confirm Password").fill("tested")

    page.get_by_role("button", name="Sign Up").click()
    expect(page).to_have_title("Flask Blog - Register")
    expect(page.get_by_role("group")).to_contain_text("Field must be between 2 and 20 characters long.")
    expect(page.get_by_role("group")).to_contain_text("Invalid email address.")
    expect(page.get_by_role("group")).to_contain_text("Passwords must match")
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("TestUser")
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("TestUser@demo.com")
    page.get_by_label("Password", exact=True).click()
    page.get_by_label("Password", exact=True).fill("testing")
    page.get_by_label("Confirm Password").click()
    page.get_by_label("Confirm Password").fill("testing")
    page.get_by_role("button", name="Sign Up").click()

    expect(page).to_have_title("Flask Blog - Register")
    expect(page.get_by_role("group")).to_contain_text("That username is taken. Please choose a different one.")
    expect(page.get_by_role("group")).to_contain_text("That email is taken. Please choose a different one.")
    page.get_by_role("link", name="Home").click()


def test_postform_validation(page: Page) -> None:
    page.goto("http://localhost:5000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("jkaganda@gmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("password")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("link", name="New Post", exact=True).click()
    expect(page).to_have_title("Flask Blog - New Post")

    page.get_by_role("button", name="Post").click()
    expect(page).to_have_title("Flask Blog - New Post")
    expect(page.get_by_role("group")).to_contain_text("This field is required.")
    expect(page.get_by_role("group")).to_contain_text("This field is required.")
    page.get_by_role("link", name="Home").click()
    page.get_by_role("link", name="Logout").click()