from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('/Users/shoheihashimoto/MIRABELL/chromedriver')
driver.get('https://www.mirabell.co.jp/search/')

# element = driver.find_element_by_css_selector(".pager li a")
# 各物件にて行う処理
def each_property():
  element = driver.find_element_by_css_selector("#content01 h1")
  print(element.text)
  driver.back()

# 共通メソッド
# CSSのセレクタを引数として、そのオブジェクトをクリックする
def click_element_by_css_selector(css_selector):
  element = driver.find_element_by_css_selector(css_selector)
  element.click()

def is_property_page(url):
  return 'building' in url

# property_list_1 = [
#   "#content02 h2 a",
#   "#content02 article:nth-child(2) h2 a",
#   "#content02 font article h2 a",
#   "#content02 font font article h2 a",
#   "#content02 font font font article h2 a",
#   "#content02 font font font font article h2 a",
#   "#content02 font font font font article:nth-child(2) h2 a",
#   "#content02 font font font font article:nth-child(3) h2 a",
#   "#content02 font font font font font article h2 a",
#   "#content02 font font font font font font article h2 a"
#   ]

# property_list_2 = [
#   "#content02 h2 a",
#   "#content02 article:nth-child(2) h2 a",
#   "#content02 font article h2 a",
#   "#content02 font article:nth-child(2) h2 a",
#   "#content02 font article:nth-child(3) h2 a",
#   "#content02 font font article h2 a",
#   "#content02 font font article:nth-child(2) h2 a",
#   "#content02 font font font article h2 a",
#   "#content02 font font font article:nth-child(2) h2 a",
#   "#content02 font font font font article h2 a",
#   ]

elements = driver.find_elements_by_css_selector("#content02 a")
for index, element in enumerate(elements, 1):
  if is_property_page(element.get_attribute('href')):
    print(element.text)




# for index, property_selector in enumerate(property_list_1, 1):
#   print(index)
#   click_element_by_css_selector(property_selector)
#   each_property()

# # 次へ
# click_element_by_css_selector("#content01 .pager li a[title~=next]")
# click_element_by_css_selector("#content01 .pager li a[title~=next]")
# click_element_by_css_selector("#content01 .pager li a[title~=next]")
# click_element_by_css_selector("#content01 .pager li a[title~=next]")
# click_element_by_css_selector("#content01 .pager li a[title~=next]")
# click_element_by_css_selector("#content01 .pager li a[title~=next]")
# click_element_by_css_selector("#content01 .pager li a[title~=next]")
# click_element_by_css_selector("#content01 .pager li a[title~=next]")
# click_element_by_css_selector("#content01 .pager li a[title~=next]")
# click_element_by_css_selector("#content01 .pager li a[title~=next]")

# for index, property_selector in enumerate(property_list_1, 1):
#   print(index)
#   click_element_by_css_selector(property_selector)
#   each_property()

# for index, property_selector in enumerate(property_list_2, index):
#   print(index)
#   click_element_by_css_selector(property_selector)
#   each_property()

# # 次へ
# click_element_by_css_selector("#content01 .pager li a[title~=next]")

# for index, property_selector in enumerate(property_list_2, index):
#   print(index)
#   click_element_by_css_selector(property_selector)
#   each_property()
  

