from bs4 import BeautifulSoup
import datetime
import requests
import time


def scrape_books():
    page = requests.get("http://books.toscrape.com/").text
    # print(page) Prints the response to the request <Response [200] means Successful>

    soup = BeautifulSoup(page, 'lxml')
    # print(soup)

    '''

    book = soup.find('article', class_="product_pod")
    book_name = book.find('h3').find('a').get('title')
    print(book_name)
    book_price = book.find('p', class_='price_color').text[1:]  # shows text from index[1]
    print(book_price)

    # to get ratings, we went to find 'p' of class 'star-rating' and get that class name<['star-rating','Three]> to index[1]
    rating = book.find('p', class_='star-rating').get('class')[1]
    print(f'{rating} Stars')

    '''

    books = soup.find_all('article', class_="product_pod")

    for book in books:
        book_name = book.find('h3').find('a').get('title')
        rating = book.find('p', class_='star-rating').get('class')[1]
        book_price = book.find('p', class_='price_color').text[1:]
        more_info = book.h3.a['href']

        print(f'Name: {book_name} \nRating: {rating} \nPrice: {book_price} \nMore Info: {more_info}')
        print("")


scrape_books()

'''
if __name__ == '__main__':
    scrape_books()
    time.sleep()
'''