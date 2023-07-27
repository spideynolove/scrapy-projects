from seleniumwire import webdriver
from shutil import which
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

fire_options = Options()
fire_options.add_argument("--headless")

firefox_path = which("geckodriver")
print(f"firefox_path: {firefox_path}")

# Create a new instance of the Gecko driver
# driver = webdriver.Firefox(executable_path=firefox_path, options=fire_options)
driver = webdriver.Firefox(executable_path=firefox_path)

# Go to the Google home page
driver.get('https://www.google.com.vn')

input_content = driver.find_element("xpath", "//input[@title='Tìm kiếm']")
input_content.send_keys("onejav.com")

# # way 1
driver.find_element("xpath", "(//input[@value='Tìm trên Google'])[2]").click()

driver.find_element(
    "xpath", "//h3[contains(text(), 'OneJAV.com - Free JAV Torrents')]").click()


# # Access requests via the `requests` attribute
# for request in driver.requests:
#     if request.response:
#         print(
#             request.url,
#             request.response.status_code,
#             request.response.headers['Content-Type']
#         )


driver.close()
