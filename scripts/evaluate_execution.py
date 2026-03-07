import json, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "scripts" / "evaluation_queries.json"

from app.services.query_service import query_service

with open(DATA_PATH) as f:
    test_cases = json.load(f)

correct = 0

for case in test_cases:
    response = query_service.process_natural_language(case['query'])
    print(response)
    result = list(response['data'].values())[0]

    if result == case["expected_result"]:
        correct += 1

accuracy = correct/len(test_cases)

print(f"Execution Accuracy : {accuracy}")