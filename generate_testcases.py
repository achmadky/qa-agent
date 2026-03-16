import os
import json


INPUT_DIR = "data/endpoints"
OUTPUT_DIR = "data/testcases"


def generate_tests():

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for file in os.listdir(INPUT_DIR):

        path = os.path.join(INPUT_DIR, file)

        with open(path) as f:
            endpoint = json.load(f)

        tests = []

        # happy path
        tests.append({
            "name": "happy_path",
            "request": {},
            "expected_status": 200
        })

        # generic negative tests
        tests.append({
            "name": "sql_injection",
            "request": {"input": "' OR 1=1 --"},
            "expected_status": 400
        })

        tests.append({
            "name": "script_injection",
            "request": {"input": "<script>alert(1)</script>"},
            "expected_status": 400
        })

        data = {
            "endpoint": endpoint["endpoint"],
            "method": endpoint["method"],
            "tests": tests
        }

        out_file = file.replace(".json", "_tests.json")

        with open(os.path.join(OUTPUT_DIR, out_file), "w") as f:
            json.dump(data, f, indent=2)

    print("Testcases generated")