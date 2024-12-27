# Spotify Charts Scraper

This project is a reusable Python script designed to scrape data from Spotify Charts. The script fetches detailed information about the top albums, artists, and songs, along with highlights for each category. The script is dynamic and can be run weekly (or whenever the charts refresh) to fetch the latest data.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Scraped Data](#scraped-data)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Contact](#contact)

---

## Overview

This project uses python to provide the latest data on Spotify's top charts. It is particularly useful for tracking trends, analyzing rankings, and gathering insights into Spotify's top-performing songs, albums, and artists over time.

---

## Features

- **Reusable**: Run the script weekly or whenever Spotify Charts refresh to get updated data.
- **Comprehensive Data**: Fetches information on top songs, albums, and artists.
- **Highlights**: Provides highlight data such as streaks and notable achievements for songs, albums, and artists.
- **Export**: Outputs the scraped data in both CSV and Excel formats.

---

## Scraped Data

The script gathers the following details:

### Songs Data
- Name
- Rank
- Previous Rank
- Image URL
- Song URL
- Artist/s Name
- Artist Spotify

### Albums Data
- Name
- Rank
- Previous Rank
- Image URL
- Song URL
- Artist/s Name
- Artist Spotify

### Artists Data
- Name
- Rank
- Previous Rank
- Artist URL
- Photo URL

### Highlights Data
For songs, albums, and artists:
- Streak
- Details
- Image URL

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/spotify-charts-scraper.git
   cd spotify-charts-scraper
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
---

## Usage

1. Run the script to fetch the latest Spotify Charts data:
   ```bash
   python scrape_spotify_charts.py
   ```

2. The script will automatically update the data and save it in the specified output formats.

---

## Output

The script generates the following files:
- **CSV File**: Contains all scraped data for songs, albums, and artists.
- **Excel File**: Provides the same data in an Excel-friendly format for further analysis.

---

## Contact

For questions or support, feel free to reach out:
- **GitHub**: [Abdullah-Shaheer](https://github.com/Abdullah-Shaheer)
- **Email**: abdullahshaheer17398@gmail.com

---

Happy scraping! 🎵
