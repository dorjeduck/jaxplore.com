import sys
import os
import requests
import xml.etree.ElementTree as ET
from datetime import datetime
from urllib.parse import urlparse


def get_arxiv_id_from_url(url):
    parsed = urlparse(url)
    if parsed.netloc != "arxiv.org":
        raise ValueError("Only arxiv.org URLs are supported.")
    return parsed.path.strip("/").split("/")[-1]


def fetch_arxiv_metadata(arxiv_id):
    api_url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    response = requests.get(api_url)
    if response.status_code != 200:
        raise Exception(
            f"Failed to fetch metadata from arXiv API: {response.status_code}"
        )

    root = ET.fromstring(response.content)
    entry = root.find("{http://www.w3.org/2005/Atom}entry")
    if entry is None:
        raise Exception("No entry found for the given arXiv ID.")

    title = (
        entry.find("{http://www.w3.org/2005/Atom}title").text.strip().replace("\n", " ")
    )
    summary = (
        entry.find("{http://www.w3.org/2005/Atom}summary")
        .text.strip()
        .replace("\n", " ")
    )
    published = entry.find("{http://www.w3.org/2005/Atom}published").text
    date_obj = datetime.strptime(published, "%Y-%m-%dT%H:%M:%SZ")
    date_formatted = date_obj.strftime("%Y-%m-%d")
    weight = date_obj.strftime("%Y%m%d")

    authors = entry.findall("{http://www.w3.org/2005/Atom}author")
    author_names = ", ".join(
        [a.find("{http://www.w3.org/2005/Atom}name").text for a in authors]
    )
    author_line = f'author = "{author_names}"'

    web = f"https://arxiv.org/abs/{arxiv_id}"

    content = (
        f"""+++
title = "{title}"
date = "{date_formatted}"
weight = {weight}

template="resources/paper.html"

[extra]
web = "{web}"

{author_line}

abstract = """
        + '"""'
        + f"{summary}"
        + '"""'
        + """
+++
"""
    )
    return title, content


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <arxiv_url>")
        sys.exit(1)

    try:
        arxiv_id = get_arxiv_id_from_url(sys.argv[1])
        title, metadata = fetch_arxiv_metadata(arxiv_id)
        print(metadata)

        filename = title.lower().replace(" ", "_").replace("/", "_").replace(":", "")
        filepath = os.path.join("../content/resources/papers/", f"{filename}.md")
        with open(filepath, "w") as f:
            f.write(metadata)
        print(f"\nSaved to: {filepath}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
