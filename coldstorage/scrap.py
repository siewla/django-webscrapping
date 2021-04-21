import requests
from bs4 import BeautifulSoup

url = "https://coldstorage.com.sg/search?q=peanuts"

page = requests.get(url)
# print(page.content)

parsed_html = BeautifulSoup(page.content, "html.parser")
# print(parsed_html)

list_of_items = parsed_html.find_all("div", class_="product_box")
# print(list_of_items)

final_list_of_items = []

for item in list_of_items:
    item_price = item.find('div',class_="price_now").text
    item_name = item.find('div', class_="product_name").text
    item_category = item.select(".category-name > b")
    item_size = item.find('span', class_="size").text
    item_image = item.find("img").get("src")
    item_details = {"price":item_price, "name":item_name, "category":item_category, "size":item_size, "image":item_image}
    print(item_details)
    