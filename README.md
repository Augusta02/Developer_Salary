# AI/ML with Python : WebScraping and Sentiment Analyis with Natural Language Processing Bounty

In this campaign, we continue our journey into the realm of natural language processing (NLP)! Building on our foundational insights from our previous campaign on NLP, we'll delve deeper into the significance of NLP across various sectors.

Sentiment analysis stands out as a pivotal application, empowering businesses, politicians, and marketers to gauge public sentiments and perceptions about products or figures. This campaign will equip you with crucial tools: from data harvesting via web scraping to sentiment analysis leveraging Python's native libraries.

## First Task 
- Webscraping with Urllib, Beautiful Soup and Selenium

Pseudocode for Scraping 
python
1. Start Selenium WebDriver (e.g., ChromeDriver).
2. Navigate to the initial page.

LOOP:
3.   Locate the 'Next' button using a XPath Selector.
4.   Click on the 'Next' button.

5.   Wait for the page to load (use implicit or explicit waits as needed).

6.   Get the URL of the current page.
7.   Print or store the URL for further use.

8.   Use BeautifulSoup to scrape quotes on the current page:
       a. Locate the HTML elements containing quotes using appropriate HTML tags and attributes.
       b. Extract and print the text content of each quote.

9.   Check if there is another 'Next' button on the page (to determine if there are more pages).
10.  If another 'Next' button is found, go back to step 3.
11.  If no 'Next' button is found, exit the loop.

12. Close the Selenium WebDriver.
