import sys

def main():
    if len(sys.argv) != 7:
        print("Usage: python hospital.py <name> <ward> <diagnosis> <s1> <s2> <s3>")
        sys.exit(1)

    name = sys.argv[1]
    ward = sys.argv[2]
    diagnosis = sys.argv[3]
    s1 = float(sys.argv[4])
    s2 = float(sys.argv[5])
    s3 = float(sys.argv[6])

    avg = (s1 + s2 + s3) / 3

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

    print("Patient Name :", name)
    print("Ward :", ward)
    print("Diagnosis :", diagnosis)
    print("Average Score :", avg)
    print("Health Status :", status)

if __name__ == "__main__":
    main()
