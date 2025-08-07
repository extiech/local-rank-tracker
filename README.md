Google Maps Local Rank Scraper
==============================

### Description

This Python script is a tool for scraping business listings from Google Maps. It's designed to help with local SEO rank tracking by automating searches for a specific keyword in a given location, extracting business names and their corresponding rank, and saving the results to a CSV file.

The script uses **Selenium** to control a web browser, allowing it to handle the dynamic content on Google Maps. It then uses **Beautiful Soup** to parse the page content and extract the relevant business information.

### Prerequisites

Before running the script, you need to have Python installed on your system. You'll also need to install the necessary Python libraries.

Install the required libraries using pip:

    pip install selenium
    pip install beautifulsoup4
    pip install webdriver-manager
    

### How to Use

1.  **Open the Script:** Make sure you have the Python script saved as a file (e.g., `google_maps_scraper.py`).
    
2.  **Edit the Configuration:** Open the script and modify the `search` and `loc` variables in the `if __name__ == "__main__":` block to match your desired search query and location.
    
        if __name__ == "__main__":
            search = "plumber"  # Your desired search query
            loc = "London, UK"  # Your desired location
            scraped_data = scrape_google_maps_results(search, loc)
            if scraped_data:
                save_to_csv(scraped_data)
                print("Scraping complete!")
            else:
                print("Scraping failed or no results found.")
        
    
3.  **Run the Script:** Execute the script from your terminal:
    
        python google_maps_scraper.py
        
    
4.  **View Results:** A new CSV file named `google_maps_ranks.csv` will be created in the same directory as your script, containing the scraped data.
    

### Troubleshooting

*   **"Error setting up the WebDriver":** Ensure you have Google Chrome installed on your machine. The `webdriver-manager` library will automatically download and set up the correct driver for you.
    
*   **"No business listings found":** This can happen if Google changes the class names of the HTML elements. You may need to inspect the Google Maps page to find the current class name for business listings and update the `soup.find_all("div", class_="hfpxzc")` line in the script.
    
*   **The browser opens but nothing happens:** The website might have a cookie consent pop-up or other modal dialogs that need to be handled. You might need to add a `try/except` block to find and click the accept button.
    

### What the Script Extracts

Currently, the script extracts the following information:

*   **Rank:** The position of the business in the search results.
    
*   **Name:** The name of the business.
    

The script also contains commented-out lines to demonstrate how you could expand it to scrape ratings and review counts as well.


### Local Rank Tracking Tools

For a more complete and robust local rank tracking solution, professional tools such as [GMBRadar](https://www.gmbradar.com/) are available that offer features far beyond what this simple script provides. These services often include:

*   Geogrid rank tracking (visualizing rankings on a map)
    
*   Automated daily or weekly scans
    
*   Tracking of multiple keywords and locations
    
*   Competitor analysis
    
*   Integration with other SEO and marketing platforms
    
