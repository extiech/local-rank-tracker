import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def scrape_google_maps_results(search_query, location, num_scrolls=5):
    """
    Scrapes Google Maps for a given search query and location.

    Args:
        search_query (str): The business or keyword to search for (e.g., "plumber").
        location (str): The geographic location for the search (e.g., "New York, NY").
        num_scrolls (int): The number of times to scroll down to load more results.
    """
    
    # Set up Selenium WebDriver
    # webdriver_manager automatically handles the Chrome driver installation
    try:
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    except Exception as e:
        print(f"Error setting up the WebDriver: {e}")
        print("Please make sure you have Google Chrome installed.")
        return

    # Navigate to Google Maps
    print("Navigating to Google Maps...")
    driver.get("https://www.google.com/maps")
    time.sleep(3) # Wait for the page to load

    # Find the search box and input the query
    try:
        search_box = driver.find_element(By.ID, "searchboxinput")
        search_box.send_keys(f"{search_query} in {location}")
        search_box.send_keys(Keys.ENTER)
        time.sleep(5) # Wait for search results to load
    except Exception as e:
        print(f"Could not find search box: {e}")
        driver.quit()
        return

    # Scroll to load more results
    print("Scrolling to load more results...")
    scrollable_panel = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Results for restaurant in new york ny']")
    for _ in range(num_scrolls):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_panel)
        time.sleep(2) # Give the page time to load new content

    # Get the page source and parse it with BeautifulSoup
    print("Parsing page content...")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    # Quit the driver to close the browser
    driver.quit()

    # Find and extract data for each business
    results = []
    # This class may change, so you might need to inspect the page to find the correct one
    business_listings = soup.find_all("div", class_="hfpxzc")
    
    if not business_listings:
        print("No business listings found with the specified class. The class name might have changed.")
        return []

    for idx, listing in enumerate(business_listings):
        try:
            name = listing.get('aria-label')
            
            # Extract other details if needed, for example:
            # rating_element = listing.find("span", class_="MW4etd")
            # rating = rating_element.text if rating_element else "N/A"
            # review_count_element = listing.find("span", class_="UY7F9")
            # review_count = review_count_element.text if review_count_element else "N/A"

            results.append({
                "rank": idx + 1,
                "name": name,
                # "rating": rating,
                # "review_count": review_count
            })
            
        except Exception as e:
            print(f"Error extracting data for a listing: {e}")
            continue

    return results

def save_to_csv(data, filename="google_maps_ranks.csv"):
    """Saves the scraped data to a CSV file."""
    if not data:
        print("No data to save.")
        return

    print(f"Saving data to {filename}...")
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print("Data saved successfully.")

if __name__ == "__main__":
    search = "restaurants"
    loc = "New York, NY"
    scraped_data = scrape_google_maps_results(search, loc)
    if scraped_data:
        save_to_csv(scraped_data)
        print("Scraping complete!")
    else:
        print("Scraping failed or no results found.")

