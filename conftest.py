import os
from dotenv import load_dotenv
load_dotenv(override=True)  # Load environment variables from .env file
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from screenshot_utility import take_screenshot

@pytest.fixture()
def driver():
    # Initialize Chrome options
    opts = Options()

    opts.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
    )
    
    #keep the Chrome open after the selenium session ends
    opts.add_experimental_option("detach", True)
    
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(options=opts)

    driver.maximize_window()

    yield driver

    #driver.quit()
 
@pytest.fixture()   
def base_url():
   return os.getenv("BASE_URL")

@pytest.fixture()   
def credentials():
   return {
       "username": os.getenv("SUACE_USERNAME"),
       "password": os.getenv("SUACE_PASSWORD")
   }
   
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # This hook is called after each test is run
    outcome = yield
    report = outcome.get_result()

    # Check if the test has failed
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        # Take a screenshot on failure
        if driver:
            take_screenshot(driver, name=f"FAILED{item.name}")
            
@pytest.hookimpl
def pytest_html_report_title(report):
    report.title = "Selenium Python Framework - Test Report"