class LiftCycle(object):


    lift_name = ""

    training_max = 0

    warmup_sets = []
    week1_sets = []
    week2_sets = []
    week3_sets = []

    warmup_percentages = [0.4, 0.5, 0.6]
    week1_percentages = [0.65, 0.75, 0.85]
    week2_percentages = [0.7, 0.8, 0.9]
    week3_percentages = [0.75, 0.85, 0.95]

    def __init__( self, lift_name, training_max):
        self.lift_name = lift_name
        self.training_max = float(training_max)

        self.warmup_sets = self.calculate_set_weights(self.training_max, LiftCycle.warmup_percentages)
        self.week1_sets = self.calculate_set_weights(self.training_max, LiftCycle.week1_percentages)
        self.week2_sets = self.calculate_set_weights(self.training_max, LiftCycle.week2_percentages)
        self.week3_sets = self.calculate_set_weights(self.training_max, LiftCycle.week3_percentages)

    def calculate_set_weights( self, training_max, percentages_list):
        set_weight_list = []
        for percentage_iterator in percentages_list:
               set_weight_list.append( training_max * percentage_iterator )

        return set_weight_list 
        
