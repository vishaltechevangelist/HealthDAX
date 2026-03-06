import random
import json

schema = {
    "Blood_Pressure_Abnormality": {"type":"categorical","values": {"Normal":0, "Abnormal":1}},
    "Level_of_Hemoglobin": {"type":"numeric"},
    "Age": {"type":"numeric"},
    "BMI": {"type":"numeric"},
    "Sex": {"type": "categorical", "values": {"male":0,"female":1}},
    "Pregnancy": {"type": "categorical", "values": {"No":0,"Yes": 1}},
    "Smoking": {"type":"categorical", "values": {"No":0, "Yes":1}},
    "Level_of_Stress": {"type":"categorical", "values": {"Low":1, "Normal":2,"High":3}},
    "Chronic_kidney_disease": {"type":"categorical", "values": {"No":0, "Yes":1}},
    "Adrenal_and_thyroid_disorders": {"type": "categorical", "values": {"No":0,"Yes": 1}},
}

NUM_QUERIES = 200


def build_conditions():

    conditions = []

    for column, meta in schema.items():

        if meta["type"] == "categorical":

            for label in meta["values"].keys():

                label_clean = label.lower()

                if column == "Sex":
                    conditions.append(f"{label_clean} patients")

                elif column == "Pregnancy":
                    if label_clean == "yes":
                        conditions.append("pregnant patients")

                else:
                    conditions.append(f"patients with {label_clean} {column.replace('_',' ').lower()}")

    return conditions


def build_numeric_columns():

    numeric_cols = []

    for column, meta in schema.items():
        if meta["type"] == "numeric":
            numeric_cols.append(column.replace("_"," "))

    return numeric_cols


def generate_queries():

    conditions = build_conditions()
    numeric_cols = build_numeric_columns()

    queries = []

    templates = [
        "count patients",
        "count {condition}",
        "count patients with {condition}",
        "average {numeric}",
        "mean {numeric}",
        "mean {numeric} for {condition}",
        "average {numeric} for {condition}",
    ]

    for _ in range(NUM_QUERIES):

        template = random.choice(templates)

        query = template.format(
            condition=random.choice(conditions),
            numeric=random.choice(numeric_cols)
        )

        queries.append({"query": query})

    return queries


if __name__ == "__main__":

    queries = generate_queries()

    with open("evaluation_queries.json", "w") as f:
        json.dump(queries, f, indent=2)

    print(f"Generated {len(queries)} queries")