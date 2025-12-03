import csv
from collections import defaultdict
from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[1] / "inventory_export_1.csv"
OUT_ALL_OOS = Path(__file__).resolve().parents[1] / "inventory_out_of_stock_all_locations.csv"
OUT_PARTIAL_OOS = Path(__file__).resolve().parents[1] / "inventory_out_of_stock_partial_locations.csv"
OUT_VARIANT_ALL_OOS = Path(__file__).resolve().parents[1] / "inventory_variants_out_of_stock_all_locations.csv"
OUT_VARIANT_PARTIAL_OOS = Path(__file__).resolve().parents[1] / "inventory_variants_out_of_stock_partial_locations.csv"
OUT_VARIANT_ALL_OOS_SUM = Path(__file__).resolve().parents[1] / "inventory_variants_oos_summary_all_locations.csv"
OUT_VARIANT_PARTIAL_OOS_SUM = Path(__file__).resolve().parents[1] / "inventory_variants_oos_summary_partial_locations.csv"

REQUIRED_COLUMNS = {
    "Handle",
    "Title",
    "Location",
    "Available (not editable)",
    "SKU",
    "Option1 Name",
    "Option1 Value",
    "Option2 Name",
    "Option2 Value",
    "Option3 Name",
    "Option3 Value",
}

def parse_int(value: str) -> int:
    try:
        v = value.strip()
        if v == "":
            return 0
        return int(float(v))
    except Exception:
        return 0

def main() -> None:
    if not INPUT_PATH.exists():
        raise SystemExit(f"Input file not found: {INPUT_PATH}")

    with INPUT_PATH.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        header = set(reader.fieldnames or [])
        missing = REQUIRED_COLUMNS - header
        if missing:
            raise SystemExit(f"Missing required columns: {sorted(missing)}")

        # Aggregates (product-level)
        product_title: dict[str, str] = {}
        product_total_available: defaultdict[str, int] = defaultdict(int)
        product_location_available: defaultdict[tuple[str, str], int] = defaultdict(int)
        product_locations: defaultdict[str, set[str]] = defaultdict(set)

        # Aggregates (variant-level, keyed by SKU primarily)
        variant_title: dict[str, str] = {}
        variant_handle: dict[str, str] = {}
        variant_options: dict[str, str] = {}
        variant_total_available: defaultdict[str, int] = defaultdict(int)
        variant_location_available: defaultdict[tuple[str, str], int] = defaultdict(int)
        variant_locations: defaultdict[str, set[str]] = defaultdict(set)
        variant_option1_value: dict[str, str] = {}

        for row in reader:
            handle = row.get("Handle", "").strip()
            title = row.get("Title", "").strip()
            location = row.get("Location", "").strip() or "(Unknown)"
            available = parse_int(row.get("Available (not editable)", "0"))
            sku = row.get("SKU", "").strip() or "(no-sku)"
            opt_parts = []
            option1_value = ""
            for idx, (n_key, v_key) in enumerate((
                ("Option1 Name", "Option1 Value"),
                ("Option2 Name", "Option2 Value"),
                ("Option3 Name", "Option3 Value"),
            ), start=1):
                n = (row.get(n_key, "") or "").strip()
                v = (row.get(v_key, "") or "").strip()
                if n or v:
                    # Keep readable representation
                    label = n if n else "Option"
                    opt_parts.append(f"{label}: {v}")
                if idx == 1:
                    option1_value = v
            options_str = ", ".join(opt_parts) if opt_parts else ""

            if not handle:
                continue

            product_title[handle] = title or product_title.get(handle, "")
            product_total_available[handle] += available
            product_location_available[(handle, location)] += available
            product_locations[handle].add(location)

            # Variant aggregates
            variant_title[sku] = title or variant_title.get(sku, "")
            variant_handle[sku] = handle or variant_handle.get(sku, "")
            variant_options[sku] = options_str or variant_options.get(sku, "")
            if option1_value:
                variant_option1_value[sku] = option1_value
            variant_total_available[sku] += available
            variant_location_available[(sku, location)] += available
            variant_locations[sku].add(location)

    # Classify products
    all_oos_rows = []
    partial_oos_rows = []

    for handle, total_avail in product_total_available.items():
        title = product_title.get(handle, "")
        locations = sorted(product_locations.get(handle, set()))
        # Summaries per location
        loc_avails = {loc: product_location_available.get((handle, loc), 0) for loc in locations}
        any_in_stock = any(av > 0 for av in loc_avails.values())
        all_zero = all(av == 0 for av in loc_avails.values())

        if all_zero:
            all_oos_rows.append({
                "handle": handle,
                "title": title,
                "total_available": total_avail,
                "locations": ", ".join(locations),
            })
        else:
            # Out of stock in select locations if at least one is zero and at least one > 0
            has_zero = any(av == 0 for av in loc_avails.values())
            has_positive = any(av > 0 for av in loc_avails.values())
            if has_zero and has_positive:
                partial_oos_rows.append({
                    "handle": handle,
                    "title": title,
                    "locations_oos": ", ".join(sorted([loc for loc, av in loc_avails.items() if av == 0])),
                    "locations_in_stock": ", ".join(sorted([loc for loc, av in loc_avails.items() if av > 0])),
                })

    # Write outputs
    with OUT_ALL_OOS.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["handle", "title", "total_available", "locations"])
        writer.writeheader()
        writer.writerows(sorted(all_oos_rows, key=lambda r: (r["title"], r["handle"])) )

    with OUT_PARTIAL_OOS.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["handle", "title", "locations_oos", "locations_in_stock"])
        writer.writeheader()
        writer.writerows(sorted(partial_oos_rows, key=lambda r: (r["title"], r["handle"])) )

    # Classify variants
    variant_all_oos_rows = []
    variant_partial_oos_rows = []

    for sku, total_avail in variant_total_available.items():
        title = variant_title.get(sku, "")
        handle = variant_handle.get(sku, "")
        options_str = variant_options.get(sku, "")
        locations = sorted(variant_locations.get(sku, set()))
        loc_avails = {loc: variant_location_available.get((sku, loc), 0) for loc in locations}
        all_zero = all(av == 0 for av in loc_avails.values())
        has_zero = any(av == 0 for av in loc_avails.values())
        has_positive = any(av > 0 for av in loc_avails.values())

        if all_zero:
            variant_all_oos_rows.append({
                "sku": sku,
                "handle": handle,
                "title": title,
                "options": options_str,
                "total_available": total_avail,
                "locations": ", ".join(locations),
            })
        elif has_zero and has_positive:
            variant_partial_oos_rows.append({
                "sku": sku,
                "handle": handle,
                "title": title,
                "options": options_str,
                "locations_oos": ", ".join(sorted([loc for loc, av in loc_avails.items() if av == 0])),
                "locations_in_stock": ", ".join(sorted([loc for loc, av in loc_avails.items() if av > 0])),
            })

    with OUT_VARIANT_ALL_OOS.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["sku", "handle", "title", "options", "total_available", "locations"],
        )
        writer.writeheader()
        writer.writerows(sorted(variant_all_oos_rows, key=lambda r: (r["title"], r["handle"], r["sku"])) )

    with OUT_VARIANT_PARTIAL_OOS.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["sku", "handle", "title", "options", "locations_oos", "locations_in_stock"],
        )
        writer.writeheader()
        writer.writerows(sorted(variant_partial_oos_rows, key=lambda r: (r["title"], r["handle"], r["sku"])) )

    # Condensed summaries (sku, product name, option1 value)
    with OUT_VARIANT_ALL_OOS_SUM.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["sku", "title", "option1_value"],
        )
        writer.writeheader()
        for r in sorted(variant_all_oos_rows, key=lambda r: (r["title"], r["sku"])):
            writer.writerow({
                "sku": r["sku"],
                "title": r["title"],
                "option1_value": variant_option1_value.get(r["sku"], ""),
            })

    with OUT_VARIANT_PARTIAL_OOS_SUM.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["sku", "title", "option1_value", "locations_oos", "locations_in_stock"],
        )
        writer.writeheader()
        for r in sorted(variant_partial_oos_rows, key=lambda r: (r["title"], r["sku"])):
            writer.writerow({
                "sku": r["sku"],
                "title": r["title"],
                "option1_value": variant_option1_value.get(r["sku"], ""),
                "locations_oos": r["locations_oos"],
                "locations_in_stock": r["locations_in_stock"],
            })

    print(f"Wrote {len(all_oos_rows)} all-location OOS products -> {OUT_ALL_OOS}")
    print(f"Wrote {len(partial_oos_rows)} partial-location OOS products -> {OUT_PARTIAL_OOS}")
    print(f"Wrote {len(variant_all_oos_rows)} all-location OOS variants -> {OUT_VARIANT_ALL_OOS}")
    print(f"Wrote {len(variant_partial_oos_rows)} partial-location OOS variants -> {OUT_VARIANT_PARTIAL_OOS}")
    print(f"Wrote condensed all-location OOS variant summary -> {OUT_VARIANT_ALL_OOS_SUM}")
    print(f"Wrote condensed partial-location OOS variant summary -> {OUT_VARIANT_PARTIAL_OOS_SUM}")

if __name__ == "__main__":
    main()


