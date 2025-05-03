import sys
import os
import requests
from bs4 import BeautifulSoup

def fetch_arxiv_metadata(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch URL: {url}")

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1", class_="title").text.replace("Title:", "").strip()
    authors = soup.find("div", class_="authors").text.replace("Authors:", "").strip()
    abstract = soup.find("blockquote", class_="abstract").text.replace("Abstract:", "").strip()
    dateline = soup.find("div", class_="dateline").text.strip()

    # Format date
    import re
    from datetime import datetime
    date_match = re.search(r"(\d{1,2} \w+ \d{4})", dateline)
    if not date_match:
        raise Exception("Could not parse date.")
    date_obj = datetime.strptime(date_match.group(1), "%d %b %Y")
    date_formatted = date_obj.strftime("%Y-%m-%d")
    weight = date_obj.strftime("%Y%m%d")

    # Single or multiple authors?
    author_field = f'author = "{authors}"' if ',' not in authors else f'author = "{authors}"'

    # Create TOML frontmatter
    result = f'''+++
title = "{title}"
date = "{date_formatted}"
weight = {weight}

template="resources/paper.html"

[extra]
web = "{url}"

{author_field}

abstract = "{abstract}"
+++
'''
    return title, result

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <arxiv_url>")
        sys.exit(1)

    url = sys.argv[1]
    try:
        title, output_text = fetch_arxiv_metadata(url)
        print(output_text)

        # Save to file
        output_dir = sys.argv[2] if len(sys.argv) > 2 else "../content/resources/papers/"
       
        safe_title = title.lower().replace(" ", "_").replace("/", "_")
        output_path = os.path.join(output_dir, f"{safe_title}.md")
        
        with open(output_path, "w") as f:
            f.write(output_text)
        print(f"\nSaved to: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()