# Supply Chain Analytics & Machine Learning

## Project Overview

This project analyzes supply-chain data to identify delivery delays, evaluate supplier performance, monitor inventory, and build a machine-learning model for delivery-delay prediction.

The project combines:

- Python for data generation, preprocessing, analysis, and machine learning
- SQL for database storage and analytical queries
- Power BI for KPI cards and interactive dashboards
- Excel for dataset handling and supporting analysis

## Dataset

The project uses a realistic supply-chain dataset containing 2,000 records and 25 columns.

Key information includes:

- Order and supplier details
- Product and category information
- Warehouse information
- Order, shipping, expected delivery, and actual delivery dates
- Quantity and cost information
- Lead time and delivery delay
- Delivery status
- Inventory and reorder levels
- Supplier performance

## Project Structure

```text
Supply-Chain-Analytics/
│
├── data/          # Dataset files
├── ml/            # Machine-learning files and model outputs
├── python/        # Python scripts
├── sql/           # SQL database and analysis queries
├── powerbi/       # Power BI dashboard/data/DAX files
├── dashboard/     # Dashboard-related files
├── excel/         # Excel analysis files
│
├── README.md
└── requirements.txt
```

## Key KPIs

The Power BI dashboard focuses on supply-chain performance indicators such as:

- Total Orders
- Delayed Orders
- On-Time Orders
- Delay Rate
- Total Order Value
- Transportation Cost
- Average Lead Time
- Average Delay Days
- Supplier Performance
- Inventory Status

## Machine Learning

The machine-learning component uses historical supply-chain information to predict whether an order is likely to be delayed.

The workflow includes:

1. Dataset preparation
2. Data preprocessing
3. Feature selection
4. Model training
5. Model evaluation
6. Delay prediction

## Power BI Dashboard

The Power BI component provides interactive visualization of supply-chain performance, including delivery status, supplier performance, inventory status, order value, and delay trends.

## SQL Analysis

SQL is used to store and analyze the supply-chain dataset and perform queries for operational and KPI analysis.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- SQL / MySQL
- Microsoft Power BI
- Microsoft Excel
- Git & GitHub

## How to Run the Python Project

1. Clone this repository.
2. Open the project folder in a terminal.
3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

4. Run the required Python scripts from the `python/` or `ml/` folders.

## Power BI

Open the Power BI file inside the `powerbi/` folder using Power BI Desktop.

If a `.pbix` file is not included, import the Power BI-ready CSV/data file and create the provided DAX measures.

## Project Goal

The goal of this project is to demonstrate how data analytics, SQL, machine learning, and business intelligence can be combined to improve supply-chain visibility and identify potential delivery risks.

## Author

Supply Chain Analytics & Machine Learning Project
