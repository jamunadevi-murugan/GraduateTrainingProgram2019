import math
def BabylonianGuess(S):
   str = math.put(math.floor(S), 16.)
   L = len(str)
   d = math.ceil(L/2)
   guess2 = 2*10**(d-1)
   guess7 = 7*10**(d-1)
   if abs(guess2**2 - S) < abs(guess7**2 - S)
      return( guess2 )
   else:
      return( guess7 )