# Sudhakar Manufacturing Analytics & Intelligence Dashboard

## Project Overview

This project is a manufacturing analytics and business intelligence portfolio project designed around a manufacturing environment similar to the operations of Sudhakar Industries.

The project uses a synthetic manufacturing dataset to analyze production performance, product rejection rates, machine downtime, inventory status, and sales performance.

The analysis was performed using Python and Tableau, with Tableau used to create an interactive manufacturing intelligence dashboard.

> **Note:** This project uses synthetic data created exclusively for portfolio demonstration. It does not contain or represent confidential operational data from Sudhakar Industries.

---

## Project Objectives

The main objectives of this project are to:

- Monitor production performance against targets
- Analyze production achievement
- Track product rejection rates
- Examine machine downtime
- Compare performance across manufacturing plants
- Analyze inventory and reorder conditions
- Explore product and regional sales performance
- Present operational KPIs through an interactive dashboard

---

## Technologies Used

- **Python** — Data analysis and exploratory analysis
- **Pandas** — Data manipulation and aggregation
- **Matplotlib** — Data visualization
- **Excel** — Dataset storage and analysis output
- **Tableau Public** — Interactive business intelligence dashboard
- **GitHub** — Project documentation and version control

---

## Dataset

The project uses a synthetic manufacturing dataset covering six months:

**January 2026 – June 2026**

The dataset contains four main areas:

### Production

Includes:

- Date
- Plant
- Product
- Machine
- Shift
- Target Units
- Produced Units
- Rejected Units
- Accepted Units
- Downtime Minutes
- Achievement Percentage
- Rejection Rate Percentage

### Inventory

Includes:

- Opening Stock
- Production Received
- Dispatch Units
- Closing Stock
- Reorder Level
- Stock Status

### Sales

Includes:

- Region
- Product
- Channel
- Units Sold
- Revenue

### Machines

Includes:

- Machine ID
- Primary Plant
- Process Type
- Installation Year
- Operating Hours

---

## Key Project Metrics

Based on the synthetic dataset:

| Metric | Value |
|---|---:|
| Total Production | 4,456,436 units |
| Total Target | 4,665,818 units |
| Production Achievement | 95.51% |
| Total Rejected | 100,584 units |
| Overall Rejection Rate | 2.26% |
| Total Downtime | 3,093.78 hours |
| Synthetic Sales Revenue | ₹2,001,981,461.85 |

These figures are derived from the synthetic dataset and should not be interpreted as actual Sudhakar Industries operational metrics.

---

## Python Analysis

Python was used to perform the underlying data analysis.

The analysis includes:

- Production KPI calculation
- Production achievement analysis
- Product rejection analysis
- Machine downtime analysis
- Plant-level performance analysis
- Shift-level analysis
- Monthly production analysis
- Inventory reorder analysis
- Sales analysis
- Basic anomaly screening

The Python analysis script is available in:

`python/analysis.py`

Generated analytical outputs and charts are available in:

`analysis_outputs/`

---

## Tableau Dashboard

The Tableau dashboard provides an interactive view of the manufacturing KPIs.

### Dashboard includes

- Total Production
- Production Achievement
- Rejection Rate
- Downtime Hours
- Target vs Actual Production
- Product Rejection Rate
- Machine Downtime
- Plant-level filtering

### Dashboard Preview

![Sudhakar Manufacturing Intelligence Dashboard](tableau/sudhakar-manufacturing-dashboard.png)

### Live Tableau Dashboard

[View the interactive dashboard on Tableau Public](https://public.tableau.com/app/profile/pola.tharun/viz/sudhakar_17904127424650/SudhakarManufacturingIntelligenceDashboard)

---

## Project Structure

```text
sudhakar-manufacturing-analytics/
│
├── analysis_outputs/
│   ├── 01_machine_downtime.png
│   ├── 02_target_vs_actual.png
│   ├── 03_monthly_production.png
│   ├── 04_product_rejection.png
│   ├── 05_plant_performance.png
│   ├── 06_inventory_reorder.png
│   ├── 07_sales_by_product.png
│   ├── 08_sales_by_region.png
│   └── manufacturing_analysis_results.xlsx
│
├── data/
│   └── manufacturing_analytics_dataset.xlsx
│
├── python/
│   └── analysis.py
│
├── tableau/
│   └── sudhakar-manufacturing-dashboard.png
│
└── README.md
