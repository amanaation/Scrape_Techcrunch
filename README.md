# Scrape_Techcrunch

## Installation

1. Clone the repository to your local repository.
2. Run the following command, to install required dependencies
  ```pip install -r requirements.txt```

## Usage:

Execute scrape_techcrunch.py

## How it Works:

The Article class has the following methods : 

1. get_displayed_articles : This function will check if the file articles.csv exists or not. If it doesnt exists, then it means then this is the first time that the article is 
being displayed for the first time. In taht case a blank articles.csv file is created with required columns. This function return previously scraped articles list if the file is
already present or an empty list if file does not exists.
