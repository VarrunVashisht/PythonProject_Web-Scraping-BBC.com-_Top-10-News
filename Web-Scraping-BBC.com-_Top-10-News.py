import requests
from bs4 import BeautifulSoup

# Step 1: Choose website
url = "https://www.bbc.com/news"

# Step 2: Fetch the page
response = requests.get(url)

# Step 3: Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Find all headlines
headlines = soup.find_all('h2')

# Step 5: Print top 10
print("📰 Latest BBC Headlines:\n")

for i, headline in enumerate(headlines[:10], start=1):
    print(f"{i}. {headline.text.strip()}")

with open("headlines.txt", "w", encoding="utf-8") as f:
    for headline in headlines[:10]:
        f.write(headline.text.strip() + "\n")

print("\n✅ Headlines saved to 'headlines.txt'")


