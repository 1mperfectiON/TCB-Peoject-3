from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


first_name=input("input first name")
last_name=input("input last name")
origin_birthdate=input("input date of birth(MM/DD/YYYY)")
new_birthdate=origin_birthdate.split("/")
zip_code=input("input zipcode")
email=input("input email")
password_ftl=input("input password for ftl account")
password_gmail=input("input password for gmail")
telephone=input("input telephone")


def create_application():
    driver=webdriver.Chrome(executable_path="C:\\bin\chromedriver_win32\chromedriver.exe")
    options=webdriver.ChromeOptions()
    options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"')
    driver.get("https://www.google.com/")

    search=driver.find_element_by_name("q")
    search.send_keys("https://www.footlocker.com/")
    search.send_keys(Keys.RETURN)
    sleep(2)
    driver.find_element_by_xpath("//*[@id=\"vn1s0p1c0\"]/h3").click()
    sleep(1)
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/header/nav[1]/div[2]/button").click()
    sleep(0.5)
    driver.find_element_by_xpath("//*[@id=\"SignIn\"]/ul/li[2]/a").click()
    sleep(1.5)

    fill_out_first_name=driver.find_element_by_name("firstName")
    fill_out_first_name.send_keys(first_name)

    fill_out_last_name=driver.find_element_by_name("lastName")
    fill_out_last_name.send_keys(last_name)

    fill_out_month=driver.find_element_by_name("dateofbirthmonth")
    fill_out_month.send_keys(new_birthdate[0])

    fill_out_day=driver.find_element_by_name("dateofbirthday")
    fill_out_day.send_keys(new_birthdate[1])

    fill_out_year=driver.find_element_by_name("dateofbirthyear")
    fill_out_year.send_keys(new_birthdate[2])

    fill_out_zip_code=driver.find_element_by_name("postalCode")
    fill_out_zip_code.send_keys(zip_code)

    fill_out_email=driver.find_element_by_name("uid")
    fill_out_email.send_keys(email)

    fill_out_password=driver.find_element_by_name("password")
    fill_out_password.send_keys(password_ftl)

    fill_out_telephone=driver.find_element_by_name("phoneNumber")
    fill_out_telephone.send_keys(telephone)

    submit_application=driver.find_element_by_xpath("//*[@id=\"AccountCreate\"]/div[11]/button").click()
    sleep(3)

    driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent")
    driver.find_element_by_xpath("//*[@id=\"openid-buttons\"]/button[1]").click()
    driver.find_element_by_xpath("//input[@type=\"email\"]").send_keys(email)
    driver.find_element_by_xpath("//*[@id=\"identifierNext\"]").click()
    sleep(3)
    driver.find_element_by_xpath("//input[@type=\"password\"]").send_keys(password_gmail)
    driver.find_element_by_xpath("//*[@id=\"passwordNext\"]").click()
    sleep(2)
    driver.get("https://mail.google.com/mail")
    sleep(1)
    driver.find_elements_by_xpath("//span[contains(text(),\"Validate your new FLX\")]")[1].click()
    sleep(1)
    driver.find_element_by_xpath("//a[contains(@href,\"https://www.footlocker.com/\")]").click()
    sleep(2)
    quit()

create_application()



















