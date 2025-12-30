## 🐍 Python Scripting Practice

A collection of beginner-friendly Python scripts that helped me learn file I/O, text processing, API usage, and basic automation.
Each script focuses on one skill and does one useful thing.

--------------------------------

Project Structure

python-scripting-practice/
  Text_processing/
    keyword_counter/
    log_error_finder/
    word_frequency/
    login_attempt_analyzer/

  api_scripting/
    weather_fetcher/
    stock_price_fetcher/

--------------------------------

Text Processing Scripts

keyword_counter
Scans a text file for a keyword the user enters and reports how many times it appears.

log_error_finder
Reads a .log file and counts how many lines include "ERROR".

word_frequency
Counts how often each word appears, sorts them, and shows the most common ones.

login_attempt_analyzer
Parses a login log file and summarizes successful and failed login attempts.

Concepts Practiced
- Reading and writing files
- Dictionaries for counting
- Sorting data
- User input handling
- Simple automation

--------------------------------

Weather Fetcher
Uses the Open-Meteo API to:
- ask for a city
- convert city → latitude and longitude
- fetch current weather and multi-day forecast
- save a weather_report.txt

Concepts Practiced
- APIs and JSON
- requests library
- error handling
- formatting reports

--------------------------------

Stock Price Fetcher
Uses the Alpha Vantage API to:
- ask for a stock ticker (AAPL, MSFT, TSLA, etc.)
- fetch live stock price
- handle invalid symbols and rate limits

Concepts Practiced
- API keys
- parsing structured JSON
- defensive coding

--------------------------------

Goal
This repo is for learning scripting, practicing real-world problem solving, and building useful small tools.
