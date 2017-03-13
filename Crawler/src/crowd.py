#! /usr/bin/env python2.7
# coding=utf-8
__author__ = 'bulu_dog'
from selenium import webdriver
import config
import requests
import time
import urllib  # 1 import urlparse
import json

driver = None

def init():
    global driver
    driver = webdriver.Firefox()

def login():
    driver.get("https://login.taobao.com/member/login.jhtml?spm=a21bo.7724922.1997563269.1.vUMIJx&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F")
    for key, value in config.Cookies.items():
        driver.add_cookie(dict(name=key, value=value))
    driver.get("https://login.taobao.com/member/login.jhtml?spm=a21bo.7724922.1997563269.1.vUMIJx&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F")
    driver.find_element_by_name("TPL_password").send_keys("XXXUserNameXXX")
    driver.maximize_window()
    driver.find_element_by_id("J_SubmitStatic").click()
    time.sleep(1)
    while(1):
        try:
            driver.find_element_by_class_name("search-combobox-input-wrap")
            break
        except Exception:
            print("请手动登陆！")
            time.sleep(5)

def search(query, page):
    f = open("url.txt", "w")
    input = driver.find_element_by_tag_name("input")
    input.send_keys(query)
    driver.find_element_by_class_name("btn-search").click()

    while(page > 0):
        time.sleep(1)
        page = page - 1
        items = driver.find_elements_by_class_name("J_U2IStat")
        for item in items:
            f.write(item.get_attribute("href") + "\n")
        driver.find_element_by_link_text("下一页").click()
    f.close()

def get_info(url):
    driver.get(url)
    if "tmall" not in driver.current_url:
        j = dict()
        # 标题
        j["title"] = driver.find_element_by_class_name("tb-main-title").text

        # 获取图片URL
        urls = []
        for image in driver.find_element_by_id("J_UlThumb").find_elements_by_tag_name("img"):
            iurl = image.get_attribute("src")
            iurl = iurl[0:iurl.find(".jpg")+4]
            urls.append(iurl)
        j["img"] = urls

        # id
        id = None
        if "id" in driver.current_url:
            # url 中有id字段
            current = urllib.parse.urlparse(driver.current_url)       #urlparse.urlparse(driver.current_url)
            id = urllib.parse.parse_qs(current.query, True)["id"][0]   #urlparse.parse_qs(current.query, True)
        else:
            # 没有id字段
            id = driver.current_url
        j["id"] = id

        # 参数：
        attributes = []
        for li in driver.find_element_by_class_name("attributes-list").find_elements_by_tag_name("li"):
            attributes.append(li.text)
        j["attributes"] = attributes

        jstring = json.dumps(j)
        out = open("../data/" + id + ".txt", "w")
        out.write(jstring)

    else:
        print("天猫产品暂时跳过")

def get_image(image_url, filename):
    r = requests.get(image_url, stream=True)
    with open(filename, "wb") as f:
        for chunk in r.iter_content():
            f.write(chunk)

def close():
    global driver

import json
# d = loads(string)
# d["id"]
# d["imgs"]

if __name__ == "__main__":
    init()
    login()
    # search(u"来自星星的你", 50)
    # 读取文件，一行一个url
    get_info("https://click.simba.taobao.com/cc_im?p=%C0%B4%D7%D4%D0%C7%D0%C7%B5%C4%C4%E3&s=349812704&k=385&e=gcm1eV0dR9g8zlk7KJIljQJaUYQ8fPNbPybjoUaorWPAu8%2FrmxXnK7E%2Fa09gDkJmFy%2BG2uzZazEKawVW5uTVsN%2BmmodseKsOr2wR3ub3UTFUnakrBZbJV5EK%2BRtRqYHmhaq%2Bs6lnmlZjSqe7dmmetUdHJrdgUL%2FWycEfEoHxP3gxmy5tJ0dzMnA%2BweokUi4k2L6u47IX9zHlRpNq%2FRXUOJxDYRKyrD3puyG37Wi3oST%2F96jQOl4RRGJBgAVyQZkJXBeSUuTOG6xrE%2BlHaVXlbkmkMcENwXhyS2yCXKxXPjhmBznSI2HPkVQw7vUnNC4LxSUqmkYZWD3Jpm1%2BfzASnPnmof%2F94TANCJeak1i1rNgaaR%2Fe7HfyWSlx3ANgubjy")
    # get_image("http://gd2.alicdn.com/bao/uploaded/i2/TB1SPT7KVXXXXXzXFXXXXXXXXXX_!!0-item_pic.jpg", "1.jpg")
