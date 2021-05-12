from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from multiprocessing import Pool
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re 
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

cwd = os.getcwd()

opts = Options()
opts.headless = False
opts.add_argument('log-level=3') 
opts.add_argument("--start-maximized")
dc = DesiredCapabilities.CHROME
dc['loggingPrefs'] = {'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}

opts.add_argument('--disable-blink-features=AutomationControlled')
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
path_browser = f"{cwd}\chromedriver.exe"

def login_twitter(k):
    global browser
    global email
    global password
    k = k.split("|")
    email = k[0]
    password = k[1]
     
    
    browser = webdriver.Chrome(options=opts, desired_capabilities=dc, executable_path=path_browser)
    browser.get("https://twitter.com/login")
    print(f"[*] [ {email} ] Please wait, trying to login twitter!")
    sleep(3)
     
    element = wait(browser,35).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')))
    element.send_keys(email)
    sleep(0.5)
    element = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')))
    element.send_keys(password)
    sleep(0.5)
    wait(browser,10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span'))).click()
    
    sleep(3)
    file_caption = "caption.txt"
    file_caption_get = open(f"{cwd}/{file_caption}","r")
    caption = file_caption_get.read()
    if "/login" in browser.current_url:
        get_warn = wait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/span'))).text
        print(f"[*] {get_warn}")
        print(f"[*] [ {email} ] Failed Login")
        with open('failedLoginTwitter.txt','a') as f:
            f.write('{0}|{1}\n'.format(email,password))
        browser.quit()
    else:
        print(f"[*] [ {email} ] Success Login")
        file_lists = "url_input.txt"
        myfiles = open(f"{cwd}/{file_lists}","r")
        list_accounts = myfiles.read()
        url = list_accounts.split("\n")
        browser.get(url[0])
        sleep(1) 
        if "/status/" in browser.current_url:
            username_url = wait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/a/div/div[1]/div[1]/span/span')))
            
            username_url.click()
            username_get = wait(browser, 15).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div/span'))).text
            try:
                click_follow = wait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(2) > div > div > div:nth-child(1) > div.css-1dbjc4n.r-1ifxtd0.r-ymttw5.r-ttdzmv > div.css-1dbjc4n.r-obd0qt.r-18u37iz.r-1w6e6rj.r-1wtj0ep > div > div:nth-child(2) > div > div > div > span > span'))) 
                click_follow.click()
                print(f"[*] [ {email} ] [ {username_get} ] Success Follow!")
                sleep(1)
            except:
                print(f"[*] [ {email} ] [ {username_get} ] Followed!")
            #https://twitter.com/Airdropfindx
            get_notif_pinned = wait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/span')))
            browser.execute_script("arguments[0].scrollIntoView();", get_notif_pinned)
            notif_pinned = get_notif_pinned.text
            print(f"[*] [ {email} ] [ {username_get} ] Have a {notif_pinned}")
            wait(browser,20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]'))).click()

            sleep(1)
            # try_retweet = wait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[3]/div[5]/div[2]/div/div')))
             
            # sleep(2)
            # try_retweet.click()
            
            
            if len(caption) > 1:
                try_love = wait(browser,20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[3]/div[5]/div[3]/div/div'))).click()
                print(f"[*] [ {email} ] [ {username_get} ] Success Love")
                sleep(1)
                try_retweet =  wait(browser,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.css-18t94o4[data-testid ="retweet"]'))).click()
                sleep(1)
                try_quote = wait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div[2]/div[3]/div/div/div/a'))).click()
                sleep(1)
                try_fill_caption = wait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/div/div/div')))
                try_fill_caption.send_keys(caption)
                submit_tweet = wait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div/div/span/span'))) 
                try:
                    browser.execute_script("arguments[0].scrollIntoView();", submit_tweet)
                    sleep(1)
                    submit_tweet.click()
                except:
                    submit_tweet.click()
                sleep(1)
                
                print(f"[*] [ {email} ] [ {username_get} ] Success Retweet Caption")
            else:
                try_love = wait(browser,20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[3]/div[5]/div[3]/div/div'))).click()
                print(f"[*] [ {email} ] [ {username_get} ] Success Love")
                try_retweet =  wait(browser,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.css-18t94o4[data-testid ="retweet"]'))).click()
                sleep(1)
                try_retweet_confirm =  wait(browser,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.css-1dbjc4n[data-testid ="retweetConfirm"]'))).click()
                print(f"[*] [ {email} ] [ {username_get} ] Success Retweet")

                
        else:
            try:
                username_get = wait(browser, 0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div/span'))).text
            except:
                pass
                
            try:
                click_follow = wait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(2) > div > div > div:nth-child(1) > div.css-1dbjc4n.r-1ifxtd0.r-ymttw5.r-ttdzmv > div.css-1dbjc4n.r-obd0qt.r-18u37iz.r-1w6e6rj.r-1wtj0ep > div > div:nth-child(2) > div > div > div > span > span'))) 
                click_follow.click()
                print(f"[*] [ {email} ] [ {username_get} ] Success Follow!")
                sleep(2)
            except:
                print(f"[*] [ {email} ] [ {username_get} ] Followed!")
 
            get_notif_pinned = wait(browser, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/span')))
            browser.execute_script("arguments[0].scrollIntoView();", get_notif_pinned)
            notif_pinned = get_notif_pinned.text
            print(f"[*] [ {email} ] Have a {notif_pinned}")
            wait(browser,20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]'))).click()
     
            sleep(1)
             
            if len(caption) > 1:
                sleep(1)
                try_love = wait(browser,20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[3]/div[5]/div[3]/div/div'))).click()
                print(f"[*] [ {email} ] [ {username_get} ] Success Love")
                sleep(0.5)
                try_retweet =  wait(browser,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.css-18t94o4[data-testid ="retweet"]'))).click()
                sleep(1)
                try_quote = wait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div[2]/div[3]/div/div/div/a'))).click()
                sleep(1)
                try_fill_caption = wait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/div/div/div')))
                try_fill_caption.send_keys(caption)
                submit_tweet = wait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div/div/span/span'))) 
                try:
                    browser.execute_script("arguments[0].scrollIntoView();", submit_tweet)
                    sleep(1)
                    submit_tweet.click()
                except:
                    submit_tweet.click()
                sleep(1)
              
                print(f"[*] [ {email} ] [ {username_get} ] Success Retweet Caption")
            else:
                try_love = wait(browser,20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[3]/div[5]/div[3]/div/div'))).click()
                print(f"[*] [ {email} ] [ {username_get} ] Success Love")
                try_retweet =  wait(browser,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.css-18t94o4[data-testid ="retweet"]'))).click()
                sleep(1)
                try_retweet_confirm =  wait(browser,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.css-1dbjc4n[data-testid ="retweetConfirm"]'))).click()
                print(f"[*] [ {email} ] [ {username_get} ] Success Retweet")
        browser.quit() 

if __name__ == '__main__':
    global list_accountsplit
    global k
    print("[*] Automation Twitter Tools")
    print("[*] Author: RJD")
    url_input = input("[*] Input URL: ")
    with open('url_input.txt','w') as f:
        f.write('{0}\n'.format(url_input))
    input_caption = input("[*] Input Quotes Retweet (No Quotes? Just Enter): ")
    with open('caption.txt','w') as f:
        f.write('{0}\n'.format(input_caption))
    jumlah = int(input("[*] Multi Proccessing: "))
    file_list = "twitter.txt"
    
    myfile = open(f"{cwd}/{file_list}","r")
    list_account = myfile.read()
    list_accountsplit = list_account.split() 
    with Pool(jumlah) as p:  
        p.map(login_twitter, list_accountsplit)
