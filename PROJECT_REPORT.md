# EV Market Performance & Insights — Project Report

## 1. Objective
Analyze the supplied electric-vehicle dataset to compare vehicle categories, driving range, battery technologies, pricing, customer ratings and market regions.

## 2. Dataset overview
The training dataset contains 200,000 records and 37 fields. The test dataset contains 100,000 records and 37 fields. Fields include vehicle specifications, battery characteristics, pricing, safety, customer ratings, sales and recommended use cases.

## 3. Key descriptive findings
- Mean listed driving range: **324.5 km**; median: **337.9 km**.
- Mean battery capacity: **78.2 kWh**.
- Mean listed price: **$64,921**; median listed price: **$42,815**.
- Mean customer rating: **4.09/5**.
- Mean five-year battery degradation field: **12.31%**.
- Most frequent recommended use case: **Family Daily Use**.
- Most frequent battery type: **NMC**.
- The highest average range among categories is **Luxury Sedan** at approximately **550.6 km**.
- The lowest average range among categories is **Two-Wheeler Scooter** at approximately **105.0 km**.

## 4. Data quality
The training file has 18,996 missing cells across fields and 1 fully duplicated rows. Missing values occur in fields including battery cycle life, resale value, infotainment screen size, annual sales and customer rating. Before advanced modelling, investigate outliers and missingness, validate units, and avoid treating extreme values as typical without checking them.

## 5. Dashboard and methods
The preview dashboard presents KPI cards and charts for category mix, average range by category, battery type, market region and recommended use case. The analysis is descriptive: it summarizes the supplied data and does not establish causation.

## 6. Recommendations
1. Compare range and price together, rather than using range alone to identify value.
2. Evaluate battery technologies using both range and degradation indicators.
3. Segment results by category and use case to avoid unfair comparisons between scooters, passenger cars, trucks and buses.
4. Clean missing values and investigate extreme values before building forecasts.
5. Use Tableau filters for category, region, battery type, manufacturer and model year to explore the dataset interactively.

## 7. Limitations
The findings describe only the provided dataset. The dataset's representativeness and data-generation methodology are not independently verified; therefore, do not generalize the values to the complete global EV market.
