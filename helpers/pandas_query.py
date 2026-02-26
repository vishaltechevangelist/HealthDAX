def aggregate_activity(df2):
    activity = (
        df2.groupby("patient_number")["physical_activity_steps_per_day"]
        .mean()
        .reset_index()
        .rename(columns={"physical_activity_steps_per_day": "avg_steps"})
    )
    return activity


def execute_structured_query(datasets, query):
    df = datasets[query["datasets"][0]]

    # Join if needed
    if query.get("join"):
        right_df = datasets[query["join"]["right"]]
        df = df.merge(right_df, on=query["join"]["on"])

    # Filters
    for f in query.get("filters", []):
        col, op, val = f["column"], f["operator"], f["value"]
        if op == "==":
            df = df[df[col] == val]
        elif op == ">":
            df = df[df[col] > val]
        elif op == "<":
            df = df[df[col] < val]

    # Aggregation
    result = getattr(
        df.groupby(query["groupby"])[query["metric_column"]],
        query["aggregation"]
    )()

    return result