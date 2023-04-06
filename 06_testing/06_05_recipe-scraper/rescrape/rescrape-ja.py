import requests
from bs4 import BeautifulSoup


BASE_URL = "https://woven-dojo.github.io/recipes/"

def get_page_content(url):
    """URLへのHTTP呼び出しによる応答を取得します。"""
    page = requests.get(url)
    return page

def get_html_content(url):
    """ページのHTMLを取得します。"""
    html = get_page_content(url).text
    return html

def make_soup(html):
    """HTML文字列をBeautifulSoupオブジェクトに変換します。"""
    soup = BeautifulSoup(html, "html.parser")
    return soup

def get_recipe_links(soup):
    """bs4オブジェクトを指定して、ページにあるすべてのリンクのURLを抽出します。"""
    links = [link["href"] for link in soup.find_all("a")]
    return links

def get_author(soup):
    """レシピの作成者名を抽出します。"""
    author = soup.find("p", class_="author").text.strip("by ")
    return author

def get_recipe(soup):
    """bs4オブジェクトのレシピテキストを抽出します。"""
    recipe = soup.find("div", class_="md").text
    return recipe

# breakpoint()

if __name__ == "__main__":
    index_html = get_html_content(BASE_URL)
    index_soup = make_soup(index_html)
    recipe_links = get_recipe_links(index_soup)
    # breakpoint()

    for r_link in recipe_links:
        URL = f"{BASE_URL}/{r_link}"
        soup = make_soup(get_html_content(URL))
        # breakpoint()
        author = get_author(soup)
        recipe = get_recipe(soup)
        print(f"({author})\t[{recipe}]\n\n\n")
