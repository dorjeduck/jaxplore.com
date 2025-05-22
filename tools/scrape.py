import sys
import os
import requests
import xml.etree.ElementTree as ET
from datetime import datetime
from urllib.parse import urlparse, parse_qs

def get_url_type(url):
    parsed = urlparse(url)
    if parsed.netloc in ["www.youtube.com", "youtube.com", "youtu.be"]:
        if "playlist" in parsed.path or "list" in parse_qs(parsed.query):
            return "youtube_playlist"
        return "youtube_video"
    elif parsed.netloc == "arxiv.org":
        return "arxiv"
    elif parsed.netloc == "github.com":
        return "github"
    else:
        raise ValueError("Unsupported URL type.")

# YouTube Functions
def get_youtube_id(url):
    parsed = urlparse(url)
    if "playlist" in parsed.path:
        query_params = parse_qs(parsed.query)
        return query_params.get("list", [None])[0], "playlist"
    if parsed.netloc == "youtu.be":
        return parsed.path.strip("/"), "video"
    query_params = parse_qs(parsed.query)
    return query_params.get("v", [None])[0], "video"

def fetch_youtube_metadata(identifier, id_type):
    if id_type == "playlist":
        api_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/playlist?list={identifier}&format=json"
    else:
        api_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={identifier}&format=json"

    response = requests.get(api_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch metadata from YouTube API: {response.status_code}")

    data = response.json()
    title = data["title"]
    channel_url = data["author_url"]
    channel = channel_url.split("/")[-1]
    date_formatted = datetime.now().strftime("%Y-%m-%d")

    if id_type == "playlist":
        content = (
            f"""+++
title = "{title}"
date = "{date_formatted}"
template = "resources/youtube_video.html"

[extra]
playlist = "{identifier}"
channel = "{channel}"
+++
"""
        )
    else:
        content = (
            f"""+++
title = "{title}"
date = "{date_formatted}"
template = "resources/youtube_video.html"

[extra]
video = "{identifier}"
channel = "{channel}"
+++
"""
        )

    return title, content

# GitHub Functions
def get_github_repo_info(url):
    parsed = urlparse(url)
    path_parts = parsed.path.strip("/").split("/")
    if len(path_parts) < 2:
        raise ValueError("Invalid GitHub URL. Could not extract repository information.")

    owner, repo = path_parts[:2]
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(api_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch repository metadata from GitHub API: {response.status_code}")

    data = response.json()
    title = data["name"]
    description = data.get("description", "No description provided.")
    github_repo = f"{owner}/{repo}"

    content = (
        f"""+++
title = "{title}"
description = "{description}"
template = "resources/github_repo.html"

[extra]
github_repo = "{github_repo}"
+++
"""
    )
    return title, content

# arXiv Functions
def get_arxiv_id_from_url(url):
    parsed = urlparse(url)
    return parsed.path.strip("/").split("/")[-1]

def fetch_arxiv_metadata(arxiv_id):
    api_url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    response = requests.get(api_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch metadata from arXiv API: {response.status_code}")

    root = ET.fromstring(response.content)
    entry = root.find("{http://www.w3.org/2005/Atom}entry")
    if entry is None:
        raise Exception("No entry found for the given arXiv ID.")

    title = entry.find("{http://www.w3.org/2005/Atom}title").text.strip().replace("\n", " ")
    summary = entry.find("{http://www.w3.org/2005/Atom}summary").text.strip().replace("\n", " ")
    published = entry.find("{http://www.w3.org/2005/Atom}published").text
    date_obj = datetime.strptime(published, "%Y-%m-%dT%H:%M:%SZ")
    date_formatted = date_obj.strftime("%Y-%m-%d")
    weight = date_obj.strftime("%Y%m%d")

    authors = entry.findall("{http://www.w3.org/2005/Atom}author")
    author_names = ", ".join([a.find("{http://www.w3.org/2005/Atom}name").text for a in authors])
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
        print("Usage: python scrape.py <url>")
        sys.exit(1)

    try:
        url = sys.argv[1]
        url_type = get_url_type(url)

        if url_type == "youtube_video" or url_type == "youtube_playlist":
            identifier, id_type = get_youtube_id(url)
            title, metadata = fetch_youtube_metadata(identifier, id_type)
            folder = "youtube"
        elif url_type == "github":
            title, metadata = get_github_repo_info(url)
            folder = "github"
        elif url_type == "arxiv":
            arxiv_id = get_arxiv_id_from_url(url)
            title, metadata = fetch_arxiv_metadata(arxiv_id)
            folder = "papers"
        else:
            raise ValueError("Unsupported URL type.")

        filename = title.lower().replace(" ", "_").replace("/", "_").replace(":", "")
        filepath = os.path.join(f"../content/resources/{folder}/", f"{filename}.md")
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as f:
            f.write(metadata)
        print(f"\nSaved to: {filepath}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
