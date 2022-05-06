## About
Useful template scripts for web scraping projects that use Selenium.

## High-level view
For a project using [Selenium](https://selenium-python.readthedocs.io/index.html), the typical components are:
```
Python Script -> Selenium Module for Python -> Chrome WebDriver -> Chrome Web Broswer
```

## Scripts in this repository
#### DownloadChromeDriver.py
This script will detect the version of the Chrome web browser on your Windows PC and will then download the correct version of the Chrome WebDriver.
#### StartSelenium.py
This script will do an automated Google search for news and pick a news article to navigate to.

## Installation
* Install the Chrome web browser
* Install [Python](https://www.python.org/downloads/)
* Run the following commands at a command prompt to install Selenium (and another useful module):
```bash
pip install beautifulsoup4
pip install selenium
```
* Run the following command to download (or update to) the newest version of the Chrome WebDriver. The python script must be in the current directory.
```bash
python .\DownloadChromeDriver.py
```

## Running
* Run this command at a command prompt to start running Selenium. The python script must be in the current directory.
```bash
python .\StartSelenium.py
```
