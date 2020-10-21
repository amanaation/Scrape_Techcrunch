import os
import pandas as pd
import regex

from selenium import webdriver


class Articles:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("start-maximized")
        self.options.add_argument('disable-infobars')
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.previous_articles = self.get_displayed_articles()

    def check_file_exists(self, path):
        return os.path.exists(path)

    def get_displayed_articles(self):
        if not self.check_file_exists("articles.csv"):
            pd.DataFrame(columns=["title_text", "date_of_publishing",
                                  "article_full_url", "image_urls"]).to_csv(
                "articles.csv", index=False)
        previous_articles = pd.read_csv("articles.csv")["title_text"].to_list()

        return previous_articles

    def get_currency(self, value):
        temp = regex.findall(r'\p{Sc}', value)
        return temp

    def get_new_articles(self):
        driver = self.driver
        driver.get("https://techcrunch.com/startups/")
        driver.implicitly_wait(5)
        new_article = {"title_text": [], "date_of_publishing": [],
                       "article_full_url": [], "image_urls": []}

        while len(new_article["title_text"]) < 50:
            article_blocks = driver.find_elements_by_tag_name("article")[len(new_article["title_text"]):]
            for article in article_blocks:
                if len(new_article["title_text"]) >= 50:
                    break
                title = article.find_element_by_class_name("post-block__title__link")
                title_text = title.text
                currency = self.get_currency(title_text)
                if currency != []:
                    if title_text not in self.previous_articles:
                        date_of_publishing = article.find_element_by_tag_name("time").text.replace("•", ", ")
                        article_full_url = article.find_element_by_tag_name("a").get_property("href")
                        img_urls = [article.find_element_by_tag_name("img").get_property("src"),
                                    article.find_element_by_tag_name("img").get_property("srcset")]

                        new_article["title_text"].append(title_text)
                        new_article["date_of_publishing"].append(date_of_publishing)
                        new_article["article_full_url"].append(article_full_url)
                        new_article["image_urls"].append(", ".join(img_urls))
            driver.find_element_by_class_name("load-more ").click()
            driver.implicitly_wait(4)
        self.write_to_file(new_article)

    def write_to_file(self, new_article):
        new_article = pd.DataFrame(new_article)
        existing_article = pd.read_csv("articles.csv")
        new_article = pd.concat([existing_article, new_article])
        new_article.to_csv("articles.csv", index=False, header=True)

if __name__ == "__main__":
    art = Articles()
    art.get_new_articles()
