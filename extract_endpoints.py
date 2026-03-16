import os
import json
from document_loader import load_document


OUTPUT_DIR = "data/endpoints"


def simple_extract(text):

    endpoints = []

    lines = text.split("\n")

    for line in lines:

        if "GET /" in line or "POST /" in line or "PUT /" in line or "DELETE /" in line:

            parts = line.split()

            method = parts[0]
            path = parts[1]

            endpoints.append({
                "name": path.replace("/", "_"),
                "endpoint": path,
                "method": method,
                "request": {},
                "response": {}
            })

    return endpoints


def extract(doc):

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    text = load_document(doc)

    endpoints = simple_extract(text)

    for ep in endpoints:

        filename = ep["name"].replace("/", "") + ".json"

        with open(f"{OUTPUT_DIR}/{filename}", "w") as f:
            json.dump(ep, f, indent=2)

    print(f"Extracted {len(endpoints)} endpoints")