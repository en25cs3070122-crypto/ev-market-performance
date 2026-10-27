# Tableau Dashboard Build Guide

## Connect your data
1. Open Tableau Public or Tableau Desktop.
2. Choose **Text File** and select `ev_market_train(1).csv` (the original training dataset).
3. Check data types: `model_year` as whole number; range, battery, price, efficiency, rating and sales as numeric; category, region, manufacturer and battery type as dimensions.
4. Rename the data source to `EV Market Training Data`.

## Recommended dashboard: Electric Vehicle Market Performance & Insights
Create these worksheets:
1. **KPI – Average Range**: `AVG(range_km)` as a large number.
2. **KPI – Average Price**: `AVG(price_usd)` formatted as currency.
3. **KPI – Average Battery Capacity**: `AVG(battery_capacity_kwh)`.
4. **Vehicle Mix by Category**: bar chart; Rows = `category`, Columns = `COUNT(vehicle_id)`, sort descending.
5. **Average Range by Category**: horizontal bars; Rows = `category`, Columns = `AVG(range_km)`.
6. **Average Price vs Range**: scatter plot; Columns = `AVG(range_km)`, Rows = `AVG(price_usd)`, Detail = `model_name`, Color = `category` (if crowded, use category-level aggregation).
7. **Battery Technology Comparison**: bars by `battery_type`; compare `AVG(range_km)` and `AVG(battery_degradation_pct_5yr)`.
8. **Market Region Comparison**: bars by `market_region`; measure = `COUNT(vehicle_id)` or `AVG(range_km)`.
9. **Customer Ratings**: histogram or box plot of `customer_rating`.

## Dashboard layout and filters
- Put the KPI cards across the top.
- Add category, market_region, battery_type, model_year and manufacturer filters.
- Use **Apply to Worksheets → All Using This Data Source** for each filter.
- Add a clear title, captions with units, and a note: “Summary statistics are based on the supplied training dataset.”
- Add a story point with 3 findings: average range is about 325 km; the largest listed use case is Family Daily Use; average customer rating is about 4.1/5. These are descriptive dataset results, not claims about the whole real-world EV market.
- Publish using Tableau Public: **Server → Tableau Public → Save to Tableau Public As**. Then copy the published view URL for the Demo Link field.
