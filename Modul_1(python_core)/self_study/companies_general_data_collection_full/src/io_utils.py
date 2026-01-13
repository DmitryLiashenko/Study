from __future__ import annotations
import pandas as pd

def read_companies(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    if "company_name" not in df.columns:
        raise ValueError("Input CSV must contain a 'company_name' column.")
    for col in ("country", "website_hint"):
        if col not in df.columns:
            df[col] = ""
    df["company_name"] = df["company_name"].astype(str).str.strip()
    df["country"] = df["country"].astype(str).str.strip()
    df["website_hint"] = df["website_hint"].astype(str).str.strip()
    return df

def write_results(df: pd.DataFrame, path: str) -> None:
    df.to_csv(path, index=False)
