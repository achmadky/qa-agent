AI QA Agent

Lightweight AI-assisted API test generator.

Automatically:

extracts endpoints from docs

generates testcases

creates Playwright API tests

executes tests

Supports:

.md
.txt
.pdf
.docx
.html

Install

Install Python deps

pip install -r requirements.txt

Install Playwright

npm init -y
npm install -D @playwright/test

npx playwright install

Usage

Full pipeline

python qa_agent.py run techspec.md

Extract endpoints only

python qa_agent.py extract techspec.md

Generate testcases

python qa_agent.py generate-tests

Generate Playwright tests

python qa_agent.py generate-playwright

Run tests

python qa_agent.py run-tests

Folder Structure

data/endpoints
Extracted API contracts

data/testcases
Generated testcases

tests/generated
Generated Playwright tests

Example Workflow

python qa_agent.py run techspec.md

Result:

tests/generated/*.spec.ts# qa-agent
