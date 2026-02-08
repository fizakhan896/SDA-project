import matplotlib.pyplot as plt

def show_dashboard(result):
    print("\nGDP DASHBOARD")
    print("----------------")
    print(f"Operation: {result['operation']}")
    print(f"Countries: {result['countries']}")
    print(f"GDP Result: {result['result']}")

    plt.bar(["GDP Result"], [result["result"]])
    plt.title("GDP Analysis Result")
    plt.ylabel("GDP Value")
    plt.show()
   




