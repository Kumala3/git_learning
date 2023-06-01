import requests
from bs4 import BeautifulSoup

url = 'https://funpay.com/chips/99/' # берем ссылку сайта которого хотим парсить
take_request = requests.get(url).text # посылаем запрос на сайт
count_people = int(input('Введите сколько человек вы хотите спарсить: '))
soup = BeautifulSoup(take_request, 'lxml')

# Функция парсит количевство отзывов у продавца
def get_count_reviews():
    reviews = soup.find_all('div', class_="media-user-reviews")
    text_reviews = []
    for review in reviews[:count_people + 1]:
        content = review.get_text().strip()
        if content == 'нет отзывов':
            text_reviews.append('0')
        else:
            text_reviews.append(content)
    return text_reviews

# Функция парсит количевтсво доступных робуксов у продавца
def get_robux_stoc():
    values = []
    count_value = soup.find_all('div', class_="tc-amount")
    for value in count_value[:count_people + 1]:
        robux_value = value.get_text().strip()
        if robux_value != 'Наличие':
            values.append(robux_value)
    return values

# Функция парсит цену за 1 робукс у продавца
def get_price_robux():
    prices = []
    price_rob = soup.find_all('div', class_="tc-price")
    for price in price_rob[:count_people + 1]:
        robux_price = price.get_text().strip()
        if robux_price != 'Цена':
            prices.append(robux_price)
    return prices

# Функция парсит ссылку на продавца
def get_user_link():
    links = []
    links_users = soup.find_all('div', class_="avatar-photo")
    for linki in links_users[:count_people]:
        link_user = linki.get('data-href').strip()
        links.append(link_user)

    return links

# Функция парсит сколько продавец уже торгует на бирже
def get_reg_data():
    regs_dates = []
    datas = soup.find_all('div', class_ = "media-user-info")
    for data in datas[:count_people+1]:
        daty = data.get_text()
        regs_dates.append(daty)

    return regs_dates

# Основная функция с которой мы работаем
def main():
        reviews = get_count_reviews()
        robux = get_robux_stoc()
        robux_price = get_price_robux()
        user_linkt = get_user_link()
        data_reg_user = get_reg_data()

        for review, value, price, user_link, reg_user in zip(reviews, robux, robux_price, user_linkt, data_reg_user):
            print(f'Отзывы: {review}//Доступно робуксов: {value}//Цена за 1 rb: {price}//Ссылка на профиль: {user_link} //Дата регистрации: {reg_user}')

if __name__ == '__main__':
    main()







