import time
import keyboard
import shutil

from random_mail2 import generate_random_email, generate_random_name, input_pv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


in_pwd = '*********'
transfer_username = '*******'

if __name__ == '__main__':
    # folder_path = './data'
    #
    # shutil.rmtree(folder_path)
    options = webdriver.ChromeOptions()
    # Enable incognito mode
    # options.add_argument("--incognito")

    # options.add_argument("--user-data-dir=./data")
    # options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    # options.binary_location = chrome_path

    dc_name = generate_random_name()
    dc_mail = generate_random_email()
    input('sssssssss')
    # print('1111')
    time.sleep(10)

    driver = webdriver.Chrome(options=options)
    # try:

    window_handles = driver.window_handles

    for handle in window_handles:
        driver.switch_to.window(handle)

        if driver.title == 'tea':
            print("找到了标题为 'tea' 的窗口！")
            break

    wait = WebDriverWait(driver, 30)
    input_username_path = '/html/body/div/div[2]/div[2]/div/section/div[2]/article/div[4]/div/div/input'
    input_username = wait.until(EC.presence_of_element_located((By.XPATH, input_username_path))).send_keys(dc_name)
    time.sleep(5)

    wait2 = WebDriverWait(driver, 10)
    for _ in range(3):
        try:
            click_path = '/html/body/div/div[2]/div[2]/div/section/div[2]/footer/button/span'
            tea_reg_click = wait2.until(EC.presence_of_element_located((By.XPATH, click_path)))
            tea_reg_click.click()
            time.sleep(1)
            break
        except:
            time.sleep(2)
            pass
    #loading
    # time.sleep(10)
    check_path = '/html/body/div/div[2]/div[2]/div/section/main/div/div[1]/div/div[2]/button'
    a = wait.until(EC.presence_of_element_located((By.XPATH, check_path)))

    set_url = 'https://app.tea.xyz/settings'
    driver.execute_script("window.open('');")

    driver.switch_to.window(driver.window_handles[-1])
    print('settings')

    driver.get(set_url)
    for _ in range(5):
        try:
            add_email_path = '/html/body/div/div[2]/div[2]/div/section/main/div/section/div/article[4]/button/span'
            add_email_click = wait.until(EC.presence_of_element_located((By.XPATH, add_email_path)))
            add_email_click.click()

            input_email_path = '/html/body/div/div[2]/div[2]/div/section/main/div/section/div/article[4]/div[2]/div/div/input'
            add_email_click = wait.until(EC.presence_of_element_located((By.XPATH, input_email_path))).send_keys(dc_mail)

            save_email_path = '/html/body/div/div[2]/div[2]/div/section/main/div/section/div/article[4]/div[2]/button/span'
            save_email_click = wait.until(EC.presence_of_element_located((By.XPATH, save_email_path)))
            save_email_click.click()
            break
        except Exception as e:
            time.sleep(2)
            pass


    for _ in range(5):
        try:
            add_profile_path = '/html/body/div/div[2]/div[2]/div/section/main/div/section/div/article[5]/button/span'
            add_profile_click = wait.until(EC.presence_of_element_located((By.XPATH, add_profile_path)))
            add_profile_click.click()

            save_profile_path = '/html/body/div/div[2]/div[2]/div/section/main/div/section/div/article[5]/button/span'
            save_profile_click = wait.until(EC.presence_of_element_located((By.XPATH, save_profile_path)))
            save_profile_click.click()
        except Exception as e:
            time.sleep(2)
            pass

    slider_path = '/html/body/div/div[2]/div[2]/div/section/main/div/section/div/article[2]/div[3]/div/div/div[4]'
    slider = wait.until(EC.presence_of_element_located((By.XPATH, slider_path)))
    actions = ActionChains(driver)

    n = 100
    ## 滑块
    try:
        while True:
            actions.click_and_hold(slider).move_by_offset(n, 0).release().perform()  # 10 是向右移动的像素
            time.sleep(0.5)  # sleep

            n = n + 100
            if n >= 800:
                break
    except:
        pass


    showpv_path = '/html/body/div/div[2]/div[2]/div/section/main/div/section/div/article[2]/div[4]/div/div[1]'
    showpv = wait.until(EC.presence_of_element_located((By.XPATH, showpv_path)))
    # text = showpv.text
    input_pv(showpv.text)

    # ------- transfer_tea https://app.tea.xyz/testnet
    # url = 'https://app.tea.xyz/testnet'
    #
    #click
    tranfer_tea_path = '/html/body/div/div[2]/div[2]/div/section/header/div[2]'
    tranfer_tea = wait.until(EC.presence_of_element_located((By.XPATH, tranfer_tea_path)))
    tranfer_tea.click()

    input_transfer_username_path = '/html/body/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div/input'
    input_tranfer_tea = wait.until(EC.presence_of_element_located((By.XPATH, input_transfer_username_path))).send_keys(transfer_username)
    time.sleep(3)

    choose25_path = '/html/body/div[2]/div/div/div/div[2]/div/div[2]/div/div[2]/div/input' #click
    choose25 = wait.until(EC.presence_of_element_located((By.XPATH, choose25_path))).send_keys('1')
    # choose25.click()

    transfer_tea_now_path = '/html/body/div[2]/div/div/div/div[2]/div/button'
    transfer_tea_now = wait.until(EC.presence_of_element_located((By.XPATH, transfer_tea_now_path)))
    transfer_tea_now.click()

    transfer_tea_true_path = '/html/body/div[2]/div/div/div/div[2]/div/button[1]'
    transfer_tea_true = wait.until(EC.presence_of_element_located((By.XPATH, transfer_tea_true_path)))
    transfer_tea_true.click()

    #---- stake
    stake_project = 'https://app.tea.xyz/oss-staking/f7e6f2d2-8072-4c9a-affe-fd0346b996a8'
    driver.execute_script("window.open('');")

    driver.switch_to.window(driver.window_handles[-1])

    driver.get(stake_project)

    stake_input_path = '/html/body/div/div[2]/div[2]/div/section/main/div/section/aside/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/input'
    stake_input = wait.until(EC.presence_of_element_located((By.XPATH, stake_input_path))).send_keys('1')


    stake_click_path = '/html/body/div/div[2]/div[2]/div/section/main/div/section/aside/div[1]/div/div[2]/div[1]/div/div/button/span'
    stake_click = wait.until(EC.presence_of_element_located((By.XPATH, stake_click_path)))
    stake_click.click()

    stake_true1_path = '/html/body/div/div[2]/div[2]/div/section/main/div/section/aside/div[1]/div/div[2]/div[1]/div/div/article/div[1]/input'
    stake_true1 = wait.until(EC.presence_of_element_located((By.XPATH, stake_true1_path)))
    stake_true1.click()
    stake_true2_path = '/html/body/div/div[2]/div[2]/div/section/main/div/section/aside/div[1]/div/div[2]/div[1]/div/div/article/div[2]/input'
    stake_true2 = wait.until(EC.presence_of_element_located((By.XPATH, stake_true2_path)))
    stake_true2.click()

    stake_confirm_path = '/html/body/div/div[2]/div[2]/div/section/main/div/section/aside/div[1]/div/div[2]/div[1]/div/div/article/button/span'
    stake_confirm = wait.until(EC.presence_of_element_located((By.XPATH, stake_confirm_path)))
    stake_confirm.click()
    time.sleep(10)

    #---- unstak
    url = 'https://app.tea.xyz/oss-staking'
    driver.execute_script("window.open('');")

    driver.switch_to.window(driver.window_handles[-1])

    driver.get(url)

    staked_project_path = '/html/body/div/div[2]/div[2]/div/section/main/div/div[4]/div/section/div/header/div/button[2]/span/span'  #click
    staked_project = wait.until(EC.presence_of_element_located((By.XPATH, staked_project_path)))
    staked_project.click()

    unstake_path = '/html/body/div/div[2]/div[2]/div/section/main/div/div[4]/div/section/div/div/div/div/div[1]/table/tbody/tr[1]/td[5]/div/button[2]/span'
    unstake = wait.until(EC.presence_of_element_located((By.XPATH, unstake_path)))
    unstake.click()

    unstake_amount_path = '/html/body/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div/input'
    unstake_amount = wait.until(EC.presence_of_element_located((By.XPATH, unstake_amount_path))).send_keys('1')


    unstake_true_path = '/html/body/div[2]/div/div/div/div[2]/div/button'
    unstake_true = wait.until(EC.presence_of_element_located((By.XPATH, unstake_true_path)))
    unstake_true.click()

    unstak_confirm_path = '/html/body/div[2]/div/div/div/div/div/button/span'
    unstak_confirm = wait.until(EC.presence_of_element_located((By.XPATH, unstak_confirm_path)))
    unstak_confirm.click()


    # input_pv()
    driver.quit()
    # input('end')

