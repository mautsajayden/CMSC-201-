"""
    File : lock_and_key.py
    Author : Jayden Mautsa 
    Date : 10/10/2025
    Section : Homework 5
    E-mail : jmautsa1@umbc.edu
    Description : lock and key
    """


def lock_and_key (key_cuts, lock_pinning,minimum):
     
     sumK_L = 0
     
     #checks if the list is eqaul to the key and lock  
     if(len(key_cuts) != len(lock_pinning)): return False
     
     for i in range(0,len(key_cuts)):
          
          #sum of the the key cuts and locking pin 
          sumK_L = (key_cuts[i] + lock_pinning[i])
          
          # formula to check if the lock opens 
          isCheck = (6-minimum) < sumK_L < (6+minimum)
          
          if not(isCheck): 
               return False

     return True

#main function   
def main():
   if lock_and_key([2.1, 3.5, 2.7], [4.1, 2.5, 3.2], 0.25):
      print('Unlocked')
   else:
      print('Still Locked')


   if lock_and_key([2.1, 3.5, 2.7, 1.7], [4.1, 2.5, 3.2], 0.25):
      print('Unlocked')
   else:
      print('Still Locked')


   if lock_and_key([2.1, 3.5, 2.7, 1.7], [4.1, 2.5, 3.2, 3.2], 0.25):
      print('Unlocked')
   else:
      print('Still Locked')
      
if __name__ == "__main__" :
   main()