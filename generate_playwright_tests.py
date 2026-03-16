import os
import json


INPUT_DIR = "data/testcases"
OUTPUT_DIR = "tests/generated"


def generate_playwright():

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for file in os.listdir(INPUT_DIR):

        with open(os.path.join(INPUT_DIR, file)) as f:
            data = json.load(f)

        endpoint = data["endpoint"]
        method = data["method"]

        test_code = """
import { test, expect } from '@playwright/test';
"""

        for t in data["tests"]:

            name = t["name"]
            req = t["request"]
            status = t["expected_status"]

            test_code += f"""

test('{name}', async ({{ request }}) => {{

  const response = await request.{method.lower()}('{endpoint}', {{
    data: {req}
  }});

  expect(response.status()).toBe({status});

}});
"""

        output_file = file.replace(".json", ".spec.ts")

        with open(os.path.join(OUTPUT_DIR, output_file), "w") as f:
            f.write(test_code)

    print("Playwright tests generated")