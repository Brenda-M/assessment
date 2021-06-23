def get_records(s):
  # create variables to track highest score, lowest score, number she breaks records for most records, and number she breaks record for least points and intialize them to 0
  highest_score = 0
  lowest_score = 0
  highest_record = 0
  lowest_record = 0



  for i in range(len(s)):
    if i == 0:
      highest_score = lowest_score = s[i]
    elif s[i] > highest_score:
    # update the value of highest_score to the current value in the iteration and we update the number of times she has broken the record for the highest points
      highest_score = s[i]
      highest_record += 1
    # we check for the lowest scored and update it
    elif s[i] < lowest_score:
      lowest_score = s[i]
      lowest_record += 1

  return highest_record, lowest_record


