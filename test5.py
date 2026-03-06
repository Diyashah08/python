class rotation:
    def __init__(self,a,b):
        if a==b:
            print("yes rotation")
        else:
            rotate_right(b)
    def rotate_right(s:str):
        return s[-1]+s[:-1]
    
    def main():
        a=input("enter og string")
        b=input("enter a string to check")
        ob=rotation(a,b)
                
            