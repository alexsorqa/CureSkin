from app.application import Application
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait


def before_all(context):
    context.config.setup_logging()
    context.service = Service('/Users/asorokin/Desktop/careerist/CureSkin/chromedriver')
    # context.service = Service('/Users/asorokin/Desktop/careerist/CureSkin/geckodriver')


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    # Add any necessary options to the ChromeOptions object here
    context.driver = webdriver.Chrome(service=context.service, options=options)
    # context.driver = webdriver.Firefox(service=context.service)
    # context.driver = webdriver.Safari()

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def after_scenario(context, scenario):
    context.driver.delete_all_cookies()
    context.driver.quit()