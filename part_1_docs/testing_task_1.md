### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    ## = should be ==
    if card.value = 1:
      return True
    ##else line missing :
    else
      return False
   

  dif highest_card(self, card1 card2):
  ## dif should be def
  ## , missing between card1 and card 2 in paramaters
  ## no indent on lines following function definition
  if card1.value > card2.value:
  # line should read 'return card1'
    return card
  else:
    return card2
  

## function is not indented in line with other class functions
def cards_total(self, cards):
  ## the total variable hasn't been set to anything
  total
  for card in cards:
    total += card.value
    ## To return this as a string total needs to be converted to string i.e str(total)
    ## white space missing after 'of'
    return "You have a total of" + total
    ## return is indented within for loop so will exit the function after only one cycle
  
```
