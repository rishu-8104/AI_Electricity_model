# Electricity Data Fetching and Processing

This project fetches electricity price data from the "electricity-price.p.rapidapi.com" API for each day of the year, from January 1st to December 31st, and saves it to a file. The project includes scripts for fetching electricity data and provides various Excel files with weather and energy generation data.

## Introduction

This repository contains Python scripts for retrieving electricity price data for Finland (EUR currency) over the course of an entire year. The data is fetched from the API, formatted, and saved to an output file. Additionally, various datasets for weather (temperature, wind speed, etc.) and electricity generation are provided.

### Key Features:
- **Data Fetching**: Fetch electricity price data for each day of the year.
- **API Integration**: Uses the "electricity-price.p.rapidapi.com" API to gather electricity price data.
- **Data Storage**: Saves the fetched data into a text file.
- **File Organization**: Includes multiple datasets like air temperature, global radiation, precipitation, and electricity generation data in Excel format.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Project Structure](#project-structure)
4. [Features](#features)
5. [License](#license)
6. [Contact Information](#contact-information)
7. [Acknowledgements](#acknowledgements)

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/rishu-8104/AI_Electricity_model.git
    cd electricity-data-fetching
    ```

2. Install dependencies:
    This project requires `requests` and `openpyxl` for interacting with APIs and handling Excel files.

    To install the required libraries, use:
    ```bash
    pip install -r requirements.txt
    ```

    Alternatively, you can manually install:
    ```bash
    pip install requests openpyxl
    ```

3. Ensure you have an API key for RapidAPI (you can get it from the [RapidAPI website](https://rapidapi.com/)) and replace it in the code.

## Usage

1. **Fetching Electricity Data**:
   - Navigate to the `code` directory where the `fetch_electric_data.py` script is located.
   - Run the script to fetch electricity price data for the specified date range and save it to a text file.

    ```bash
    python fetch_electric_data.py
    ```

    The script will fetch data for every day in 2023 and save it in `electricity_data.txt` in the `Data` folder.

2. **Viewing and Using Excel Files**:
   - The data can be viewed or analyzed using Excel or any data processing tool that supports `.xlsx` files.
   - The `electricity_data.xlsx` and `electricity_generation_data_2023_formatted.xlsx` files are included, providing relevant data for analysis.

## Project Structure

```
.
├── Data
│   ├── AirTemp.xlsx                  # Air temperature data
│   ├── GlobalRadiation.xlsx          # Global radiation data
│   ├── Merged_data.xlsx              # Merged data from various sources
│   ├── electricity_data.xlsx         # Electricity price data for the year
│   ├── electricity_generation_data_2023_formatted.xlsx # Electricity generation data for 2023
│   ├── precepetation.xlsx            # Precipitation data
│   ├── windspeed.xlsx                # Wind speed data
│   ├── ~$Merged_data.xlsx            # Temporary file for merged data
│   ├── ~$electricity_data.xlsx       # Temporary file for electricity data
│   └── ~$electricity_generation_data_2023_formatted.xlsx # Temporary file for electricity generation data
└── code
    └── fetch_electric_data.py        # Python script to fetch electricity price data
```

## Features

- **Data Fetching**: Fetches daily electricity price data for Finland for the year 2023.
- **Excel Files**: Includes various datasets like temperature, wind speed, radiation, and electricity generation.
- **Data Processing**: Prepares data in a format ready for further analysis.
- **API Integration**: Uses the RapidAPI service to fetch the data.


## Contact Information

For any questions or feedback, feel free to reach out:

- **Email**: rishugupta8104@gmail.com

## Acknowledgements

- **RapidAPI**: For providing the API to fetch electricity price data.
- **OpenPyXL**: For handling Excel files.
