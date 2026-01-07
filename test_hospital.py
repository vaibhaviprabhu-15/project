import subprocess
import sys

def run_program(args):
    result = subprocess.run(
        [sys.executable, "hospital.py"] + args,
        capture_output=True,
        text=True
    )
    return result.stdout

def test_critical_care_not_required():
    output = run_program(["John", "ICU", "Fever", "95", "92", "93"])
    assert "Critical Care Not Required" in output

def test_stable():
    output = run_program(["Alice", "Ward-1", "Infection", "85", "82", "80"])
    assert "Stable" in output

def test_under_observation():
    output = run_program(["Bob", "Ward-2", "Diabetes", "70", "68", "66"])
    assert "Under Observation" in output

def test_needs_attention():
    output = run_program(["Emma", "Ward-3", "Asthma", "55", "52", "50"])
    assert "Needs Attention" in output

def test_high_risk():
    output = run_program(["Liam", "Emergency", "Cardiac", "45", "42", "40"])
    assert "High Risk" in output

def test_critical():
    output = run_program(["Noah", "ICU", "Trauma", "30", "35", "38"])
    assert "Critical" in output
