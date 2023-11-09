# BTS Form 41 Traffic Data Post-Processor

This repository contains a Python script designed for post-processing and visualizing BTS (Bureau of Transportation Statistics) Form 41 Traffic data. The main purpose of this script is to evaluate and visualize Available Seat Miles (ASM) and Revenue Seat Miles (RSM) for Full Service Carriers (FSC) over a range of years.

## Features

- Importing BTS Form 41 traffic data.
- Filtering data based on specific airline codes.
- Calculating ASM and RPM metrics for specified airlines.
- Visualizing ASM and RSM as bar graphs for American Airlines, United Airlines, and Delta Airlines.

## Requirements

- Python 3.x
- Pandas: `pip install pandas`
- NumPy: `pip install numpy`
- Matplotlib: `pip install matplotlib`

## Data

The dataset used is the T-100 Domestic Market (All Carriers) from the BTS, which contains segment data for various airlines over the years. The data should be organized in CSV files within folders named by year (e.g., `2015/`, `2016/`, etc.).

## Usage

1. Ensure you have the required CSV data files within the respective year folders.
2. Run the script using Python.
   
   ```bash
   python3 operations.py
