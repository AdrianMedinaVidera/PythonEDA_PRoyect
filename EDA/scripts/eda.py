"""
EDA script for Bank Marketing dataset.
Covers: cleaning, descriptive analysis, visualizations, simple report generation.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import argparse

sns.set(style="whitegrid")

def load_data(path):
    df = pd.read_csv(path, sep=",")
    return df

def basic_cleaning(df):
    # Standardize column names
    df.columns = [c.strip() for c in df.columns]
    # Try parse date if exists
    if "date" in df.columns:
        try:
            df["date"] = pd.to_datetime(df["date"], errors="coerce")
        except Exception:
            pass
    # Replace common missing markers
    df.replace(["unknown", ""], np.nan, inplace=True)
    # Convert binary-like columns to 0/1 if they are 'yes'/'no' or '1'/'0'
    for col in ["default","housing","loan"]:
        if col in df.columns:
            df[col] = df[col].map({"yes":1, "no":0, "1":1, "0":0}).fillna(df[col])
    return df

def descriptive_stats(df, out_dir):
    desc = df.describe(include="all").transpose()
    desc.to_csv(os.path.join(out_dir, "descriptive_stats.csv"))
    return desc

def plots(df, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    # Histogram of age
    plt.figure(figsize=(8,4))
    df["age"].dropna().astype(int).hist(bins=30)
    plt.title("Distribución de edades")
    plt.xlabel("Edad")
    plt.savefig(os.path.join(out_dir, "age_histogram.png"))
    plt.close()

    # Conversion rate by contact method
    if "contact" in df.columns and "y" in df.columns:
        conv = df.groupby("contact")["y"].apply(lambda x: (x=="yes").mean()).sort_values(ascending=False)
        conv.plot(kind="bar")
        plt.ylabel("Tasa de conversión (proporción 'yes')")
        plt.title("Tasa de conversión por método de contacto")
        plt.tight_layout()
        plt.savefig(os.path.join(out_dir, "conversion_by_contact.png"))
        plt.close()

    # Correlation heatmap for numeric features
    num = df.select_dtypes(include=[np.number])
    if not num.empty:
        corr = num.corr()
        plt.figure(figsize=(10,8))
        sns.heatmap(corr, annot=True, fmt=".2f", cmap="viridis")
        plt.title("Mapa de correlaciones (numéricas)")
        plt.tight_layout()
        plt.savefig(os.path.join(out_dir, "correlation_heatmap.png"))
        plt.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/bank-additional.csv")
    parser.add_argument("--out", default="reports/figures")
    args = parser.parse_args()
    df = load_data(args.data)
    df = basic_cleaning(df)
    os.makedirs("reports", exist_ok=True)
    desc = descriptive_stats(df, "reports")
    plots(df, args.out)
    print("EDA completo. Resultados en ./reports")

if __name__ == "__main__":
    main()
