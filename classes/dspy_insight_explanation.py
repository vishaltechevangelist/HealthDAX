import dspy

class HealthInsightStruct(dspy.Signature):
    """
    Generate grounded health insights strictly from structured statistics.
    Do not introduce external medical knowledge.
    """
    structured_stats = dspy.InputField(desc="")
    #instruction = dspy.InputField("JSON  containing the instruction to llm regarding role, goal and style rules to display text")
    explaination = dspy.OutputField(desc="A detailed, layman-friendly grounded explanation ") 


class InsightExplaination(dspy.Module):
    def __init__(self):
        super().__init__()
        self.generate = dspy.Predict(HealthInsightStruct)

    def forward(self, structured_stats):
        return self.generate(structured_stats=structured_stats)