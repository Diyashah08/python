def segerigate_marks(lst):
     A_Grade=[]
     B_Grade=[]
     C_Grade=[]
     for i in lst:
        if i>=80:
            A_Grade.append(i)
        elif i>=50 and i<80:
            B_Grade.append(i)
        else:
            C_Grade.append(i)  
     return A_Grade,B_Grade,C_Grade
            
def main():
     marks = [23,65,85,29,78,93,46,62,39]
     A_Grade,B_Grade,C_Grade=segerigate_marks(marks)
     
     for i in A_Grade:
      print("A Grade Marks:",i)
      
     for i in A_Grade:
           print("A Grade Marks:",i)

           for i in A_Grade:
               print("A Grade Marks:",i)
            
            
if __name__=="__main__":
        main()