import json

def validate_inputs(data, config):
    for key in ["region", "year", "operation"]:
        if key not in config:
            raise ValueError(f"Missing config key: {key}")

    if config["operation"] not in ["sum", "average"]:
        raise ValueError("Invalid operation")

def filter_data(data, region, year):
    rows = data.to_dict(orient="records")

    filtered = list(
        filter(lambda r: r["Region"] == region and r["Year"] == year, rows)
    )

    if not filtered:
        raise ValueError("No data found after filtering")

    return filtered

def calculate_gdp(filtered, operation):
    values = list(map(lambda r: r["Value"], filtered))

    if operation == "sum":
        result = sum(values)
    else:
        result = sum(values) / len(values)

    return {
        "operation": operation,
        "countries": len(values),
        "result": result
    }

def save_output(result):
    with open("data/output_result.json", "w") as f:
        json.dump(result, f, indent=4)
