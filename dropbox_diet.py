
'''
Solution to the Dropbox diet challenge @ 

https://www.dropbox.com/jobs/challenges#the-dropbox-diet

by Jimmy John

Sample Output:

Jimmy-Johns-MacBook-Pro:dropbox_challenges jjohn$ python dropbox_diet.py 
2
red-bull 140
coke 110

no solution <= OUTPUT

Jimmy-Johns-MacBook-Pro:dropbox_challenges jjohn$ python dropbox_diet.py 
12
free-lunch 802
mixed-nuts 421
orange-juice 143
heavy-ddr-session -302
cheese-snacks 137
cookies 316
mexican-coke 150
dropballers-basketball -611
coding-six-hours -466
riding-scooter -42
rock-band -195
playing-drums -295

coding-six-hours <= OUTPUT
cookies <= OUTPUT
mexican-coke <= OUTPUT
Jimmy-Johns-MacBook-Pro:dropbox_challenges jjohn$ 

'''

def combinations(items, start, eligible_combinations, length, combined_activities, combined_sum):
    '''
    Finds out all the different combinations of the activities chosen 1 at a 
    time, 2 at a time, 3 at a time etc and returns those whose sum is zero.

    combined_activities = one possibility of a activity formation
    combined_sum = the caloric_impact of the above
    '''

    if start >= len(items):
        return eligible_combinations

    for i in range(start, length):
        #check if it's sum is zero
        if not (combined_sum + int(items[i][1])):
            eligible_combinations.append(combined_activities + ' %s' % items[i][0])

        eligible_combinations = combinations(items, i + 1, eligible_combinations, length, combined_activities + ' %s' % items[i][0], combined_sum + int(items[i][1]))

    return eligible_combinations


def parse_input():
    '''
    parse the input and return it in a list
    '''

    data = []
    num_of_list_items = int(raw_input())
    for item in range(num_of_list_items):
        line = raw_input()
        activity, caloric_impact = line.split(' ')
        data.append((activity, caloric_impact))

    return data


if __name__ == '__main__':

    #get the input data
    input_data = parse_input()

    #get all the zero caloric impact combos
    eligible_combinations = combinations(input_data, 0, [], len(input_data), '', 0)

    #print them out
    if eligible_combinations:
        for activities in eligible_combinations:
            zero_caloric_impact = activities.strip().split(' ')
            zero_caloric_impact.sort()
            for activity in zero_caloric_impact:
                print activity
            #we need to print only one of them
            break
    else:
        print 'no solution'


