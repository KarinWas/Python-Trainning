import collections
#Ex 6.1
def print_dictionary(dict):
    for key, value in dict.items():
        print (key, value)

#Ex 6.2
def list_to_dictionary(lst):
    new_dict = {}
    cnt = collections.Counter()
    for value in lst:
        if new_dict.get(value) == None:
            new_dict[value] = 1
        else:
            new_dict[value] +=1
    #return new_dict

    #with counter:
    for value in lst:
        cnt[value] += 1
    return cnt

#Ex 6.6
def reverse_look_up(dict, searchValue):
    return (list(dict.keys())[list(dict.values()).index(searchValue)])

if __name__== "__main__":
    marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29 }
    print_dictionary(marbles)
    '''answer:
    red 34
    green 30
    brown 31
    yellow 29'''
    names = ['Karin', 'Eli', 'Dana', 'Karin', 'Karin', 'Dana', 'Eden']
    print(list_to_dictionary(names)) # answer : {'Karin': 3, 'Eli': 1, 'Dana': 2, 'Eden': 1}
    print(reverse_look_up(marbles, 31)) #answer: brown