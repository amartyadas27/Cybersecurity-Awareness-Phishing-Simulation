# Phishing Link checker


# A simple web application built with Python and Flask the Checks if a given URL is Potentially a site using basic heuristic methods.


# Features

Submit a website URL to check
Basic phishing detection using Keyword rules
URL reachability status(HTTP status Codes)
Simple and Clean HTML/CSS interface
Modular and easy to extend

### Project Structure

phishing checker/
|
|---app.py # Main Flask aplication
|---requirements.txt # Python dependencies
|---templates/
  |----index.html # HTML UI
|---Static/
  |----style.css #Styling
|---utils/
  |----Checker.py # Phishing checking logic
|---README.md

## Setup Instructions

### BASH
git clone https://github.com/amartyadas27/Cybersecurity-Awareness-Phishing-Simulation.git

cd Cybersecurity-Awareness-Phishing-Simulation

## Create a virtual Enviroment 
python -m venv venv
Source venv/bin/activate # ON WINDOWS USE: venv\Scripts\activate
## Install Dependencies

pip install -r requirements.txt

## Run the Flask APP

python app.py


#### Then Open your browser and go to:
https://127.0.0.1:5000

## How It Works
The user inputs a URL.
The bacKend checks for suspicious Keywords in the URL.
It attempts to access the URL and envluates its HTTP status code.
A result is shown indicating whether it's likely safe or suspicious.





