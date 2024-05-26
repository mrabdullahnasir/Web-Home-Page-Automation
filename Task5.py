import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def setup(request):
    my_driver = webdriver.Chrome()
    my_driver.get('https://www.pf.com.pk/')
    my_driver.maximize_window()

    def teardown():
        # Cleanup after all the test cases are executed
        my_driver.close()

    request.addfinalizer(teardown)
    return my_driver


def test_home_page(setup):
    # asserting the logo
    my_driver = setup
    wait = WebDriverWait(my_driver, 10)
    my_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='footer-logo']")))
    logo = my_driver.find_element(By.XPATH, "//img[@alt='footer-logo']")
    assert logo.is_displayed()

    # opening multiple header links and taking screenshot
    header = my_driver.find_element(By.XPATH, "//ul[@id='top-menu']")
    pages = header.find_elements(By.TAG_NAME, 'a')
    pages_to_open = ['About Us', 'Careers', 'Life at PF', 'Expertise', 'Blogs', 'Graduate Gateway Program']
    for page in pages:
        if page.text in pages_to_open:
            page_text = page.text
            about = my_driver.find_element(By.XPATH, f"//a[text()='{page_text}']")
            about.send_keys(Keys.CONTROL + Keys.RETURN)
    my_driver.save_screenshot('pages.png')

    # Form Filling
    my_driver.find_element(By.XPATH, "//a[text()='Apply Now']").click()
    my_driver.find_element(By.XPATH, "//a[@href='https://pf.com.pk/job/mid-level-sqa-engineer/']//p[@class='apply-m-now']").click()
    dob = my_driver.find_element(By.CSS_SELECTOR, "input#dob")
    my_driver.execute_script("arguments[0].setAttribute('value','1998-08-24')", dob)
    my_driver.find_element(By.XPATH, '//input[@id="name"]').send_keys('Abdullah Nasir')
    my_driver.find_element(By.XPATH, '//input[@id="email"]').send_keys('abdullahnasir361@gmail.com')
    my_driver.find_element(By.XPATH, '//input[@id="cnic"]').send_keys('1234567890123')
    my_driver.find_element(By.XPATH, '//input[@id="phone"]').send_keys('+123456789012')
    my_driver.find_element(By.XPATH, '//input[@id="address"]').send_keys('Lahore')
    my_driver.find_element(By.XPATH, '//input[@id="city"]').send_keys('Lahore')
    my_driver.find_element(By.ID, "qualification").click()
    my_driver.find_element(By.XPATH, "//option[@value='BSCS']").click()
    my_driver.find_element(By.ID, "yr-of-comp").click()
    my_driver.find_element(By.XPATH, "//option[@value='2019']").click()
    my_driver.find_element(By.ID, "university").send_keys('UET')
    my_driver.find_element(By.ID, "cgpa_cd").send_keys('3.05')
    my_driver.find_element(By.XPATH, "//input[@name='cur-working']").click()
    my_driver.find_element(By.ID, "salry-expt").send_keys('1000000')
    doj = my_driver.find_element(By.ID, "doj")
    my_driver.execute_script("arguments[0].setAttribute('value','2024-07-01')", doj)
    my_driver.find_element(By.ID, "hear-abt-us").send_keys('LinkedIn')
    my_driver.find_element(By.ID, "experiance").click()
    my_driver.find_element(By.XPATH, "//option[@value='4 Years']").click()
    my_driver.find_element(By.ID, "resume").send_keys('A:\Automation Assignment\PF_Task5\pythonProject\Abdullah Nasir.pdf')
