#First Task : Compare Two Dices
from itertools import product , combinations

def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    for tup in product(dice1 , dice2):
      if tup[0] > tup[1]:
        dice1_wins +=1
      elif tup[1] > tup[0]:
        dice2_wins +=1

    return (dice1_wins, dice2_wins)
  
  #Second Task : Is there the best dice?
  
  def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
  
    for i in range(len(dices)):
      res = []
      for j in range(len(dices)):
        if i == j : continue
        dice_i_score , dice_j_score = count_wins(dices[i] , dices[j])
        if dice_i_score > dice_j_score :
          res.append(1)
      if res.count(1) == len(dices) - 1 : return i
    return -1
  
  #Third Task : Implement a Strategy
  
  def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    if find_the_best_dice(dices) != -1 :
      strategy = {"choose_first" : True , "first_dice" : find_the_best_dice(dices)}
    else :
      strategy = dict()
      for i in range(len(dices)):
         for j in range(len(dices)):
           if i == j : continue
           dice_i_score , dice_j_score = count_wins(dices[i] , dices[j])
           if dice_i_score > dice_j_score :
             strategy[j] = i 
           elif dice_i_score < dice_j_score :
             strategy[i] = j
      
      strategy["choose_first"] = False
    return strategy 
