import hw3
from texts import *
from nltk import FreqDist

print("Running Unit Tests on Ling 441 Homework 3")

A4_correct = [(448, 'Wall Street Journal'), 
            (433, 'Moby Dick by Herman Melville 1851'), 
            (432, 'Inaugural Address Corpus'), 
            (425, 'The Man Who Was Thursday by G . K . Chesterton 1908'), 
            (391, 'Chat Corpus'), 
            (352, 'Personals Corpus'), 
            (339, 'Sense and Sensibility by Jane Austen 1811'), 
            (259, 'Monty Python and the Holy Grail'), 
            (177, 'The Book of Genesis')]

A6_correct = [(0.5820969337289812, 'Chat Corpus'), 
            (0.5667870036101083, 'Personals Corpus'), 
            (0.5323176361957526, 'Monty Python and the Holy Grail'), 
            (0.5208736299161831, 'Wall Street Journal'), 
            (0.500661084178052, 'The Man Who Was Thursday by G . K . Chesterton 1908'), 
            (0.46601439146865453, 'Moby Dick by Herman Melville 1851'), 
            (0.4284689852993905, 'The Book of Genesis'), 
            (0.4225958581094935, 'Inaugural Address Corpus'), 
            (0.39426313478706276, 'Sense and Sensibility by Jane Austen 1811')]

A7_correct = [(0.4305468680189438, 'The Book of Genesis'), 
            (0.4093829197854659, 'Monty Python and the Holy Grail'), 
            (0.38596768106494667, 'Inaugural Address Corpus'), 
            (0.37024861310869117, 'Personals Corpus'), 
            (0.3617672980509442, 'The Man Who Was Thursday by G . K . Chesterton 1908'), 
            (0.3566776854834153, 'Sense and Sensibility by Jane Austen 1811'), 
            (0.3540807993282698, 'Moby Dick by Herman Melville 1851'), 
            (0.32031467281179227, 'Wall Street Journal'), 
            (0.2715840924239058, 'Chat Corpus')]

A_list = [A4_correct, A6_correct, A7_correct]

testvals = [
    hw3.mobysorted(["whale", "the", "anvil"]),
    hw3.nvowels("tuesday"),
    hw3.nvowels("TUESDAY"),
    hw3.nvowels("ttytt"),
    hw3.nvowels("aeiou"),
    hw3.vsort(["test", "a", "iamb", "aeolian"]),
    hw3.vsort(["shawn", "testy", "beets"]),
    hw3.diversity(load_text1()),
    hw3.zipfslope(["a", "a", "a", "a", "a", "b", "b", "c"]),
    hw3.hapax_prop(['a', 'a', 'b', 'b', 'c', 'c', 'd']),
    hw3.cumulative(FreqDist(["a", "a", "a", "b", "b", "c", "d", "e"]), 2),
    hw3.coverage20(load_text1())
    ]

testlist = [
    (testvals[0] == ["the", "whale", "anvil"], "Qeustion 1 Failed: Result of mobysorted on the example should ['the', \
'whale', 'anvil'], but you had {}".format(testvals[0])),
    (testvals[1] == 3, "Question 2 Failed: Result of nvowels on 'tuesday' should be 3, but you had {}".format(testvals[1])),
    (testvals[2] == 3, "Question 2 Failed: Result of nvowels on 'TUESDAY' should be 3, but you had {}".format(testvals[2])),
    (testvals[3] == 0, "Question 2 Failed: Result of nvowels on 'ttytt' should be 0, but you had {}".format(testvals[3])),
    (testvals[4] == 5, "Question 2 Failed: Result of nvowels on 'aeiou' should be 5, but you had {}".format(testvals[4])),
    (testvals[5] == ['a', 'aeolian', 'iamb', 'test'], "Question 3 Failed: Result of vsort on the example should be \
['a', 'aeolian', 'iamb', 'test'], but you had {}".format(testvals[5])),
    (testvals[6] == ['beets', 'shawn', 'testy'], "Question 3 Failed: Result of vsort on ['shawn', 'testy', 'beets'] should be \
['beets', 'shawn', 'testy'], but you had {}".format(testvals[6])),
    (testvals[7] == 433, "Question 4 Failed: Result of diversity on Moby Dick should be 433, but you had {}".format(testvals[7])),
    (testvals[8] == 2.5, "Question 5 Failed: Result should be 2.5, but you had {}".format(testvals[8])),
    (testvals[9] == 0.25, "Question 6 Failed: Result of hapax_prop on the example should be 0.25, but you had {}".format(testvals[9])),
    (testvals[10] == 0.625, "Question 7 Failed: Result of cumulative on the example should be \
0.625, but you had {}".format(testvals[10])),
    (abs(testvals[11] - 0.3540807993282698) < 0.00001, "Question 7 Failed: Result of coverage20 \
on Moby Dick should be close to 0.3540808 but you had {}".format(testvals[11]))
    ]

hw_A = [hw3.A4, hw3.A6, hw3.A7]
A_strings = ["A4", "A6", "A7"]

# add three for checking the floats
total = len(testlist) + 3
failurelist = []
for test in testlist:
    if test[0] == False:
        failurelist.append(test[1])
for failure in failurelist:
    print(failure)
extras = 0
for i in range(len(A_list)):
    for j in range(len(A_list[i])):
        if abs(hw_A[i][j][0] - A_list[i][j][0]) > 0.00001:
            print("Question Failed, Incorrect Value for {}: Your value of\n{} should be similar to\n{}".format(A_strings[i], hw_A[i], A_list[i]))
            extras += 1
            break
print("End of Unit Tests. You passed {}/{} test cases".format(total - len(failurelist) - extras, total))
