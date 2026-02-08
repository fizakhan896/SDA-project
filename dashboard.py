from data_loader import load_data, load_config
from data_processor import (
    validate_inputs,
    filter_data,
    calculate_gdp,
    save_output
)
from visualizer import (
    region_bar_chart,
    region_pie_chart,
    year_line_chart,
    year_histogram
)

def show_dashboard():
    # Load config and data
    config = load_config()
    data = load_data()

    # Validate config
    validate_inputs(data, config)

    # Display config
    print("\n========== GDP ANALYTICS DASHBOARD ==========")
    print(f"Region    : {config['region']}")
    print(f"Year      : {config['year']}")
    print(f"Operation : {config['operation']}")
    print("============================================")

    # Compute result (filtered data)
    filtered = filter_data(data, config["region"], config["year"])
    result = calculate_gdp(filtered, config["operation"])

    # Display result
    print("\n--- Computed Result ---")
    print(f"Countries Considered : {result['countries']}")
    print(f"GDP Result           : {result['result']}")

    # Save output
    save_output(result)

    # ✅ PASS FULL DATAFRAME DIRECTLY (THIS FIXES YOUR ERROR)
    region_bar_chart(data)
    region_pie_chart(data)
    year_line_chart(data)
    year_histogram(data, config["year"])
    plt.show()
