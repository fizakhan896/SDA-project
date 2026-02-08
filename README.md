GDP Analysis Project
Project Overview:
The GDP Analysis Project is a Python-based data analysis application that processes GDP data of countries and produces meaningful results based on user-defined configuration settings.
The project follows a modular architecture, separating data loading, processing, and presentation into different Python modules.

The goal of the project is to:
Clean and organize GDP data
Filter data by region and year
Perform GDP calculations (sum or average)
Save results in a JSON file
Display results through a simple dashboard
All user choices are controlled via a config.json file, ensuring no hardcoded values.

Problem Statement:
Raw GDP data is large, unstructured, and difficult to analyze directly.
This project solves the problem by:
Cleaning and reshaping GDP data
Making analysis configurable
Automating GDP calculations
Producing clean and reusable outputs

Key Features:
Config-driven logic (no hardcoding)
Modular design (Single Responsibility Principle)
Error handling for invalid inputs
Clean data preprocessing
Output saved to JSON

Dashboard / presentation layer:
Ready for future visualization extensions
Project Structure
project/
│
├── data/
│   ├── gdp_with_continent_filled.csv
│   ├── gdp_data_clean.csv
│   └── output_result.json
│
├── data_loader.py
├── data_processor.py
├── dashboard.py
├── main.py
├── config.json
└── README.md

File Responsibilities:
data_loader.py:
Handles only data loading tasks:
Loads CSV data using pandas
Loads configuration from config.json
Returns cleaned data to the controller
No filtering or calculations

data_processor.py:
Handles only data processing logic:
Validates input data and configuration
Filters data by region and year
Calculates GDP (sum or average)
Saves results to output_result.json
No file loading or dashboard printing

dashboard.py:
Acts as the presentation layer:
Reads results from output_result.json
Displays formatted GDP analysis results

main.py:
The controller of the application:
Calls the data loader
Calls the data processor
Calls the dashboard
Manages the overall program flow

config.json:
Defines user choices:
{
  "region": "Asia",
  "year": 2020,
  "operation": "average"
}

Changing this file changes the program output without modifying code

How to Run the Project:
Run inside Jupyter (NO terminal)
In Jupyter, in cell run this
!python main.py
Press Shift + Enter

This tells Jupyter:
“Run this as a system command, not Python code”

Testing
You can test different scenarios by modifying config.json:
Change region (e.g., Asia, Europe)
Change year (e.g., 2018, 2019, 2020)
Change operation (sum or average)

Each change will produce different results, demonstrating correct config-driven behavior.

Technologies Used:
Python
Pandas
JSON
Command Line Interface (CLI)

Design Principles Used:
Modular Architecture
Separation of Concerns
Functional Programming (map, filter, lambda)
Error Handling
Config-Driven Design

Conclusion:
This project demonstrates a clean, professional approach to data analysis using Python.
By separating logic into modules and avoiding hardcoding, the project is scalable, maintainable, and easy to understand.