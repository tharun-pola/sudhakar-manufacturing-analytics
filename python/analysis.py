import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# SETTINGS
# ============================================================

INPUT_FILE = "manufacturing_analytics_dataset.xlsx"

OUTPUT_DIR = Path("analysis_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

# ============================================================
# LOAD DATA
# ============================================================

print("=" * 60)
print("SUDHAKAR MANUFACTURING ANALYTICS PROJECT")
print("=" * 60)

print("\nLoading Excel data...")

production = pd.read_excel(INPUT_FILE, sheet_name="Production")
inventory = pd.read_excel(INPUT_FILE, sheet_name="Inventory")
sales = pd.read_excel(INPUT_FILE, sheet_name="Sales")
machines = pd.read_excel(INPUT_FILE, sheet_name="Machines")

# Make sure date is treated as a date
production["date"] = pd.to_datetime(production["date"])
inventory["date"] = pd.to_datetime(inventory["date"])
sales["date"] = pd.to_datetime(sales["date"])

print("Data loaded successfully.")


# ============================================================
# 1. EXECUTIVE KPIs
# ============================================================

total_target = production["target_units"].sum()
total_production = production["produced_units"].sum()
total_rejected = production["rejected_units"].sum()
total_accepted = production["accepted_units"].sum()

production_achievement = (
    total_production / total_target * 100
)

rejection_rate = (
    total_rejected / total_production * 100
)

total_downtime_hours = (
    production["downtime_minutes"].sum() / 60
)

total_revenue = sales["revenue"].sum()
total_units_sold = sales["units_sold"].sum()

reorder_records = (
    inventory["stock_status"] == "Reorder Required"
).sum()

reorder_percentage = (
    reorder_records / len(inventory) * 100
)

print("\n" + "=" * 60)
print("EXECUTIVE KPIs")
print("=" * 60)

print(f"Total Target:              {total_target:,.0f} units")
print(f"Total Production:          {total_production:,.0f} units")
print(f"Production Achievement:    {production_achievement:.2f}%")
print(f"Total Rejected:             {total_rejected:,.0f} units")
print(f"Overall Rejection Rate:    {rejection_rate:.2f}%")
print(f"Total Downtime:              {total_downtime_hours:,.2f} hours")
print(f"Total Revenue:              ₹{total_revenue:,.2f}")
print(f"Total Units Sold:            {total_units_sold:,.0f}")
print(f"Reorder Records:             {reorder_records:,}")
print(f"Inventory Reorder Rate:     {reorder_percentage:.2f}%")


# ============================================================
# 2. MACHINE ANALYSIS
# ============================================================

machine_analysis = (
    production
    .groupby("machine")
    .agg(
        produced_units=("produced_units", "sum"),
        rejected_units=("rejected_units", "sum"),
        downtime_minutes=("downtime_minutes", "sum")
    )
    .reset_index()
)

machine_analysis["downtime_hours"] = (
    machine_analysis["downtime_minutes"] / 60
)

machine_analysis["rejection_rate_pct"] = (
    machine_analysis["rejected_units"]
    / machine_analysis["produced_units"]
    * 100
)

machine_analysis = machine_analysis.sort_values(
    "downtime_hours",
    ascending=False
)

print("\n" + "=" * 60)
print("MACHINE DOWNTIME")
print("=" * 60)

print(
    machine_analysis[
        ["machine", "downtime_hours", "rejection_rate_pct"]
    ].round(2).to_string(index=False)
)


# ============================================================
# 3. PRODUCT / QUALITY ANALYSIS
# ============================================================

product_analysis = (
    production
    .groupby("product")
    .agg(
        target_units=("target_units", "sum"),
        produced_units=("produced_units", "sum"),
        rejected_units=("rejected_units", "sum"),
        downtime_minutes=("downtime_minutes", "sum")
    )
    .reset_index()
)

product_analysis["achievement_pct"] = (
    product_analysis["produced_units"]
    / product_analysis["target_units"]
    * 100
)

product_analysis["rejection_rate_pct"] = (
    product_analysis["rejected_units"]
    / product_analysis["produced_units"]
    * 100
)

product_analysis["downtime_hours"] = (
    product_analysis["downtime_minutes"] / 60
)

product_analysis = product_analysis.sort_values(
    "rejection_rate_pct",
    ascending=False
)

print("\n" + "=" * 60)
print("PRODUCT QUALITY")
print("=" * 60)

print(
    product_analysis[
        [
            "product",
            "achievement_pct",
            "rejection_rate_pct",
            "downtime_hours"
        ]
    ].round(2).to_string(index=False)
)


# ============================================================
# 4. PLANT ANALYSIS
# ============================================================

plant_analysis = (
    production
    .groupby("plant")
    .agg(
        target_units=("target_units", "sum"),
        produced_units=("produced_units", "sum"),
        rejected_units=("rejected_units", "sum"),
        downtime_minutes=("downtime_minutes", "sum")
    )
    .reset_index()
)

plant_analysis["achievement_pct"] = (
    plant_analysis["produced_units"]
    / plant_analysis["target_units"]
    * 100
)

plant_analysis["rejection_rate_pct"] = (
    plant_analysis["rejected_units"]
    / plant_analysis["produced_units"]
    * 100
)

plant_analysis["downtime_hours"] = (
    plant_analysis["downtime_minutes"] / 60
)

print("\n" + "=" * 60)
print("PLANT PERFORMANCE")
print("=" * 60)

print(
    plant_analysis[
        [
            "plant",
            "achievement_pct",
            "rejection_rate_pct",
            "downtime_hours"
        ]
    ].round(2).to_string(index=False)
)


# ============================================================
# 5. SHIFT ANALYSIS
# ============================================================

shift_analysis = (
    production
    .groupby("shift")
    .agg(
        target_units=("target_units", "sum"),
        produced_units=("produced_units", "sum"),
        rejected_units=("rejected_units", "sum"),
        downtime_minutes=("downtime_minutes", "sum")
    )
    .reset_index()
)

shift_analysis["achievement_pct"] = (
    shift_analysis["produced_units"]
    / shift_analysis["target_units"]
    * 100
)

shift_analysis["rejection_rate_pct"] = (
    shift_analysis["rejected_units"]
    / shift_analysis["produced_units"]
    * 100
)

shift_analysis["downtime_hours"] = (
    shift_analysis["downtime_minutes"] / 60
)

print("\n" + "=" * 60)
print("SHIFT PERFORMANCE")
print("=" * 60)

print(
    shift_analysis[
        [
            "shift",
            "achievement_pct",
            "rejection_rate_pct",
            "downtime_hours"
        ]
    ].round(2).to_string(index=False)
)


# ============================================================
# 6. MONTHLY PRODUCTION
# ============================================================

production["month"] = (
    production["date"]
    .dt.to_period("M")
    .astype(str)
)

monthly_production = (
    production
    .groupby("month")
    .agg(
        target_units=("target_units", "sum"),
        produced_units=("produced_units", "sum")
    )
    .reset_index()
)

monthly_production["achievement_pct"] = (
    monthly_production["produced_units"]
    / monthly_production["target_units"]
    * 100
)


# ============================================================
# 7. INVENTORY ANALYSIS
# ============================================================

inventory_product = (
    inventory
    .groupby("product")
    .agg(
        average_closing_stock=("closing_stock", "mean"),
        total_dispatch=("dispatch_units", "sum"),
        reorder_records=(
            "stock_status",
            lambda x: (x == "Reorder Required").sum()
        )
    )
    .reset_index()
)

inventory_product["reorder_rate_pct"] = (
    inventory_product["reorder_records"]
    / inventory.groupby("product").size().values
    * 100
)

print("\n" + "=" * 60)
print("INVENTORY ANALYSIS")
print("=" * 60)

print(
    inventory_product[
        [
            "product",
            "average_closing_stock",
            "reorder_records",
            "reorder_rate_pct"
        ]
    ].round(2).to_string(index=False)
)


# ============================================================
# 8. SALES ANALYSIS
# ============================================================

sales_product = (
    sales
    .groupby("product")
    .agg(
        units_sold=("units_sold", "sum"),
        revenue=("revenue", "sum")
    )
    .reset_index()
)

sales_product["revenue_share_pct"] = (
    sales_product["revenue"]
    / total_revenue
    * 100
)

sales_product = sales_product.sort_values(
    "revenue",
    ascending=False
)

sales_region = (
    sales
    .groupby("region")
    .agg(
        units_sold=("units_sold", "sum"),
        revenue=("revenue", "sum")
    )
    .reset_index()
)

sales_region["revenue_share_pct"] = (
    sales_region["revenue"]
    / total_revenue
    * 100
)

sales_region = sales_region.sort_values(
    "revenue",
    ascending=False
)

print("\n" + "=" * 60)
print("SALES BY PRODUCT")
print("=" * 60)

print(
    sales_product[
        ["product", "units_sold", "revenue", "revenue_share_pct"]
    ].round(2).to_string(index=False)
)

print("\n" + "=" * 60)
print("SALES BY REGION")
print("=" * 60)

print(
    sales_region[
        ["region", "units_sold", "revenue", "revenue_share_pct"]
    ].round(2).to_string(index=False)
)


# ============================================================
# 9. ANOMALY DETECTION
# ============================================================

# These are screening rules, not proof of actual problems.
anomalies = production[
    (production["achievement_pct"] < 75)
    |
    (production["rejection_rate_pct"] > 7)
    |
    (production["downtime_minutes"] > 180)
].copy()

print("\n" + "=" * 60)
print("POTENTIAL OPERATIONAL ANOMALIES")
print("=" * 60)

print(f"Potential anomaly records: {len(anomalies)}")

print(
    anomalies[
        [
            "date",
            "plant",
            "product",
            "machine",
            "shift",
            "achievement_pct",
            "rejection_rate_pct",
            "downtime_minutes"
        ]
    ]
    .head(20)
    .round(2)
    .to_string(index=False)
)


# ============================================================
# 10. CHART 1 — MACHINE DOWNTIME
# ============================================================

plt.figure(figsize=(10, 6))

machine_chart = machine_analysis.sort_values(
    "downtime_hours",
    ascending=True
)

plt.barh(
    machine_chart["machine"],
    machine_chart["downtime_hours"]
)

plt.title("Machine Downtime Analysis")
plt.xlabel("Downtime (Hours)")
plt.ylabel("Machine")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "01_machine_downtime.png",
    dpi=300
)

plt.close()


# ============================================================
# 11. CHART 2 — TARGET VS ACTUAL BY PLANT
# ============================================================

plt.figure(figsize=(10, 6))

x = range(len(plant_analysis))

plt.bar(
    [i - 0.2 for i in x],
    plant_analysis["target_units"],
    width=0.4,
    label="Target"
)

plt.bar(
    [i + 0.2 for i in x],
    plant_analysis["produced_units"],
    width=0.4,
    label="Actual"
)

plt.xticks(
    list(x),
    plant_analysis["plant"],
    rotation=0
)

plt.title("Target vs Actual Production by Plant")
plt.xlabel("Plant")
plt.ylabel("Units")
plt.legend()

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "02_target_vs_actual.png",
    dpi=300
)

plt.close()


# ============================================================
# 12. CHART 3 — MONTHLY PRODUCTION TREND
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    monthly_production["month"],
    monthly_production["target_units"],
    marker="o",
    label="Target"
)

plt.plot(
    monthly_production["month"],
    monthly_production["produced_units"],
    marker="o",
    label="Actual"
)

plt.title("Monthly Production: Target vs Actual")
plt.xlabel("Month")
plt.ylabel("Units")
plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "03_monthly_production.png",
    dpi=300
)

plt.close()


# ============================================================
# 13. CHART 4 — PRODUCT REJECTION
# ============================================================

plt.figure(figsize=(10, 6))

quality_chart = product_analysis.sort_values(
    "rejection_rate_pct"
)

plt.barh(
    quality_chart["product"],
    quality_chart["rejection_rate_pct"]
)

plt.title("Product Rejection Rate")
plt.xlabel("Rejection Rate (%)")
plt.ylabel("Product")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "04_product_rejection.png",
    dpi=300
)

plt.close()


# ============================================================
# 14. CHART 5 — PLANT PERFORMANCE
# ============================================================

plt.figure(figsize=(10, 6))

plt.bar(
    plant_analysis["plant"],
    plant_analysis["achievement_pct"]
)

plt.title("Production Achievement by Plant")
plt.xlabel("Plant")
plt.ylabel("Achievement (%)")

plt.ylim(90, 100)

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "05_plant_performance.png",
    dpi=300
)

plt.close()


# ============================================================
# 15. CHART 6 — INVENTORY REORDER RATE
# ============================================================

plt.figure(figsize=(10, 6))

inventory_chart = inventory_product.sort_values(
    "reorder_rate_pct"
)

plt.barh(
    inventory_chart["product"],
    inventory_chart["reorder_rate_pct"]
)

plt.title("Inventory Reorder Rate by Product")
plt.xlabel("Records Requiring Reorder (%)")
plt.ylabel("Product")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "06_inventory_reorder.png",
    dpi=300
)

plt.close()


# ============================================================
# 16. CHART 7 — SALES BY PRODUCT
# ============================================================

plt.figure(figsize=(10, 6))

sales_chart = sales_product.sort_values(
    "revenue"
)

plt.barh(
    sales_chart["product"],
    sales_chart["revenue"] / 10000000
)

plt.title("Revenue by Product")
plt.xlabel("Revenue (₹ Crore)")
plt.ylabel("Product")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "07_sales_by_product.png",
    dpi=300
)

plt.close()


# ============================================================
# 17. CHART 8 — SALES BY REGION
# ============================================================

plt.figure(figsize=(10, 6))

region_chart = sales_region.sort_values(
    "revenue"
)

plt.barh(
    region_chart["region"],
    region_chart["revenue"] / 10000000
)

plt.title("Revenue by Region")
plt.xlabel("Revenue (₹ Crore)")
plt.ylabel("Region")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "08_sales_by_region.png",
    dpi=300
)

plt.close()


# ============================================================
# 18. SAVE ANALYSIS TO EXCEL
# ============================================================

analysis_file = (
    OUTPUT_DIR /
    "manufacturing_analysis_results.xlsx"
)

kpis = pd.DataFrame({
    "KPI": [
        "Total Target Units",
        "Total Production Units",
        "Production Achievement %",
        "Total Rejected Units",
        "Overall Rejection Rate %",
        "Total Downtime Hours",
        "Total Revenue",
        "Total Units Sold",
        "Inventory Reorder Records",
        "Inventory Reorder Rate %"
    ],
    "Value": [
        total_target,
        total_production,
        production_achievement,
        total_rejected,
        rejection_rate,
        total_downtime_hours,
        total_revenue,
        total_units_sold,
        reorder_records,
        reorder_percentage
    ]
})

with pd.ExcelWriter(
    analysis_file,
    engine="openpyxl"
) as writer:

    kpis.to_excel(
        writer,
        sheet_name="Executive KPIs",
        index=False
    )

    machine_analysis.to_excel(
        writer,
        sheet_name="Machine Analysis",
        index=False
    )

    product_analysis.to_excel(
        writer,
        sheet_name="Product Quality",
        index=False
    )

    plant_analysis.to_excel(
        writer,
        sheet_name="Plant Analysis",
        index=False
    )

    shift_analysis.to_excel(
        writer,
        sheet_name="Shift Analysis",
        index=False
    )

    monthly_production.to_excel(
        writer,
        sheet_name="Monthly Production",
        index=False
    )

    inventory_product.to_excel(
        writer,
        sheet_name="Inventory Analysis",
        index=False
    )

    sales_product.to_excel(
        writer,
        sheet_name="Sales Product",
        index=False
    )

    sales_region.to_excel(
        writer,
        sheet_name="Sales Region",
        index=False
    )

    anomalies.to_excel(
        writer,
        sheet_name="Potential Anomalies",
        index=False
    )


# ============================================================
# FINISHED
# ============================================================

print("\n" + "=" * 60)
print("ANALYSIS COMPLETE")
print("=" * 60)

print("\nCreated folder:")
print(OUTPUT_DIR)

print("\nCreated charts:")

for file in sorted(OUTPUT_DIR.glob("*.png")):
    print(" -", file.name)

print("\nCreated analysis workbook:")
print(" - manufacturing_analysis_results.xlsx")

print("\nNext stage:")
print("Import the analysis into Tableau and build the interactive dashboard.")