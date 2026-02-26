def process_data(input_data):
    values = input_data.values

    # pretend this is validation + fitting + plotting
    mean_value = sum(values) / len(values)

    return {"original": values, "mean": mean_value}
