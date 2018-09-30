import hw4

print("Running Unit Tests on Ling 441 Homework 4")

a = ("a", ["AH0"])
attention = ("attention", ["AH0", "T", "EH1", "N", "SH", "AH0", "N"])
mention = ("mention", ["M", "EH1", "N", "SH", "AH0", "N"])
passion = ("passion", ["P", "AE1", "SH", "AH0", "N"])
pension = ("pension", ["P", "EH1", "N", "SH", "AH0", "N"])
firearm = ('firearm', ['F', 'AY1', 'ER0', 'AA2', 'R', 'M'])

testvals = [
    hw4.mean_lengths(["hi", "there", "apple"]), 
    hw4.mean_lengths([[2, 8], [5, 6, 7]]),
    hw4.A1,
    hw4.wordnet_translations("playa", "spa", "eng"),
    hw4.wordnet_translations("imposante", "spa", "eng"),
    hw4.wordnet_eng_translation("playa", "spa"),
    hw4.wordnet_eng_translation("imposante", "spa"),
    hw4.swadesh_table["yo"],
    hw4.swadesh_table["pasto"],
    hw4.swadesh_table["ese"],
    hw4.is_spa_stopword("el"),
    hw4.is_spa_stopword("perro"),
    hw4.spa_word_to_eng("perro"),
    hw4.spa_word_to_eng("de"),
    hw4.spa_word_to_eng("estatal"),
    hw4.spa_word_to_eng("imposante"),
    hw4.spa_to_eng("el perro de mi madre es grande y rojo y imposante"),
    hw4.rhyming_suffix(attention),
    hw4.rhyming_suffix(a),
    hw4.rhyming_suffix(firearm),
    hw4.rhymes_with(attention, [a, attention, mention, passion, pension]),
    hw4.rhymes_with(a, [a, attention, mention, passion, pension]),
    hw4.nsyllables(a),
    hw4.nsyllables(attention),
    hw4.nsyllables(("nn", ["N", "N"])),
    hw4.nsyllables(firearm),
    hw4.stress_pattern(a),
    hw4.stress_pattern(attention),
    hw4.stress_pattern(firearm)
    ]

testlist = [
    (testvals[0] == 4.0, "Question 1a Failed: Result should be 4.0, but you had {}".format(testvals[0])),
    (testvals[1] == 2.5, "Question 1a Failed: Result should be 2.5, but you had {}".format(testvals[1])),
    (abs(testvals[2] - 26.603062342722623) < 0.00001, "Question 1b Failed: Result should be about \
26.60306, but you had {}".format(testvals[2])),
    (testvals[3] == set(['coast', 'beach', 'seacoast', 'seashore', 'plage', 'sea-coast']), "Question 2a \
Failed: Result should be a set containing ('coast', 'beach', 'seacoast', 'seashore', 'plage', 'sea-coast'), \
but you had {}".format(testvals[3])),
    (testvals[4] == set(), "Question 2a Failed: Result should be an empty set, \
but you had {}".format(testvals[4])),
    (testvals[5] == "coast", "Question 2b Failed: Result should be 'coast', but you had {}".format(testvals[5])),
    (testvals[6] == None, "Question 2b Failed: Result should be None, but you had {}".format(testvals[6])),
    (testvals[7] == "I", "Question 3a Failed: Result should be 'I', but you had {}".format(testvals[7])),
    (testvals[8] == "grass", "Question 3a Failed: Result should be 'grass', but you had {}".format(testvals[8])),
    (testvals[9] == "that", "Question 3a Failed: Result should be 'that', but you had {}".format(testvals[9])),
    (testvals[10] == True, "Question 3b Failed: Result should be True, but you had {}".format(testvals[10])),
    (testvals[11] == False, "Question 3b Failed: Result should be False, but you had {}".format(testvals[11])),
    (testvals[12] == "dog", "Question 4a Failed: Result should be 'dog', but you had {}".format(testvals[12])),
    (testvals[13] == "[de]", "Question 4a Failed: Result should be '[de]', but you had {}".format(testvals[13])),
    (testvals[14] == "state-supported", "Question 4a Failed: Result should be 'state-supported', \
but you had {}".format(testvals[14])),
    (testvals[15] == "?imposante?", "Question 4a Failed: Result shoul be '?imposante', \
but you had {}".format(testvals[15])),
    (testvals[16] == "[el] dog [de] [mi] mother [es] big and red and ?imposante?", "Question 4b Failed: \
Result should be '[el] dog [de] [mi] mother [es] big and red and ?imposante?', but you had {}".format(testvals[16])),
    (testvals[17] == attention[1][-5:], "Question 5a Failed: Result should be ['EH1', 'N', 'SH', 'AH0', 'N'], \
but you had {}".format(testvals[17])),
    (testvals[18] == None, "Question 5a Failed: Result should be None, but you had {}".format(testvals[18])),
    (testvals[19] == firearm[1][-3:], "Question 5a Failed: Result should be ['AA2', 'R', 'M'], \
but you had {}".format(testvals[19])),
    (testvals[20] == [mention, pension], "Question 5b Failed: Result should be {}, \
but you had {}".format([mention, pension], testvals[20])),
    (testvals[21] == [], "Question 5b Failed: Result should be an empty list, but you had {}".format(testvals[21])),
    (testvals[22] == 1, "Question 5c Failed: Result should be 1, but you had {}".format(testvals[22])),
    (testvals[23] == 3, "Question 5c Failed: Result should be 3, but you had {}".format(testvals[23])),
    (testvals[24] == 0, "Question 5c Failed: Result should be 0, but you had {}".format(testvals[24])),
    (testvals[25] == 3, "Question 5c Failed: Result should be 3, but you had {}".format(testvals[25])),
    (testvals[26] == [False], "Question 5d Failed: Result should be [False], but you had {}".format(testvals[26])),
    (testvals[27] == [False, True, False], "Question 5d Failed: Result should be [False, True, False], \
but you had {}".format(testvals[27])),
    (testvals[28] == [True, False, True], "Question 5d Failed: Result should be [True, False, True], \
but you had {}".format(testvals[28]))
    ]

total = len(testlist)
failurelist = []
for test in testlist:
    if test[0] == False:
        failurelist.append(test[1])
for failure in failurelist:
    print(failure)
print("End of Unit Tests. You passed {}/{} test cases".format(total - len(failurelist), total))