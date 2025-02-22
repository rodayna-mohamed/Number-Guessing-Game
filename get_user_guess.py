def get_user_guess():      
   while True:
    try:
      guess=inp(input("enter your guess(1-100):"))
      if guess>=1 or guess<=100:
        return guess 
      else :
          print("please enter a number between 1 and 100")
    except ValueError:
        print("invalid input! please enter a number ")      
        