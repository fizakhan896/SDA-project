import matplotlib.pyplot as plt

# REGION-WISE BAR CHART
def region_bar_chart(data):
    grouped = data.groupby("Region")["Value"].sum()

    grouped.plot(kind="bar")
    plt.title("Region-wise GDP")
    plt.xlabel("Region")
    plt.ylabel("GDP Value")
    plt.tight_layout()
    plt.show()

# REGION-WISE PIE CHART
def region_pie_chart(data):
    grouped = data.groupby("Region")["Value"].sum()

    grouped.plot(kind="pie", autopct="%1.1f%%")
    plt.title("GDP Share by Region")
    plt.ylabel("")
    plt.show()

# YEAR-WISE LINE GRAPH
def year_line_chart(data):
    grouped = data.groupby("Year")["Value"].sum()

    grouped.plot(kind="line")
    plt.title("GDP Trend Over Years")
    plt.xlabel("Year")
    plt.ylabel("GDP Value")
    plt.show()

# YEAR-WISE HISTOGRAM
def year_histogram(data, year):
    year_data = data[data["Year"] == year]["Value"]

    plt.hist(year_data, bins=10)
    plt.title(f"GDP Distribution in {year}")
    plt.xlabel("GDP Value")
    plt.ylabel("Frequency")
    plt.show()
