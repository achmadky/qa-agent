import sys
import os

from extract_endpoints import extract
from generate_testcases import generate_tests
from generate_playwright_tests import generate_playwright


def run_all(doc):

    print("Step 1: Extracting endpoints...")
    extract(doc)

    print("Step 2: Generating testcases...")
    generate_tests()

    print("Step 3: Generating Playwright tests...")
    generate_playwright()

    print("Step 4: Running tests...")
    os.system("npx playwright test")


if __name__ == "__main__":

    command = sys.argv[1]

    if command == "run":
        run_all(sys.argv[2])

    elif command == "extract":
        extract(sys.argv[2])

    elif command == "generate-tests":
        generate_tests()

    elif command == "generate-playwright":
        generate_playwright()

    elif command == "run-tests":
        os.system("npx playwright test")