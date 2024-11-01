

# ScrapVid

**ScrapVid** is a Python-based tool designed to extract and download all `.mp4` video files from a specified webpage. Created with a simple console interface, it allows users to input the target URL and download location, making it easy to retrieve video content quickly and efficiently.

## 🛠 Features
- **Automated MP4 Discovery**: Scrapes the provided URL for any accessible `.mp4` links.
- **Flexible Download Location**: Allows users to specify a custom folder for saving downloaded videos.
- **Interactive Console**: Includes prompts for easy setup and usage.

## 🚀 Installation

### Prerequisites
- **Python 3.x**: Ensure you have Python installed on your system. [Download Python](https://www.python.org/downloads/)
- **Required Libraries**: Install the necessary libraries via `pip`.

### Installation Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Chanuka-KL/ScrapVid.git
   cd ScrapVid
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🏃 Usage

Run `ScrapVid.py` directly from the terminal:

```bash
python ScrapVid.py
```

When prompted:
- **Enter the target website URL**: This is the webpage from which MP4 files will be scraped.
- **Specify the download folder**: Name the folder where all downloaded files should be saved. (If the folder doesn’t exist, it will be created automatically.)

## Example Workflow
After launching the script:
1. Input your target URL, e.g., `https://example.com/videos`.
2. Specify a folder name, such as `videos`, where the downloads should be saved.

### Sample Output

```
[+] Enter the website URL: https://example.com/videos
[+] Enter the download folder name (e.g., videos): my_videos
[*] Fetching the webpage...
[*] Looking for MP4 links...
[+] Downloading my_videos/video1.mp4...
[✔] Downloaded my_videos/video1.mp4
[!] No more MP4 files found.
```

## 💡 How It Works

1. **Webpage Fetching**: The script uses the `requests` library to load the target webpage.
2. **HTML Parsing**: `BeautifulSoup` parses the HTML to find links ending in `.mp4`.
3. **Video Download**: All identified `.mp4` files are downloaded to the specified folder.

## 🐛 Troubleshooting

- **Error 404**: If the URL is incorrect or inaccessible, make sure it’s valid and public.
- **Download Issues**: Check internet connectivity and available disk space.

## 📋 Requirements

- **requests** - Handles web requests.
- **beautifulsoup4** - Parses the HTML content to identify video links.

Install these libraries using:
```bash
pip install requests beautifulsoup4
```

## 🧑‍💻 Contributing

Feel free to fork this project, submit issues, or make pull requests to enhance **ScrapVid**. Contributions are always welcome!

---

**Author**: Chanuka-KL (GitHub: [Chanuka-KL](https://github.com/Chanuka-KL))  

