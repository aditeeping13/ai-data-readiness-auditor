"""Retail-specific, non-destructive quality rules for uploaded tabular data.

Rules are explicitly mapped to columns by the caller; no column names are
assumed. Rows are numbered 2+ to correspond to CSV/Excel header-row exports.
"""
from __future__ import annotations

import pandas as pd

RULES = {
    "missing_product_id": ("product_id", "Missing product identifier"),
    "negative_price": ("price", "Negative product price"),
    "invalid_inventory": ("inventory", "Invalid inventory quantity"),
    "duplicate_transaction_id": ("transaction_id", "Repeated transaction identifier"),
}

ISSUE_COLUMNS = ["row_number", "rule", "column", "value", "message"]


def validate_retail_data(df: pd.DataFrame, columns: dict[str, str | None]) -> pd.DataFrame:
    """Return one issue per failing cell/transaction; do not modify ``df``.

    Price: numeric >= 0 (missing/unparseable flagged).
    Inventory: whole-number >= 0 (missing/unparseable flagged).
    Product ID: required nonblank; missing values and common placeholders flagged.
    Transaction ID: nonblank repeated values beyond the first flagged. Null IDs
      aren't treated as duplicate IDs (no uniqueness assumption for missing).
    Unmapped rules are skipped; bad mappings raise ValueError rather than
      silently producing misleading results.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    result: list[dict] = []
    for logical, physical in columns.items():
        if logical not in {key for key, _ in RULES.values()}:
            raise ValueError(f"Unknown retail field: {logical}")
        if physical and physical not in df.columns:
            raise ValueError(f"Column not found: {physical}")

    placeholder = {"", "n/a", "na", "null", "none", "unknown", "tbd", "-"}
    def blank(series: pd.Series) -> pd.Series:
        return series.isna() | series.astype("string").str.strip().str.lower().isin(placeholder).fillna(False)

    def emit(mask: pd.Series, rule: str, col: str, msg: str) -> None:
        for position in range(len(df)):
            if bool(mask.iloc[position]):
                value = df.iloc[position][col]
                result.append({"row_number": position + 2, "rule": rule, "column": col,
                               "value": "" if pd.isna(value) else str(value), "message": msg})

    if (col := columns.get("product_id")):
        emit(blank(df[col]), "missing_product_id", col, "Product ID is missing or blank")

    if (col := columns.get("price")):
        raw = df[col].astype("string").str.replace(",", "", regex=False).str.strip()
        numeric = pd.to_numeric(raw, errors="coerce")
        emit(numeric.isna() | (numeric < 0), "invalid_price", col,
             "Price must be a valid non-negative number")

    if (col := columns.get("inventory")):
        raw = df[col].astype("string").str.replace(",", "", regex=False).str.strip()
        numeric = pd.to_numeric(raw, errors="coerce")
        emit(numeric.isna() | (numeric < 0) | (numeric.mod(1) != 0), "invalid_inventory", col,
             "Inventory must be a non-negative whole number")

    if (col := columns.get("transaction_id")):
        ids = df[col].astype("string").str.strip()
        missing = blank(df[col])
        emit(ids.duplicated(keep="first").fillna(False) & ~missing,
             "duplicate_transaction_id", col, "Repeated transaction ID (after first occurrence)")

    return pd.DataFrame(result, columns=ISSUE_COLUMNS)
