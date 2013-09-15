#universal settings
#1 for yes 0 for no

#making a list of settings that I would guess is how the intoxilyzer 8000 is set up. 

#TODO {put accompanying code in this file, or make another file with the functions

#clock and time settings
dst_adjust = 1
#timezone = 'm' 									#gmt +/- hours ? maybe just have US time zones
#use_gmt = 0 											#nevermind, use this for deciding between gmt or US times.

#test settings

data_input = 1
test_sequence = ['a','d','a','b','a','c','a','b','a']
prelim_result = 1
three_digit_result = 1
enable_breath_plot = 1 #plots breath reading over time

test_number = 0 #increments for every test done.
#