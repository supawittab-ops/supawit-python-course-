def get_temperatures():
    temps = [31, 30, 29, 28, 27, 25, 26]
    return temps


def analyze_temps(temp_list):
    average = sum(temp_list) / len(temp_list)
    high = max(temp_list)
    low = min(temp_list)
    return (average, high, low)


def display_analysis(avg, high, low):
    print("Temperature Analysis for the Week:")
    print("Average: %.1f C" % avg)
    print("Highest: %d C" % high)
    print("Lowest: %d C" % low)


temps = get_temperatures()
avg, high, low = analyze_temps(temps)
display_analysis(avg, high, low)