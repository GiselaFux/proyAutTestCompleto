import subprocess

def run_pytest():
    subprocess.run(
        ["pytest", "tests/unit", "tests/integration", "tests/e2e", "-v"],
        check=True
    )

def run_behave():
    subprocess.run(
        ["behave", "behave/features", "-f", "json", "-o", "reports/behave.json", "-f", "pretty"],
        check=True
    )

if __name__ == "__main__":
    run_pytest()
    run_behave()