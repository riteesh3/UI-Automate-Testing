# ScreenShot of websiter using selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(),options = options)
driver.implicitly_wait(10)

URL = 'http://localhost:4200/home'
driver.get(URL)
S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment                                                                                                                
driver.find_element_by_tag_name('body').screenshot('screenshot.png');