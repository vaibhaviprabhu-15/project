name = "Abcd"
ward = "General"
diagnosis = "Flu"
s1 = 75.0
s2 = 85.0
s3 = 90.0

# Calculate average
avg = (s1 + s2 + s3) / 3

# Decide health status using if statements
if avg >= 90:
    status = "Critical Care Not Required"
elif avg >= 80:
    status = "Stable"
elif avg >= 65:
    status = "Under Observation"
elif avg >= 50:
    status = "Needs Attention"
elif avg >= 40:
    status = "High Risk"
else:
    status = "Critical"

# Output
print("Patient Name :", name)
print("Ward :", ward)
print("Diagnosis :", diagnosis)
print("Average Score :", round(avg, 2))
print("Health Status :", status)

        
   
