import time
from selenium.common.exceptions import NoSuchElementException

def test_is_element_present(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(3)
    try:
        browser.find_elements_by_css_selector("[class='btn btn-lg btn-primary btn-add-to-basket']")
        result = True
    except NoSuchElementException:
        result = False
    assert result == True, "Element not found"



