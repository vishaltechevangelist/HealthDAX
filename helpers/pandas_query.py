def execute_structured_query(datasets, query):

    # Step 1 — Select base dataset
    df = datasets[query["datasets"][0]]

    # Step 2 — Join if required
    if query["join"]:
        right_df = datasets[query["join"]["right"]]
        df = df.merge(
            right_df,
            on=query["join"]["on"]
        )


    # Step 3 — Apply filters
    for f in query["filters"]:
        col, op, val = f["column"], f["operator"], f["value"]
        if op == "==":
            df = df[df[col] == val]
        elif op == ">":
            df = df[df[col] > val]

    # Step 4 — Aggregate
    result = getattr(
        df.groupby(query["groupby"])[query["metric_column"]],
        query["aggregation"]
    )()

    return result