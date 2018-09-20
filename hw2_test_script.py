import hw2
from texts import *


print("Running Unit Tests on Ling 441 Homework 2")

testvals = [
    hw2.splice("dogfood", "fishfood"), 
    hw2.splice("cat", "bog"), 
    hw2.splice("diners", "winner"),
    hw2.scrunch("dog"),
    hw2.scrunch("at"), # 4
    hw2.scrunch("a"),
    hw2.scrunch(""),
    hw2.add_s("dog"),
    hw2.add_s("fish"),
    hw2.add_s("miss"), # 9
    hw2.add_s("church"),
    hw2.add_s("fizz"),
    hw2.is_plural("dogs"),
    hw2.is_plural("miss"),
    hw2.is_plural("campus"), #14
    hw2.is_plural("a"),
    hw2.is_plural("s"),
    hw2.make_np("word"),
    hw2.make_sentence("dogs", "chase", "cat"),
    hw2.make_sentence("cat", "scratch", "sofa"), #19
    hw2.vocab(hw2.mytext),
    hw2.A7,
    hw2.A8,
    hw2.acronym("International Business Machines"),
    hw2.acronym("Lord of the Rings"), #24
    hw2.acronym("One"),
    hw2.is_palindrome("wolf"),
    hw2.is_palindrome("bob"),
    hw2.is_palindrome("a"),
    len(hw2.A10),
    len(hw2.A11) #29
    ]

testlist = [
    (testvals[0] == "dogfood", "Question 1 Failed: Result should be \"dogfood\" \
but you had {}".format(testvals[0])),
    (testvals[1] == "cog", "Question 1 Failed: Result should be \"cog\" \
but you had {}".format(testvals[1])),
    (testvals[2] == "dinner", "Question 1 Failed: Result should be \"dinner\" \
but you had {}".format(testvals[2])),
    (testvals[3] == "dg", "Question 2 Failed: Result should be \"dg\" \
but you had {}".format(testvals[3])),
    (testvals[4] == "at", "Question 2 Failed: Result should be \"at\" \
but you had {}".format(testvals[4])),
    (testvals[5] == "a", "Question 2 Failed: Result should be \"a\" \
but you had {}".format(testvals[5])),
    (testvals[6] == "", "Question 2 Failed: Result should be an empty string \
but you had {}".format(testvals[6])),
    (testvals[7] == "dogs", "Question 3 Failed: Result should be \"dogs\" \
but you had {}".format(testvals[7])),
    (testvals[8] == "fishes", "Question 3 Failed: Result should be \"fishes\" \
but you had {}".format(testvals[8])),
    (testvals[9] == "misses", "Question 3 Failed: Result should be \"misses\" \
but you had {}".format(testvals[9])),
    (testvals[10] == "churches", "Question 3 Failed: Result should be \"churches\" \
but you had {}".format(testvals[10])),
    (testvals[11] == "fizzes", "Question 3 Failed: Result should be \"fizzes\" \
but you had {}".format(testvals[11])),
    (testvals[12] == True, "Question 4 Failed: Result should be True"),
    (testvals[13] == False, "Question 4 Failed: Result should be False"),
    (testvals[14] == False, "Question 4 Failed: Result should be False"),
    (testvals[15] == False, "Question 4 Failed: Result should be False"),
    (testvals[16] == False, "Question 4 Failed: Result should be False"),
    (testvals[17] == ["the", "word"], "Question 5 Failed: Result should be [\"the\", \"word\"] \
but you had {}".format(testvals[17])),
    (testvals[18] == ["the", "dogs", "chase", "the", "cat"], "Question 5 Failed: Result should \
be [\"the\", \"dogs\", \"chase\", \"the\", \"cat\"] but you had {}".format(testvals[18])),
    (testvals[19] == ["the", "cat", "scratches", "the", "sofa"], "Question 5 Failed: Result should \
be [\"the\", \"cat\", \"scratches\", \"the\", \"sofa\"] but you had {}".format(testvals[19])),
    (testvals[20] == set(["this", "is", "a", "test", "it", "only", "not", "pipe"]), "Question 6 Failed: \
a set containing (\"this\", \"is\", \"a\", \"test\", \"it\", \"only\", \"not\", \"pipe\") but you \
had {}".format(testvals[20])),
    (testvals[21] == ["only", "pipe", "test", "this"], "Question 7 Failed: Result should be \
[\"only\", \"pipe\", \"test\", \"this\"] but you had {}".format(testvals[21])),
    (testvals[22] == ["a", "test"], "Question 8 Failed: Result should be [\"a\", \"test\"] \
but you had {}".format(testvals[22])),
    (testvals[23] == "IBM", "Question 9 Failed: Result should be \"IBM\" \
but you had {}".format(testvals[23])),
    (testvals[24] == "LotR", "Question 9 Failed: Result should be \"LotR\" \
but you had {}".format(testvals[24])),
    (testvals[25] == "O", "Question 9 Failed: Result should be \"O\" \
but you had {}".format(testvals[25])),
    (testvals[26] == False, "Question 10a Failed: Result should be False"),
    (testvals[27] == True, "Question 10a Failed: Result should be True"),
    (testvals[28] == True, "Question 10a Failed: Result should be True"),
    (testvals[29] == 53, "Question 11 Failed: Result should be a list of length 53 \
but you had a list of length {} (make sure results print in alphabetical order)".format(testvals[29])),
    (testvals[30] == 179, "Question 11 Failed: Result should be a list of length 179 \
but you had a list of length {} (make sure results print in alphabetical order)".format(testvals[30]))
    ]

total = len(testlist)
failurelist = []
for test in testlist:
    if test[0] == False:
        failurelist.append(test[1])
for failure in failurelist:
    print(failure)
print("End of Unit Tests. You passed {}/{} test cases".format(total - len(failurelist), total))