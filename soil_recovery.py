
# BOOMIRAKSHA - Soil Recovery Kit

def assess_soil(ph, organic_matter, chemical_use):
    print("BOOMIRAKSHA Soil Assessment")
    
    if ph < 6.0:
        print("Soil is acidic. Check soil treatment needs.")
    elif ph > 7.5:
        print("Soil is alkaline. Check soil treatment needs.")
    else:
        print("Soil pH is in the selected target range.")

    if organic_matter < 3:
        print("Consider adding suitable organic compost.")

    if chemical_use.lower() == "high":
        print("Consider reducing unnecessary chemical use.")

    print("Consult a soil expert before applying treatments.")

ph = float(input("Enter soil pH: "))
organic_matter = float(input("Enter organic matter percentage: "))
chemical_use = input("Chemical use (low/medium/high): ")

assess_soil(ph, organic_matter, chemical_use)
