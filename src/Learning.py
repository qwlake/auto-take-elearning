# -*- coding: utf-8 -*-
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from contextlib import contextmanager


class Learning():
    def __init__(self, user_id, pw, cource_name, section=0, playback_rate=16):
        driver = None
        if not driver:
            try:
                driver = webdriver.Chrome(executable_path="chromedriver/chromedriver80.exe")
            except:
                print("chromedriver80 fail")
        html = driver.page_source
        #soup = BeautifulSoup(html, "html.parser")
        self.user_id = user_id
        self.pw = pw
        self.driver = driver
        self.cource_name = cource_name
        self.section = section
        self.playback_rate = playback_rate # max 16

    @contextmanager
    def wait_for_new_window(self, driver, timeout=10):
        handles_before = driver.window_handles
        yield
        WebDriverWait(driver, timeout).until(
            lambda driver: len(handles_before) != len(driver.window_handles))

    def learn(self):
        driver = self.driver
        driver.get("http://eruri.kangwon.ac.kr")    # 페이지 열기
        WebDriverWait(driver, 600).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        driver.find_element_by_id("username").send_keys(self.user_id)    # 로그인
        driver.find_element_by_id("password").send_keys(self.pw)
        driver.find_element_by_tag_name("Button").click()
        WebDriverWait(driver, 600).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".close_notice"))
        )
        close_notices = driver.find_elements_by_class_name("close_notice")
        for i in range(len(close_notices)): # 공지창 닫기
            close_notices[-i-1].click()
        courses = driver.find_elements_by_class_name("course_link") # 과목 목록 받아오기
        title_list = driver.find_elements_by_xpath("//div[@class='course-title']//h3")
        for i, title in enumerate(title_list):
            if self.cource_name in title.text:
                courses[i].click()         # 과목 클릭
                break

        if self.section == 0:    # 현재 주차 강의 목록
            links = driver.find_elements_by_xpath("//div[@class='course_box course_box_current']//li[@class='activity vod modtype_vod ']//a[*]")  # 현제 강의 링크 목록
        else:   # 특정 주차 강의 목록
            links = driver.find_elements_by_xpath("//li[@id='section-" + self.section + "']//li[@class='activity vod modtype_vod ']//a[*]")  # n주차 강의 링크 목록

        for link in links:
            link.click()    # 강의 클릭
            driver.switch_to.window(driver.window_handles[-1])  # 오픈된 강의 창으로 포커스 이동
            
            element = WebDriverWait(driver, 600).until(
                EC.presence_of_element_located((By.CLASS_NAME, "jw-video"))
            )
            element.click() # 동영상 재생
            time.sleep(3)
            driver.execute_script("(function(){let x=document.querySelector('video');x.playbackRate=x.playbackRate!=1?1:"+str(self.playback_rate)+";})();") # 동영상 배속
            while True: # 재생완료 체크
                try:
                    time.sleep(1)
                    driver.find_element_by_class_name("jw-state-complete")
                    break
                except:
                    pass
            time.sleep(3)
            driver.close()  # 동영상 창 닫기
            driver.switch_to.window(driver.window_handles[-1])  # 메인 창으로 포커스 이동

        driver.close()

if __name__ == '__main__':
    learn = Learning(sys.argv[1], sys.argv[2], sys.argv[3])
    learn.learn()