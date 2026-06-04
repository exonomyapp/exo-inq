import sys
import json
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def search(query):
    with sync_playwright() as p:
        # Use a realistic User-Agent to avoid immediate blocking
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
        page = context.new_page()
        
        # Navigate to Yandex and perform search
        search_url = f"https://yandex.com/search/?text={query.replace(' ', '+')}"
        page.goto(search_url)
        
        # Wait for results to load - Yandex results often use class 'serp-item'
        try:
            page.wait_for_selector('.serp-item', timeout=30000)
        except Exception as e:
            # If selector fails, print the first 500 chars to help debugging
            print(json.dumps({"error": f"Timeout waiting for Yandex results: {str(e)}", "debug": page.content()[:500]}))
            browser.close()
            sys.exit(1)
        
        content = page.content()
        browser.close()
        
        soup = BeautifulSoup(content, 'html.parser')
        results = []
        # Extract results based on Yandex's structure
        for item in soup.select('.serp-item'):
            title_tag = item.select_one('h2 a')
            snippet_tag = item.select_one('.serp-item__text')
            
            if title_tag and snippet_tag:
                results.append({
                    "title": title_tag.get_text(),
                    "link": title_tag['href'],
                    "snippet": snippet_tag.get_text()
                })
        
        return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No query provided"}))
        sys.exit(1)
        
    query = " ".join(sys.argv[1:])
    try:
        results = search(query)
        print(json.dumps(results, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)
