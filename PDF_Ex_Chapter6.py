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

#Ex 6.5
def add_vectors(vec1, vec2):
    return [sum(x) for x in zip(vec1, vec2)]

def multiple_vectors(vec1, vec2):
    return [a*b for a,b in zip(vec1, vec2)]

def vec_to_dict(vec):
    d = {}
    index = 0

    for value in vec:
        if (value != 0):
            d[index] = value
        index += 1
    
    return d

def add_sparse_vectors(vec1, vec2):
    d1 = vec_to_dict(vec1)
    d2 = vec_to_dict(vec2)

    for key2 in d2:
        if key2 not in d1.keys():
            d1[key2] = d2[key2]
        else:
            d1[key2] += d2[key2]
      
    return dict(sorted(d1.items()))

def multiple_sparse_vectors(vec1, vec2):
    d1 = vec_to_dict(vec1)
    d2 = vec_to_dict(vec2)

    for key2 in d2.copy():
        if key2 in d1.keys():
            d2[key2] *= d1[key2]
        else:
            del d2[key2]
      
    return dict(sorted(d2.items()))

def add_sparse_dense_vectors(denseVec, sparseVec):
    dSparse = dict(vec_to_dict(sparseVec))

    for key in dSparse:
        denseVec[key] += dSparse[key]

    return denseVec

def multiple_sparse_dense_vectors(denseVec, sparseVec):
    dSparse = dict(vec_to_dict(sparseVec))
    index = 0
    for index in range(len(denseVec)):
        if index not in dSparse.keys():
            denseVec[index] = 0
        else:
            denseVec[index] *= dSparse[index]

    return denseVec

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
    vec1 = [1, 2, 3]
    vec2 = [4, 5, 6]
    print(add_vectors(vec1, vec2)) # answer: [5, 7, 9]
    print(multiple_vectors(vec1, vec2)) # answer: [4, 10, 18]
    sparseVec1 = [0, 1, 6, 0, 5, 3]
    sparseVec2 = [1, 0, 4, 0, 8, 0]
    print(add_sparse_vectors(sparseVec1, sparseVec2)) #answers: {0: 1, 1: 1, 2: 10, 4: 13, 5: 3}
    print(multiple_sparse_vectors(sparseVec1, sparseVec2)) #answer: {2: 24, 4: 40}
    newDenseVec = [1, 2, 3, 4, 5, 6]
    print(add_sparse_dense_vectors(newDenseVec, sparseVec1)) # answer: [1, 3, 9, 4, 10, 9]
    anotherDenseVec = [1, 2, 3, 4, 5, 6]
    print(multiple_sparse_dense_vectors(anotherDenseVec, sparseVec1)) # answer: [0, 2, 18, 0, 25, 18]
    print(reverse_look_up(marbles, 31)) #answer: brown