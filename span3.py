import time
import random
import string
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# 配置二进制绝对路径
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

# driver.get('http://google.com/')

number_of_strings = 5
length_of_string = 8

# admins = ["1791422575@qq.com", "hVD0vYlODk@163.com",
#           "3500085264@qq.com", "2978632316@qq.com", "yWiCmEfkuU@163.com", "evKi6xEXri@163.com", "QP9BvGLvLw@163.com", "O7dKHKETWk@163.com", "OcZSarnTc2@163.com", "SPdrbhkV9f@163.com", "GgYbrsJ9SZ@163.com"]
# passwds = ["LY1x2i3a4o", "T9SZkGFRjX", "awrn32op", "LY1x2i3a4o", "GbEQx6xieo", "6kwUC6D3a3",
#            "s0UAJQI2MS", "nmg8CYYg82", "0P4yz5deuL", "gka60KTlPs", "R5HXNPv96y", "0OaXXkhMey"]

# 能用的,能刷,
# admins = ["1791422575@qq.com", "hVD0vYlODk@163.com",
#           "3500085264@qq.com", "evKi6xEXri@163.com", "SPdrbhkV9f@163.com"]
# passwds = ["LY1x2i3a4o", "T9SZkGFRjX", "awrn32op", "6kwUC6D3a3", "R5HXNPv96y"]

# 解锁的，这个也要刷
admins = ["yWiCmEfkuU@163.com", "QP9BvGLvLw@163.com", "O7dKHKETWk@163.com", "Pl2xSHORXv@163.com", "OcZSarnTc2@163.com", "GgYbrsJ9SZ@163.com", "FZ75EeB5jE@163.com",
          "M8kfxGLvs8@163.com", "dhVlDdUpXK@163.com", "HF6qcXRHu4@163.com"]
passwds = ["GbEQx6xieo", "s0UAJQI2MS", "nmg8CYYg82", "0P4yz5deuL", "gka60KTlPs", "0OaXXkhMey", "W09LkBXAZ2",
           "qyHZ2PWaTk", "F2wxoUYR5y", "wIQHcZ5qeL"]

# 被禁的，刷不了，要解锁
# admins = ["SPdrbhkV9f@163.com"]
# passwds = ["R5HXNPv96y"]
term = 0
for admin, passwd in zip(admins, passwds):
    term += 1
    driver = webdriver.Firefox(
        executable_path=r'C:\WebDriver\bin\geckodriver.exe', options=options)
    # driver = webdriver.Edge(executable_path=r'E:\Firefox_download\edgedriver_win64\msedgedriver.exe')
    driver.get("https://login.live.com/login.srf?")
    # driver.get("https://login.live.com/oauth20_authorize.srf?client_id=9c941f7c-a811-4e9c-8e66-29fdec50490f&scope=openid+profile+offline_access&redirect_uri=https%3a%2f%2frewards.bing.com%2fsignin-oidc&response_type=code&state=CfDJ8LbKok95JvtCpPQvgHivJ2pUXSa_VJU2ToVb4p-Nh3EuMX5LkOlVw19-RkoXGZ-GZuxohADa9q0n5EeZmt3aso0pfH_kalPyrP8uQsd5n8MC5Taf_Yrh0FT7p7gohVdPkWJPP00ME9wQ3BJL1ZJoBHPfJ1Vy4Ep6k-X2sxMKmRv-lx9ZasAIJJxXN-3ug4z_Of1zVeBofcdDz_M00ylh7b7W8S8AmsVAu3Mpk1dDnM68VzNu843qUN3vYCClZtSVsiszyz8UelWvmxrladKle-VTh2oIKDUjJJvYihbenHpFUwW-Txdc8GM5r5migD0QF_SUD9nxQBLAOdA6qmxd-5dL1fqoFLzsjT73huHKOeuDhFFlU91vgtxeJ9sThQRqc4lvtCihQBXIrEzlYgVlqziZYAhOr4QqfPQ1bLmQfvjV&response_mode=form_post&nonce=638105837675894846.MWI1NjliZDItNDg0Zi00YmIwLWI5ZjEtZjhlMTFkMzg5OTU4OTM3MjEyMzktOTc5Ny00OWRmLWE4YjMtZDMwMTYzNzM2OGFh&code_challenge=l2fN1r5-NqAgrlvcTlDodexnl46B05G4pj2LfY34Qcg&code_challenge_method=S256&x-client-SKU=ID_NET6_0&x-client-Ver=6.23.1.0&uaid=e1a2ab12b7a14c8ca6d220f07e106de3&msproxy=1&issuer=mso&tenant=consumers&ui_locales=zh-CN&client_info=1&epct=AQABAAAAAAD--DLA3VO7QrddgJg7WevrMIjsk_31UHMiNqIKZ49usFHqlY5g7xI1dPC7dANpOvtEOL9GnYLmnbn-AXZ19dICLVO3byTx2Gj3CJ8j8LDl2vYrND1ahufsDfFeJ7ksF5WtvQZlEk0UW_uHzS3DIWqTzTZgGfaB7Bfb0OThCOnaHQk42wvy9hhjSdK7qVn0P0qKpCev-ACdO-z061UiBLsSXM_I4FDA8kze9W0b-VYJ6CAA&jshs=0&fl=easi2&cobrandid=03c8bbb5-2dff-4721-8261-a4ccff24c81a&lw=1#");
    startTime = time.process_time()

    time.sleep(2)
    p_input = driver.find_element(By.ID, 'i0116')
    p_input.send_keys(admin)

    p_btn = driver.find_element(By.ID, 'idSIButton9')
    p_btn.click()

    p_input = driver.find_element(By.ID, 'i0118')
    p_input.send_keys(passwd)

    time.sleep(2)
    p_btn = driver.find_element(By.ID, 'idSIButton9')
    p_btn.click()

    time.sleep(2)
    p_btn = driver.find_element(By.ID, 'idSIButton9')
    p_btn.click()

    for _ in range(10):
        for x in range(number_of_strings):
            # 生成随机字符串
            txt = ''.join(random.SystemRandom().choice(
                string.ascii_letters + string.digits) for _ in range(length_of_string))

        # 输入
        time.sleep(2)
        driver.get(
            "https://cn.bing.com/search?q=&go=%E6%90%9C%E7%B4%A2&qs=ds&form=QBRE")
        p_input = driver.find_element(By.ID, 'sb_form_q')
        p_input.send_keys(txt)

        # 搜索
        time.sleep(8)
        p_btn = driver.find_element(By.ID, 'search_icon')
        p_btn.click()
        score = driver.find_element(By.ID, 'id_rc')

        time.sleep(3)

        endTime = time.process_time()
        runTime = endTime - startTime
        rebackMsg = "###   Score: " + score.text + "     ###"

        print(rebackMsg)
        print("###  Cosume: {} ms     ###".format(runTime*1000))
        print(term)
        print("                    ")
    driver.close()
