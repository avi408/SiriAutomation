from appium import webdriver
from appium.options.ios import XCUITestOptions

options = XCUITestOptions()

options.set_capability("platformName", "iOS")
options.set_capability("automationName", "XCUITest")
options.set_capability("platformVersion", "26.5")
options.set_capability("deviceName", "iPhone 17 Pro")

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)

print("Session Created")
print(driver.session_id)

driver.quit()