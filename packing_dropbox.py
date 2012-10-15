
'''
Solution to the 'Packing your Dropbox' challenge @ 

https://www.dropbox.com/jobs/challenges#packing-your-dropbox

by Jimmy John

Sample Output:

Jimmy-Johns-MacBook-Pro:dropbox_challenges jjohn$ python ~/dropbox_challenges/packing_dropbox.py 
3
8 8
4 3
3 4
88 <= OUTPUT
Jimmy-Johns-MacBook-Pro:dropbox_challenges jjohn$ 


'''

def can_fit(w1, h1, w2, h2):
    '''
    Helper to tell you if (w1,h1) can fit in a box of dimensions (w2,h2)
    '''
    if w1 <= w2 and h2 <= h2:
        return True
    else:
        return False

def determine_min_dimensions(w1, h1, w2, h2, unused_reservoir=[]):
    '''
    Gives you the min width/height of a box to accomodate both (w1,h1) and 
    (w2,h2).

    Also returns the unused_reservoir which is a essentially any 'holes' created

    '''

    #100% compaction for all these...
    #square
    if w1 == w2 and h1 == h2:
        return (w1, 2*h1, unused_reservoir)
    #width is the same
    elif w1 == w2:
        return (w1, h1 + h2, unused_reservoir)
    #height is the same
    elif h1 == h2:
        return (w1 + w2, h1, unused_reservoir)
    #rotate 90 degrees and check w1/h2
    elif w1 == h2:
        w2, h2 = h2, w2
        return (w1, h1 + h2, unused_reservoir)
    #rotate 90 degrees and check h1/w2
    elif h1 == w2:
        w2, h2 = h2, w2
        return (w1 + w2, h1, unused_reservoir)

    #different dimensions - * no * 100% compaction
    else:
        #if we are here means we will have to deal with some 'holes' in the resultant box
        #i.e. it does not have 100% compaction

        #using the larger base
        area_using_larger_base = max(w1,w2)*(h1+h2)
        #using larger height
        area_using_larger_height = max(h1,h2)*(w1+w2)

        if area_using_larger_base <= area_using_larger_height:
            unused_area = max(w1,w2) * (h1 + h2) - w1*h1 - w2*h2

            #we append a tuple containing some details of the hole: 
            #area / width / height / a list (to be populated by 'occupants' of this hole)
            unused_reservoir.append(
                                    (unused_area, 
                                     abs(w2-w1), 
                                     unused_area/abs(w2-w1), 
                                     [])
                                    )
            return (max(w1,w2), h1 + h2, unused_reservoir)
        elif area_using_larger_height <= area_using_larger_base:
            unused_area = max(h1,h2)*(w1+w2) - w1*h1 - w2*h2

            #we append a tuple containing some details of the hole: 
            #area / width / height / a list (to be populated by 'occupants' of this hole)
            unused_reservoir.append(
                                    (unused_area, 
                                     unused_area/abs(h2-h1), 
                                     abs(h2-h1), 
                                     [])
                                    )

            return (max(h1,h2),(w1+w2), unused_reservoir)

def parse_input():
    '''
    parse the input and return it in a list
    '''

    data = []
    num_of_list_items = int(raw_input())

    for i in range(num_of_list_items):
        line = raw_input()
        width, height = line.split(' ')
        data.append((int(width), int(height)))

    return data


if __name__ == '__main__':

    #get the input data
    input_data = parse_input()

    if len(input_data) == 1:
        print input_data[0][0] * input_data[0][1]
    else:
        unused_reservoir = []

        min_width = input_data[0][0]
        min_height = input_data[0][1]

        for i in range(1,len(input_data)):

            #first check if there are any 'openings' in the existing 'holes'
            found = False
            if unused_reservoir:
                for usable in unused_reservoir:

                    #can we fit this or it's rotated clone?
                    if can_fit(input_data[i][0],input_data[i][1],usable[1],usable[2]) or \
                       can_fit(input_data[i][1],input_data[i][0],usable[1],usable[2]):
                        if not usable[3]:

                            #first time this hole is being used by someone
                            usable[3].append((input_data[i][0], input_data[i][1]))
                            found = True
                            break
                        else:
                            #this hole has some 'previous' occuopants. Check and see if the addition of this new entry
                            #causes the new min width/height > area of hole.
                            #If it does, we have to accomodate this new entry elsewhere
                            min_width_hole_fillers = input_data[i][0]
                            min_height_hole_fillers = input_data[i][1]
                            for hole_fillers in usable[3]:
                                min_width_hole_fillers, min_height_hole_fillers, _ignore = determine_min_dimensions(min_width_hole_fillers, min_height_hole_fillers, hole_fillers[0], hole_fillers[1])
                            
                            if can_fit(min_width_hole_fillers, min_height_hole_fillers, usable[1],usable[2]) or \
                               can_fit(min_height_hole_fillers, min_width_hole_fillers, usable[1],usable[2]):
                                found = True
                                usable[3].append((input_data[i][0], input_data[i][1]))

            if found:
                #this entry has found a 'home' in a 'hole'
                continue

            min_width, min_height, unused_reservoir  = determine_min_dimensions(min_width, 
                                                         min_height,
                                                         input_data[i][0],
                                                         input_data[i][1],
                                                         unused_reservoir)


        print min_width * min_height

