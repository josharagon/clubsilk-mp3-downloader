# Club Silk Records MP3 Downloader

A Python script to automatically download purchased MP3s from Club Silk Records.

## Prerequisites

- Python 3.7 or higher
- Chrome browser
- ChromeDriver matching your Chrome version

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/club-silk-downloader.git
   cd club-silk-downloader
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Update the following variables in `download_clubsilkmp3s.py`:
   ```python
   username = "your_email@example.com"  # Your Club Silk Records email
   password = "your_password"           # Your Club Silk Records password
   chrome_driver_path = "path/to/chromedriver"  # Path to ChromeDriver
   download_folder = "downloads"        # Folder where MP3s will be saved
   ```

## Usage

Simply run the script:
```bash
python download_clubsilkmp3s.py
```

The script will:
1. Log in to your Club Silk Records account
2. Navigate to your MP3 library
3. Download all available MP3 files to the specified folder

## Features

- Automated login and navigation
- Batch download of all purchased MP3s
- Automatic retry on failed downloads
- Progress tracking and status messages

## Requirements

- selenium
- requests
- Chrome WebDriver

## License

MIT License - See LICENSE file for details