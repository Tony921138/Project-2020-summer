import json
import html
from bs4 import BeautifulSoup

with open('product_info_NY1(Final).json', 'r', encoding = 'utf-8') as results:
    results_list = json.loads(results.read())

prod_count = 0

# 整理商品名稱
def clean_name(product):                                      
    product['name'] = BeautifulSoup(product['name'], 'lxml').text
    product['name'] = product['name'].replace('&amp;', '&')

# 整理商品價格
def clean_price(product):
    keyword_list = []
    price_list = []        
    if '$' in product['price']:                                   
        product['price'] = product['price'].replace('$', '')
        if '-' in product['price']:                               
            product['price'] = (float(product['price'].partition(' - ')[0]) + float(product['price'].partition(' - ')[2])) / 2
     
    product['price'] = round(float(product['price']), 2)

# 整理星星數        
def clean_star_ratings(product):
    product['star_ratings'] = tuple(product['star_ratings'])
    product['star_ratings'][1] = float(product['star_ratings'][1])

# 整理highlights
def clean_highlights(product):
    for i in product['highlights']:
        i  = BeautifulSoup(i, 'lxml').text
        i = i.replace('\n', '').replace('●', '').replace('*', '').replace('|', '').replace('see nutrition information for Saturated Fat, and Sodium content', '')

# 整理specifications
def clean_specifications(product):
    if product['specifications'] != 'NA':
        for k, v in product['specifications'].items():
            v = v.strip(' ')
            if k == 'Net weight':
                v = v.strip(' ')
                v = (float(v.partition(' ')[0]), v.partition(' ')[2].lower())

# 主程式進入點
if __name__ = '__main__':
    for product in results_list:
        clean_name(product)
        clean_price(product)
        clean_star_ratings(product)
        clean_highlights(product)
        clean_specifications(product)
        
        with open('product_info_NY1_clean', 'a', encoding = 'utf-8') as f:
            json.dump(product, f, indent = 4, ensure_ascii = False)
        
        prod_count += 1
        
    print(prod_count)   
