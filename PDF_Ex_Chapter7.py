import collections
import random

#Ex 7.1
def open_file(filename):
    file = open(filename, "r")
    for line in file:
        print(line)
    file.close()

#Ex 7.4
def data_generation(n, a, b, filename):
    file = open(filename, "w")
    randNumbers = []
    for index in range(n):
        randNumbers.append(random.randint(a,b))
    
    file.write(str(randNumbers)[1:-1])
    file.close()

def read_data(filename):
    file = open(filename, "r")
    return (file.read())

def sum_problem(fileA, fileB, k):
    A_list = [int(i) for i in list(read_data(fileA).split(","))]
    B_list = [int(i) for i in list(read_data(fileB).split(","))]
    d = {}
    for u in A_list:
        for v in B_list:
            if ( u + v == k):
                d[u] = v
    
    print ("elements from A file :" , str(list((d.keys()))))
    print ("elements from B file : " , str(list(d.values())))

if __name__== "__main__":
    open_file("Test.txt")

    #7.2
    file = open("Shakespeare.txt", "r")
    count = collections.Counter()
    for word in file.read().split():
        count[word.lower()] +=1
    print("The most 20 common words are: " + str(list(dict(count.most_common(20)).keys())))
    print("The unique words are: " + str(list(dict(count).keys())))
    words_above_5_times = [w for w in count.keys() if count[w] >=5]
    print("Words that used at least 5 times: " + str(list(words_above_5_times)))

    fileToWrite = open("most_200_Common_words", "w")
    fileToWrite.write(str(count.most_common(200)))
    fileToWrite.close()

    data_generation(10, 1, 99, "FirstFile.txt")
    data_generation(10, 1, 99, "SecondFile.txt")
    print(read_data("Karin.txt"))
    sum_problem("FirstFile.txt", "SecondFile.txt", 85)

    data_generation(2000, 1, 10000, "Test1.txt")
    data_generation(2000, 1, 10000, "Test2.txt")
   # sum_problem("Test1.txt", "Test2.txt", 5000)
    '''answer:
    elements from A file : [2850, 2346, 1012, 3769, 3141, 1616, 2590, 2717, 3922, 4732, 2162, 2516, 3519, 2915, 1057, 1239, 2970, 2369, 297, 346, 2378, 4992, 1689, 3573, 4386, 1506, 4875, 1715, 1787, 1979, 1953, 1709, 1212, 2167, 855, 2507, 1522, 3377, 4240, 4748, 2695, 4717, 1430, 578, 1180, 2753, 1109, 2545, 3517, 1967, 632, 886, 910, 4600, 3145, 3104, 2124, 3795, 3008, 1261, 1270, 3154, 3598, 3449, 2380, 3931, 838, 3523, 706, 4025, 274, 3966, 2145, 3400, 621, 1677, 1526, 2741, 2230, 2524, 1821, 3617, 2131, 4788, 217, 1172, 2146, 3388, 1478, 2355, 3246, 630, 1644, 3816, 1153, 1503, 66, 249, 4269, 1163, 4051, 2933, 4569, 3080, 2020, 1055, 3551, 1863, 4738, 3221, 766, 3911, 4030, 3387, 1896, 3692, 3209, 4858, 446, 1258, 69, 2263, 2945, 1745, 669, 1256, 3883, 3091, 224, 3768, 3248, 1452, 1815, 1844, 2691, 3463, 876, 1061, 2992, 4610, 3533, 622, 1673, 4693, 4735, 2780, 2687, 4108, 4041, 393, 631, 1736, 247, 1188]
    elements from B file :  [2150, 2654, 3988, 1231, 1859, 3384, 2410, 2283, 1078, 268, 2838, 2484, 1481, 2085, 3943, 3761, 2030, 2631, 4703, 4654, 2622, 8, 3311, 1427, 614, 3494, 125, 3285, 3213, 3021, 3047, 3291, 3788, 2833, 4145, 2493, 3478, 1623, 760, 252, 2305, 283, 3570, 4422, 3820, 2247, 3891, 2455, 1483, 3033, 4368, 4114, 4090, 400, 1855, 1896, 2876, 1205, 1992, 3739, 3730, 1846, 1402, 1551, 2620, 1069, 4162, 1477, 4294, 975, 4726, 1034, 2855, 1600, 4379, 3323, 3474, 2259, 2770, 2476, 3179, 1383, 2869,
    212, 4783, 3828, 2854, 1612, 3522, 2645, 1754, 4370, 3356, 1184, 3847, 3497, 4934, 4751, 731, 3837, 949, 2067, 431, 1920, 2980,
    3945, 1449, 3137, 262, 1779, 4234, 1089, 970, 1613, 3104, 1308, 1791, 142, 4554, 3742, 4931, 2737, 2055, 3255, 4331, 3744, 1117, 1909, 4776, 1232, 1752, 3548, 3185, 3156, 2309, 1537, 4124, 3939, 2008, 390, 1467, 4378, 3327, 307, 265, 2220, 2313, 892, 959,
    4607, 4369, 3264, 4753, 3812]
    '''
    sum_problem("Test1.txt", "Test2.txt", 12000)
    

