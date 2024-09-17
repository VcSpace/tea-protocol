import time
import keyboard
import shutil

from random_mail2 import generate_random_email, generate_random_name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

in_pwd = 'password@'


if __name__ == '__main__':
    # 指定要删除的文件夹路径
    # folder_path = './data'
    #
    # # 删除文件夹及其所有内容
    # shutil.rmtree(folder_path)
    options = webdriver.ChromeOptions()
    # Enable incognito mode
    # options.add_argument("--incognito")

    # Set user data folder
    # options.add_argument("--user-data-dir=./data")
    # options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")


    # options.binary_location = chrome_path
    driver = webdriver.Chrome(options=options)
    URL = 'https://app.tea.xyz/sign-up?r=RdMehHaY0Z2'
    driver.get(URL)

    time.sleep(2)
    wait = WebDriverWait(driver, 30)
    name = generate_random_name()


    for i in range(10):
        try:
            tea_dc_button_path = '/html/body/div/div[2]/div[2]/div/section/div/figure/div[1]/section/div[1]/button[3]/span'
            tea_dc_button = wait.until(EC.presence_of_element_located((By.XPATH, tea_dc_button_path)))
            tea_dc_button.click()
            break
        except Exception as e:
            time.sleep(2)
            continue

    try:
        list_windows = driver.window_handles

        driver.switch_to.window(list_windows[-1])
        dc_reg_button_path = '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/div[3]/button/div'
        dc_reg_button = wait.until(EC.presence_of_element_located((By.XPATH, dc_reg_button_path)))
        time.sleep(5)
        dc_reg_button.click()


        dc_input_mail_path = '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/form/div[2]/div/div[1]/div/input'
        dc_input_mail = wait.until(EC.presence_of_element_located((By.XPATH, dc_input_mail_path))).send_keys(generate_random_email())

        dc_input_username_path = '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/form/div[2]/div/div[4]/div[1]/div/input'
        dc_input_username = wait.until(EC.presence_of_element_located((By.XPATH, dc_input_username_path))).send_keys(name)

        dc_input_pwd_path = '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/form/div[2]/div/div[5]/div/input'
        dc_input_pwd = wait.until(EC.presence_of_element_located((By.XPATH, dc_input_pwd_path))).send_keys(in_pwd)

        dc_year_path = '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/form/div[2]/div/fieldset/div/div[1]/div/div/div/div/div[1]'
        dc_year_button = wait.until(EC.presence_of_element_located((By.XPATH, dc_year_path)))
        dc_year_button.click()

        # chooseyear_path = '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/form/div[2]/div/fieldset/div/div[1]/div/div/div/div[2]/div/div[40]' # 1982
        choose_year_path = '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/form/div[2]/div/fieldset/div/div[1]/div/div/div/div[2]/div/div[26]' # 1996
        choose_year_button = wait.until(EC.presence_of_element_located((By.XPATH, choose_year_path)))
        choose_year_button.click()

        # -------month
        dc_month_path = '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/form/div[2]/div/fieldset/div/div[2]/div/div/div/div/div[1]'
        dc_month_button = wait.until(EC.presence_of_element_located((By.XPATH, dc_month_path)))
        dc_month_button.click()
        choose_month_path = '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/form/div[2]/div/fieldset/div/div[2]/div/div/div/div[2]/div/div[7]' # 7月
        choose_month_button = wait.until(EC.presence_of_element_located((By.XPATH, choose_month_path)))
        choose_month_button.click()


        # -------day
        dc_day_path = '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/form/div[2]/div/fieldset/div/div[3]/div/div/div/div/div[1]'
        dc_day_button = wait.until(EC.presence_of_element_located((By.XPATH, dc_day_path)))
        dc_day_button.click()

        choose_day_path = '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/form/div[2]/div/fieldset/div/div[3]/div/div/div/div[2]/div/div[8]' # 8号
        choose_day_button = wait.until(EC.presence_of_element_located((By.XPATH, choose_day_path)))
        choose_day_button.click()

        try:
            wait2 = WebDriverWait(driver, 10)
            agress_rules_path = '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/form/div[2]/div/div[8]/label/input'
            agress_rules = wait2.until(EC.presence_of_element_located((By.XPATH, agress_rules_path)))
            # agress_rules = driver.find_element(By.XPATH,agress_rules_path)
            agress_rules.click()
        except Exception as e:
            pass

        ----reg_continue
        reg_continue_path = '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/form/div[2]/div/div[7]/button'
        reg_continue = wait.until(EC.presence_of_element_located((By.XPATH, reg_continue_path)))
        reg_continue.click()

        time.sleep(20)

        approve_button_path = '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/div/div/div[2]/button[2]/div'
        js = wait.until(EC.presence_of_element_located((By.XPATH, approve_button_path)))
        # driver.execute_script("arguments[0].click();", js)
        # approve_button.click()


    except Exception as e:
        print(e)

    input("Press enter to exit...")
    driver.quit()

