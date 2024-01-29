from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("http://localhost:5000/")
    page.get_by_role("link", name="2", exact=True).click()
    page.get_by_role("link", name="3").click()
    page.get_by_role("link", name="4").click()

    page.get_by_role("link", name="How I Record My Videos").click()
    expect(page).to_have_title("Flask Blog - How I Record My Videos")

    page.get_by_role("link", name="Home").click()
    expect(page).to_have_title("Flask Blog")
    expect(page.get_by_role("main")).to_contain_text("1")

