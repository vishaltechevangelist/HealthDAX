import json, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from app.services.query_service import query_service

with open("/Users/vishalsaxena/Documents/DS_Workspace/healthdax/scripts/evaluation_queries.json") as f:
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