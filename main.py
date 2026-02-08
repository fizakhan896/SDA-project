from data_loader import load_data, load_config
from data_processor import (
    validate_inputs,
    filter_data,
    calculate_gdp,
    save_output
)
from dashboard import show_dashboard

def main():
    print("MAIN FILE IS RUNNING")  # debug line

    data = load_data()
    config = load_config()

    validate_inputs(data, config)

    filtered = filter_data(data, config["region"], config["year"])
    result = calculate_gdp(filtered, config["operation"])

    save_output(result)
    show_dashboard(result)

if __name__ == "__main__":
    main()
