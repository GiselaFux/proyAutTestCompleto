import yaml
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from ui.pages.login_page import LoginPage
from ui.pages.inventory_page import InventoryPage

def before_all(context):
    with open("config/config.yaml") as f:
        context.config_data = yaml.safe_load(f)

def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    context.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    context.driver.implicitly_wait(context.config_data["implicit_wait"])
    context.login_page = LoginPage(context.driver)
    context.inventory_page = InventoryPage(context.driver)

def after_scenario(context, scenario):
    if scenario.status == "failed":
        context.driver.save_screenshot(f"screenshots/behave_{scenario.name}.png")
    context.driver.quit()