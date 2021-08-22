Testing HW Notes

check_for_ace_test_fail.png
- Test is failing because of the syntax error identified in testing_task_1, to correct this, line 11 of card_game.py was updated to ‘ if card.value == 1: ’

check_for_ace_test_fail_2.png
- Test is failing because of the syntax error identified in testing_task_1, to correct this, line 13 of card_game.py was updated to include a colon after the else

check_for_ace_test_pass.png
- With the syntax errors corrected in the two failed test runs, the test is now passing because the card.value is equal to 1 which results in a True result from the check_for_ace function

highest_card_test_fail_1.png
- Test is failing because the function is not defined, instead of def it is written as Dif so the function is invalid syntax. Line 17 of card_game.py was updated to def highest_card(self, card1 card2)

highest_card_test_fail_2.png
- Test is failing because there is no comma between the card1 and card2 paramater, which is causing a syntax error.  Line 17 of card_game.py was updated to def highest_card(self, card1, card2)

highest_card_test_fail_3.png
- Test is failing because under line 17 of card_game.py, the code is not indented. The whole code block was then indented.

highest_card_test_fail_4.png
- Test is failing because under line 19 of card_game.py, it is trying to return ‘card’ which is not an argument passed into this function. This was updated to ‘card1’

highest_card_test_pass.png
- Test is passing because of the two cards created for this test, the card returned by the highest_card_function is the card with the card.value of 7 which is higher than the card.value of the other card created which was 4

cards_total_test_fail_1.png
- Test is failing because the cards total function is not indented in line with the other functions in the CardGame class. The entire function was then indented in line with the other functions

cards_total_test_fail_2.png
- Test is failing because the ‘total’ variable on line 26 of card_game.py hasn’t been set to anything. This was updated to be total = 0 as a staring point

cards_total_test_fail_3.png
- Test is failing because the cards_total function is trying to return a concatenation of the string “You have a total of” and an integer value of ‘total’. Total must be parsed into string using str(), so line 29 of card_game.py was updated to return "You have a total of" + str(total)

cards_total_test_fail_4.png
- Test is failing because the for card in cards: loop in the cards_total function is returning within the for loop, so it will return after only one iteration of the loop. The return line was reverse indented back outside of the for loop so that it will only return after the full loop is completed

cards_total_test_fail_5.png
- Test is failing because line 32 of card_game_test.py requireds the string returned by the function to match - "You have a total of 21" however what is being returned is "You have a total of21”. A white space was then added after “of” on line 29 of card_game.py.

cards_total_test_pass.png
- Test is passing because the cards_total function loops through the cards array, containing card_1, card_2 & card_3 which were created as part of this test. They have values of 4, 7 and 10 respectively which totals 21. The cards_total function loops through each card in the cards array and adds the card.value to the total variable stored within the function. At the end of the loop the cards_total function returns the string “You have a total of 21”. Which is a perfect match with what the test was written to expect. 