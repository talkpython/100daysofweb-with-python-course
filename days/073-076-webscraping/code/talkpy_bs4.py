import requests
import bs4

URL = "https://training.talkpython.fm/courses/all"
header_list = []

def main():
    raw_site_page = requests.get(URL)
    raw_site_page.raise_for_status()

    soup = bs4.BeautifulSoup(raw_site_page.text, 'html.parser')
    html_header_list = soup.select('h3')
    for headers in html_header_list:
        header_list.append(headers.getText())
    for headers in header_list:
        print(headers)

if __name__ == "__main__":
    main()
