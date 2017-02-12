class LiftCycle:


    lift_name

    training_max

    warmup_sets[]
    week1_sets[]
    week2_sets[]
    week3_sets[]

    warmup_percentages = [0.4, 0.5, 0.6]
    week1_percentages = [0.65, 0.75, 0.85]
    week2_percentages = [0.7, 0.8, 0.9]
    week3_percentages = [0.75, 0.85, 0.95]

    def __init__(self, lift_name, training_max):
        lift_name = lift_name
        traininng_max = training_max

        warmup_sets = calculate_set_weights(training_max, warmup_percentages)
        week1_sets = calculate_set_weights(training_max, week1_percentages)
        week2_sets = calculate_set_weights(training_max, week2_percentages)
        week3_sets = calculate_set_weights(training_max, week3_percentages)


    def calculate_set_weights( traiing_max, percentages_list):
