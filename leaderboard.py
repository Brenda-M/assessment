# scores in the leaderboard are sorted hence we can use a binary search tree
def climbing_leaderboard(ranked, player):

  # get rid of duplicates using set method and covert back to list
  ranked = list(set(ranked))
  
  ranked.sort()
  # find lenght of scores
  len_ranked=len(ranked)
  #variable to keep track of the rankings
  i = 0
  result = []

  for all_scores in player:
    while i < len_ranked and player[i] <= all_scores:
      i+=1
    
    result.append(len_ranked - i + 1)

  return result





