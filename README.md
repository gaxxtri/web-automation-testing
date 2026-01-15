Subject: README – UI Automation Project

# Automated UI Testing of Public Websites (Selenium)

## Overview

This project demonstrates Software Quality Engineering skills using Selenium WebDriver to automate core user flows across multiple real-world websites.

Four live sites were tested with no login required:

* 🧠 Wikipedia — Knowledge base search
* 🛒 Amazon India — Product catalog search
* 🍕 Zomato — Food search (city-specific)
* 🌦️ OpenWeatherMap — Weather lookup

## Features Tested

✔ Homepage load
✔ Title validation
✔ Search functionality
✔ Results detection
✔ Negative blank input tests
✔ Error handling + logging

## Failing Observations

🚩 Zomato intermittently blocks automated access
🚩 OpenWeather temperature widget loads inconsistently
📝 Both documented in bug_report.md

## Tech Stack

* Python 3.x
* Selenium WebDriver
* WebDriver Manager
* Chrome Browser
* Git & GitHub

## Project Structure

```
amazon_test.py
zomato_test.py
openweather_test.py
wikipedia_test.py
screenshots/
bug_report.md
test_plan.md
README.md


## How to Run

python wikipedia_test.py
python amazon_test.py
python zomato_test.py
python openweather_test.py

## Next Improvements
* Page Object Model structure
* Run tests on GitHub Actions CI

## Run in terminal
pytest tests/ --html=report.html --self-contained-html
start report.html

## Author

**Gayatri Kanagaraj**
Data Science Student & Quality Engineering Contributor
