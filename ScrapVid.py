import requests
from bs4 import BeautifulSoup
import os
import urllib.parse

def print_banner():
    print("\033[1;36m")
    banner = r"""
███████╗ ██████╗██████╗  █████╗ ██████╗ ██╗   ██╗██╗██████╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║   ██║██║██╔══██╗
███████╗██║     ██████╔╝███████║██████╔╝██║   ██║██║██║  ██║
╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ╚██╗ ██╔╝██║██║  ██║
███████║╚██████╗██║  ██║██║  ██║██║      ╚████╔╝ ██║██████╔╝
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝       ╚═══╝  ╚═╝╚═════╝


                ScrapVid Web Scraper
                Created by: Specter ch
"""
    print(banner + "\033[0m")

def get_user_input():
    url = input("\033[1;32m[+] Enter the website URL: \033[0m")
    folder = input("\033[1;32m[+] Enter the download folder name (e.g., videos): \033[0m")
    return url, folder

def scrape_mp4_files(url, download_folder):
    try:
        # Make a request to the website
        print("\033[1;34m[*] Fetching the webpage...\033[0m")
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all video links
        print("\033[1;34m[*] Looking for MP4 links...\033[0m")
        mp4_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith('.mp4')]

        # Ensure the download folder exists
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        # Download each MP4 file
        if mp4_links:
            for link in mp4_links:
                # Handle relative URLs
                file_url = urllib.parse.urljoin(url, link)
                file_name = os.path.join(download_folder, os.path.basename(link))

                print(f"\033[1;33m[+] Downloading {file_name}...\033[0m")
                with requests.get(file_url, stream=True) as video_response:
                    with open(file_name, 'wb') as file:
                        for chunk in video_response.iter_content(chunk_size=8192):
                            file.write(chunk)
                print(f"\033[1;32m[✔] Downloaded {file_name}\033[0m")
        else:
            print("\033[1;31m[!] No MP4 files found.\033[0m")
    except Exception as e:
        print(f"\033[1;31m[!] An error occurred: {e}\033[0m")

# Main Execution
print_banner()
url, download_folder = get_user_input()