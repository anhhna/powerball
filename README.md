# Powerball Data Scraper and Analysis

## Overview
This project is a Python-based tool for scraping Powerball draw results from the official Powerball website and analyzing the data. It uses Selenium for web scraping and Jupyter Notebook for data visualization and analysis.

## Features
- **Web Scraping**: Automates the collection of Powerball draw results, including draw dates, winning numbers, jackpot amounts, and winner locations.
- **Data Storage**: Saves the scraped data into a CSV file (`powerball.csv`) for further analysis.
- **Data Analysis**: Provides insights into Powerball draw results, such as:
  - Frequency of winning numbers.
  - Distribution of jackpot amounts by location.
  - Visualization of Powerball winners and prize amounts.

## Technologies Used
- **Python**: Core programming language.
- **Selenium**: For web scraping.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib & Seaborn**: For data visualization.
- **Jupyter Notebook**: For interactive data analysis.

## Project Structure
```
.
├── crawl.py          # Initial version of the scraper
├── crawl_v2.py       # Enhanced version of the scraper
├── powerball.csv     # CSV file containing scraped Powerball data
├── powerball.ipynb   # Jupyter Notebook for data analysis and visualization
└── README.md         # Project documentation
```

## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- Microsoft Edge browser
- Edge WebDriver
- Required Python packages:
  - `selenium`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `jupyter`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/romanghosn/powerball-scraper.git
   cd powerball-scraper
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure Edge WebDriver is installed and added to your system PATH.

## Usage

### Running the Scraper
1. Run the enhanced scraper (`crawl_v2.py`) to collect Powerball data:
   ```bash
   python crawl_v2.py
   ```
2. The scraped data will be saved in `powerball.csv`.

### Analyzing the Data
1. Open the Jupyter Notebook:
   ```bash
   jupyter notebook powerball.ipynb
   ```
2. Follow the cells in the notebook to analyze and visualize the data.

## Notes
- The scraper is configured to run in headless mode for efficiency.
- Ensure the Powerball website's structure has not changed, as it may affect the scraper's functionality.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Disclaimer
This project is for educational purposes only. Use responsibly and ensure compliance with the website's terms of service.