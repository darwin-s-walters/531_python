import LiftCycle
import datetime
import sys

def print_set_weights( set_weight_list ):
    for current_set_weight in set_weight_list:
        print current_set_weight


def print_531_cycle( lift_cycle ):

    print "\nLift: " + lift_cycle.lift_name
    print "\n\nTraining Max: " + str(lift_cycle.training_max)

    print "\nWarmup Sets ( 5 reps each)"
    print_set_weights(lift_cycle.warmup_sets)

    print "\nWeek 1 Sets (5 reps each)"
    print_set_weights(lift_cycle.week1_sets)

    print "\nWeek 2 Sets (3 reps each)"
    print_set_weights(lift_cycle.week2_sets)

    print "\nWeek 3 Sets (5 , 3 , 1)"
    print_set_weights(lift_cycle.week3_sets)
    print "\n"

def save_cycle_to_file( lift_cycle ):
   current_time = datetime.datetime.now()


   timestamp = str(current_time.month) + "_" + str(current_time.day) + "_" + str(current_time.year)
   file_name = lift_cycle.lift_name + "_" + timestamp

   orig_stdout = sys.stdout

   log_file = open( "saved_lift_cycles/" + file_name, 'w' )
   sys.stdout = log_file

   print_531_cycle( lift_cycle )
   sys.stdout = orig_stdout
   log_file.close()

training_max = raw_input("Please enter your training max: ")
lift_name = raw_input("Please enter lift name: ")

lift_cycle = LiftCycle.LiftCycle( lift_name, training_max )

print_531_cycle( lift_cycle )
save_cycle_to_file( lift_cycle )
