def bomberMan(n, grid):
  # check initial state and return the grid as it is since it will look the same
  if n == 1:
    return grid
  # when the time elapsed is even all cells will be filled with bombs so we create a matrix that with o representing the bombs
  if n%2 == 0:
    return ['o'*c for i in range(r)]
  # checking for alternate states
  n //= 2
  # remove even states
  for q in range((n+1) % 2 + 1):
    newgrid =[['o']*c for i in range(r)]
    # detonation function
    def set(x, y):
      if 0 <= x < r and 0 <= y < c:
        newgrid[x][y] = '.'
    
    xi = [0,0,0,1,-1]
    yi = [0,-1,1,0,0]

    for x in range(r):
      for y in range(c):
        # check if bomb exists
        if grid[x][y] == 'o':
          # call function to detonate bomb
          for i,j in zip(xi, yi):
            set(x+1, y+j)
    grid = newgrid
  return["".join(x) for x in grid]


