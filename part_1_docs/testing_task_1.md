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
    if card.value = 1:
      return True
    else
      return False
      # check_for_ace errors - should be two equals rather than one, no colon after else.

   

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
    # highest_card errors - dif instead of def, no comma between card 1 and card 2, returns card instead of card 1 if true.
  


def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
    # cards_total errors - total is not assigned to anything, return is left inside loop, so it will only run once, the return tries to add a strong to a int, which cannot be done without interpolating the total int within the string.
  
```
