from time import *
import random as r
def mistake(paratest,usertest):
    error=0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error=error+1
        except:
            error= error+1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay=time_e-time_s
    time_R=round(time_delay,2)
    speed = len(userinput)/time_R
    return  round(speed)
if __name__ == '__main__':

        while True:
            chk=input("Ready to test : yes/no:")
            if chk == "yes":

                test=["A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.",
                "my name is Lavkesh","welcome to my first program"]
                test1=r.choice(test)
                print("typing speed")
                print(test1)
                print()
                print()
                time_1=time()
                testinput=input("Enter: ")
                time_2=time()

                print('Speed: ',speed_time(time_1,time_2,testinput),"w/s")
                print("Error: ",mistake(test1,testinput))

            elif chk=="no":
                print("Thank you")
                break
            else:
                print("Wromg in put")