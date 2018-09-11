import hw1
from texts import *

genesis = load_text3()
sense = load_text2()
moby = load_text1()

print("Running Unit Tests on Ling 441 Homework 1")

testlist = [(hw1.genesis_ntokens == 44764, "Question 1 Failed: There should be 44764 tokens in \
Genesis, but you had {}".format(hw1.genesis_ntokens)),
(hw1.genesis_ntypes == 2789, "Question 2 Failed: There should be 2789 types in Genesis \
but you had {}".format(hw1.genesis_ntypes)),
(hw1.genesis_nheavens == 3, "Question 3 Failed: The word \"heavens\" appears 3 times in Genesis \
but you had {}".format(hw1.genesis_nheavens)),
(hw1.genesis_more == False, "Question 4 Failed: Rsult is False, \"heavens\" appears \
3 times in Genesis and 17 times in Moby Dick"),
(hw1.ntokens == [44764, 260819], "Question 5 Failed: Genesis has 44764 tokens \
and Moby Dick has 260819 tokens, but you had {} and {}, respectively".format(hw1.ntokens[0],
    hw1.ntokens[1])),
(hw1.ppm(2, 500000) == 4, "Question 6 Failed: Result of ppm(2, 500000) should be 4, but you had \
{}".format(hw1.ppm(2, 500000))),
(hw1.ppm(2, 1000) == 2000, "Question 6 Failed: Result of ppm(2, 1000) should be 2000, but you had \
{}".format(hw1.ppm(2, 1000))),
(hw1.ppm(0, 1000) == 0, "Question 6 Failed: Result of ppm(0, 1000) should be 0, but you had \
{}".format(hw1.ppm(0, 1000))),
(hw1.ppm(1, 1) == 1000000, "Question 6 Failed: Result of ppm(1, 1) should be 1000000, but you had \
{}".format(hw1.ppm(1, 1))),
(hw1.heavens_ppm == [67.01813957644535, 65.17930058776392], "Question 7 Failed: Genesis heavens ppm \
should be 67.01813957644535 and Moby Dick heavens ppm should be 65.17930058776392, but you had \
{} and {}, respectively".format(hw1.heavens_ppm[0], hw1.heavens_ppm[1])),
(hw1.word_ppm('heavens', genesis) == 67.01813957644535 and \
    hw1.word_ppm('heavens', moby) == 65.17930058776392, "Question 8 Failed: Genesis heavens word ppm \
should be 67.01813957644535 and Moby Dick heavens word ppm should be 65.17930058776392, the same \
as in Question 7"),
(hw1.A9 == "by", "Question 9 Failed: The fourth token in Moby Dick is \"by\", but you had \
{}".format(hw1.A9)),
(hw1.A10 == ".", "Question 10 Failed: The final token of Moby Dick is \".\", but you had \
{}".format(hw1.A10)),
(hw1.A11 == "catfish", "Question 11 Failed: Result should be \"catfish\", but you had \
{}".format(hw1.A11)),
(hw1.A12 == True, "Question 12 Failed: \"diplodocus\" is longer than 7 characters"),
(hw1.A13 == True, "Question 13 Failed: \"fish\" is longer than \"cat\""),
(hw1.A14 == True, "Question 14 Failed: The first letter in \"dog\" is the same as the \
first letter in \"diplodocus\""),
(hw1.A15 == ['cat', 'fish'], "Question 15 Failed: Result should be ['cat', 'fish'], but you had \
{}".format(hw1.A15)),
(hw1.A16 == ['g', 's', 7], "Question 16 Failed: Result should be ['g', 's', 7], but you had \
{}".format(hw1.A16)),
(hw1.A17 == "tyre", "Question 17 Failed: Result should be \"tyre\", but you had \
\"{}\"".format(hw1.A17)),
(hw1.A18 == False, "Question 18 Failed: Result should be False, frequency is the same as the \
percentage function in the book"),
(hw1.A19 == ['this', 'is', 'a', 'test'], "Question 19 Failed: Result should be ['this', 'is', \
'a', 'test'], but you had {}".format(hw1.A19)),
(hw1.A20 == "frodo", "Question 20 Failed: Result should be \"frodo\", but you had {}".format(hw1.A20)),
(hw1.A21 == "said that he was one of six who had killed",
"Question 21 Failed: Result should be \"said that he was one of six who had killed\", \
but you had {}".format(hw1.A21)),
(hw1.A22 == True, "Question 22 Failed: Result should be true"),
(hw1.A23 == {'is', 'test'}, "Question 23 Failed: Result should be {{'is', 'test'}} \
(this is the set intersection), but you had {}".format(hw1.A23)),
(hw1.A24 == 2164, "Question 24 Failed: Result should be 2164 (this is the set difference), \
but you had {}".format(hw1.A24))]

total = len(testlist)

failurelist = []

for test in testlist:
    if test[0] == False:
        failurelist.append(test[1])
for failure in failurelist:
    print(failure)
print("End of Unit Tests. You passed {}/{} test cases".format(total - len(failurelist), total))