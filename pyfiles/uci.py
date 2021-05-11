import pandas as pd

url="https://archive.ics.uci.edu/ml/datasets.html"

def download_dataset_url(url, directory, msg_flag=False, download_flag=True):
    """
    Download all the files from the links in the given url.
    msg_flag: Controls verbosity.
    download_flag: Default is True. If set to False, only creates the directories but does not initiate download (for testing purpose).
    """

    import urllib.request, urllib.parse, urllib.error
    from bs4 import BeautifulSoup
    import ssl
    import os

    if url == "URL not available":
        return None

    cwd = os.getcwd()
    directory = directory.replace(":", "-")
    local_directory = cwd + "\\" + str(directory)
    if not os.path.exists(local_directory):
        try:
            os.makedirs(local_directory)
        except:
            print(f"Cannot create directory: {directory}")

    if download_flag:
        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        uh = urllib.request.urlopen(url, context=ctx)
        html = uh.read().decode()
        soup = BeautifulSoup(html, "html5lib")

        links = []
        for link in soup.find_all("a"):
            links.append(link.attrs["href"])

        links_to_download = []

        if "Index" in links:
            idx = links.index("Index")
        else:
            idx = len(links) - 2
        for i in range(idx + 1, len(links)):
            links_to_download.append(url + str(links[i]))

        for file_url in links_to_download:
            download_file(file_url, local_directory)

        if msg_flag:
            print(f"Downloaded dataset from {url}")

def download_file(url, directory):
    """
    Downloads a file from a given url into the given directory.
    """
    import requests
    import os

    local_filename = directory + "/" + url.split("/")[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    try:
        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
    except:
        print("Sorry could not write this particular file!")
        # f.flush()