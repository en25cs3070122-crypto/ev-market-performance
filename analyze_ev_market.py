"""Analyze EV market train/test CSVs. Run: python analysis/analyze_ev_market.py"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
train_path = ROOT / "data" / "ev_market_train.csv"
test_path = ROOT / "data" / "ev_market_test.csv"
if not train_path.exists():
    raise FileNotFoundError(
        f"Put the supplied training CSV at {train_path} (rename ev_market_train(1).csv to ev_market_train.csv)."
    )
train = pd.read_csv(train_path)
print("TRAIN SHAPE:", train.shape)
print("TEST FILE PRESENT:", test_path.exists())
print("\\nMissing values by column:")
print(train.isna().sum().sort_values(ascending=False).head(15))
print("\\nKey metrics:")
for col in ["range_km", "battery_capacity_kwh", "efficiency_wh_per_km",
            "price_usd", "customer_rating", "co2_saved_tons_per_year"]:
    print(f"{col}: mean={train[col].mean():.2f}, median={train[col].median():.2f}")
print("\\nCategory summary:")
summary = train.groupby("category").agg(
    vehicle_count=("vehicle_id", "count"),
    avg_range_km=("range_km", "mean"),
    avg_price_usd=("price_usd", "mean"),
    avg_rating=("customer_rating", "mean")
).sort_values("vehicle_count", ascending=False)
print(summary.round(2).to_string())
out = ROOT / "analysis" / "category_summary.csv"
summary.to_csv(out)
print(f"\\nSaved: {out}")
