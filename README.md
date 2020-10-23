# Scrape_Techcrunch

## Installation

1. Download and Install Python 3.7.5
2. Download ChromeDriver 86.0.4240.22 from : ``` https://sites.google.com/a/chromium.org/chromedriver/downloads```
3. Clone the repository to your local repository.
4. Run the following command, to install required dependencies
  ```pip install -r requirements.txt```
5. Place the downloaded ChromeDriver in the cloned github project folder

## Usage:

1. Open your command prompt and cd to your cloned directory.
2. Type following command in your cmd : 
    ``` python scraping_api.py ```
3. Open your browser and type the following url : 
    ```http://localhost:5000/```

## How it Works:

The Article class has the following important methods : 

1. get_displayed_articles : This function will check if the file articles.csv exists or not. If it doesnt exists, then it means then this is the first time that the article is 
being displayed for the first time. In taht case a blank articles.csv file is created with required columns. This function return previously scraped articles list if the file is already present or an empty list if file does not exists.

2. currency_present(title_text) : This is one of the most important function. It determines whether the title is related to fund raising or not. If there is a currency present in the title then the articles is related to fund raising, or else it isn't. Since a vast majprity of fund raising articles will have a currrency in their articles.

3. get_new_articles(): This is the main function, which scrapes the data. If after scraping if we get 50 articles related to fund raising then it calls the write function. Or else it clicks on Load More button and repeats the same process until we get 50 articles related to fundraising.
