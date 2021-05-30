from selenium import webdriver
from time import sleep
import re

driver = webdriver.Chrome('/Users/shoheihashimoto/MIRABELL/chromedriver')
driver.get('https://www.mirabell.co.jp/search/')

# 共通メソッド
# CSSのセレクタを引数として、そのオブジェクトをクリックする
def click_element_by_css_selector(css_selector):
  element = driver.find_element_by_css_selector(css_selector)
  element.click()

# URL先が物件情報ページかの判別式
# スクレイピング対象サイトの特性上、一部一致と末尾にスラッシュが入っていないことを確認する必要がある 
def is_property_page(url):
  pattern = re.compile(r'\d{2,5}$')
  if re.search('www.mirabell.co.jp/building/\d{2,5}', url) and pattern.search(url):
    return True

# 次のページへ遷移するメソッド
def go_next_page():
  click_element_by_css_selector("#content01 .pager li a[title~=next]")

# 各物件一覧ページでの処理
# 本メソッドは、物件一覧ページにて遷移先のリンクを取得する
def page_function(property_amount):
  elements = driver.find_elements_by_css_selector("#content02 a")
  links = []
  for index, element in enumerate(elements, 1):
    if is_property_page(element.get_attribute('href')):
      print(property_amount, element.text)
      # 物件先URL
      print(element.get_attribute('href'))
      links.append(element.get_attribute('href'))
      property_amount += 1
  return links, property_amount

# 各物件にて行う処理
def each_property():
  print("---- 物件情報 ----")
  element = driver.find_element_by_css_selector("#content01 h1")
  print("物件名", element.text)
  element = driver.find_elements_by_css_selector("#content01 p")
  print("物件概要")
  for p_tag_element in element:
    print(p_tag_element.text)
  print("---- 物件概要 ----")
  element = driver.find_element_by_css_selector("#content03 table tbody tr th")
  print(element.text, end=':')
  element = driver.find_element_by_css_selector("#content03 table tbody tr td")
  print(element.text)
  element = driver.find_element_by_css_selector("#content03 table tbody tr:nth-child(2) th")
  print(element.text, end=':')
  element = driver.find_element_by_css_selector("#content03 table tbody tr:nth-child(2) td")
  print(element.text)
  element = driver.find_element_by_css_selector("#content03 table tbody tr:nth-child(3) th")
  print(element.text, end=':')
  element = driver.find_element_by_css_selector("#content03 table tbody tr:nth-child(3) td")
  print(element.text)
  element = driver.find_element_by_css_selector("#content03 table tbody tr:nth-child(5) th")
  print(element.text, end=':')
  element = driver.find_element_by_css_selector("#content03 table tbody tr:nth-child(5) td")
  print(element.text)

  element = driver.find_elements_by_css_selector("#content01 p")
  print("---- 備考 ----")
  element = driver.find_element_by_css_selector("#content04 p")
  print("備考", element.text)
  print("---- 建物設備（共通部分） ----")
  element = driver.find_elements_by_css_selector("#content06 ul li")
  for li_tag_element in element:
    print(li_tag_element.text, end=' ')

  print("")
  print("")
  print("")
  print("")
  print("")
  print("")


# メイン処理
property_amount = 1
# TODO rangeを直すこと
for i in range(0, 1):
  property_link = page_function(property_amount)[0]
  print(property_link)
  for index, property_page in enumerate(property_link):
    driver.get(property_page)
    each_property()
    driver.back()
  go_next_page()

