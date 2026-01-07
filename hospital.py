import sys

# Read inputs from command line
name = sys.argv[1]
ward = sys.argv[2]
diagnosis = sys.argv[3]
s1 = float(sys.argv[4])
s2 = float(sys.argv[5])
s3 = float(sys.argv[6])

# Calculate average
avg = (s1 + s2 + s3) / 3

# Decide health status
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
print("Average Score :", avg)
print("Health Status :", status)
