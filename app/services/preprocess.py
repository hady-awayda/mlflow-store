def preprocess_data(df):
    df = df.dropna()
    features = df[["BodyweightKg", "BestSquatKg", "BestBenchKg", "BestDeadliftKg"]]
    target = df["Place"]

    target = target.apply(lambda x: 1 if x == "1" else 0)

    return features, target