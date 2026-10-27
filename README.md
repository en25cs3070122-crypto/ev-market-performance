# Electric Vehicle Market Performance & Insights

A beginner-friendly data analytics project using the supplied EV market dataset. It includes a web dashboard preview, a reproducible Python analysis script, a small sample CSV for repository upload, and a Tableau build guide.

## Dataset
- Training file: 200,000 rows × 37 columns
- Test file: 100,000 rows × 37 columns
- This ZIP contains a **2,000-row sample** so the repository stays small. Keep your original CSV files separately.
- Copy/rename the original training file to `data/ev_market_train.csv` to run the full analysis script. Optionally copy the test file to `data/ev_market_test.csv`.

## Quick start
1. Open `index.html` with a local web server, or publish the repository with GitHub Pages to get a shareable demo URL.
2. For the full dataset analysis, put your original training CSV in `data/` and name it `ev_market_train.csv`.
3. Install Python and pandas: `pip install pandas`
4. Run: `python analysis/analyze_ev_market.py`
5. Follow `TABLEAU_GUIDE.md` to recreate the visuals in Tableau and publish the actual Tableau dashboard.

## Current dataset snapshot
- Average listed driving range: **324.5 km**
- Median listed driving range: **337.9 km**
- Average battery capacity: **78.2 kWh**
- Average listed price: **$64,921**
- Average customer rating: **4.09/5**
- Most frequent use case: **Family Daily Use**
- Most frequent battery type: **NMC**
- Rows with at least one missing value exist; review missingness before deeper analysis.

## Important note
This is a descriptive analysis of the supplied dataset. It should not be interpreted as a verified representation of the entire real-world EV market. The dashboard preview uses aggregate values calculated from the training CSV. To submit a Tableau project, publish your own workbook on Tableau Public and use its URL as the demo link.

## Suggested repository files
- `index.html` – interactive dashboard preview (GitHub Pages-ready)
- `dashboard/dashboard_data.json` – aggregated chart data
- `data/ev_market_sample.csv` – 2,000-row sample
- `analysis/analyze_ev_market.py` – reproducible analysis
- `TABLEAU_GUIDE.md` – Tableau dashboard instructions

## Publish a demo link with GitHub Pages
1. Create a **public** GitHub repository, for example `ev-market-performance`.
2. Upload the files and folders from this ZIP (upload the contents, not the ZIP itself). Keep `index.html` and `dashboard_data.json` together in the repository root.
3. Open repository **Settings → Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**; select branch `main` and folder `/(root)`, then Save.
5. Wait a few minutes. Your demo URL will look like `https://YOUR-USERNAME.github.io/ev-market-performance/`. Replace `YOUR-USERNAME` with your GitHub username.
