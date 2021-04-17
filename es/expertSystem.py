from experta import *

class patient(Fact):
    pass


class GoToDoctor(KnowledgeEngine):
    @Rule(patient(Headache="yes",Fatigue="yes",Increased_thirst="yes",Urinate_a_lot="yes"))
    def urinate_a_lot(self):
        print("Beginning increasing \n Drink water and walk a little.")

    @Rule(patient(Headache="yes",Fatigue="yes",Increased_thirst="no",Feeling_dryness="yes"))
    def feeling_dryness(self):
        print("increasing \nTake and increase your insulin dose.")

    @Rule(patient(Headache="yes",Fatigue="no",Tachycardia="yes",Blurred_vision="yes"))
    def Blurred_vision(self):
        print("Steep decreasing \nThe child should be given a glucagon needle and wait 10-15 minutes for the sugar to return to its normal level.")

    @Rule(patient(Headache="yes",Fatigue="no",Tachycardia="no",Shortness_of_breath="yes"))
    def Shortness_of_breath(self):
        print("Steep increasing \nYou should go to the doctor")

    @Rule(patient(Headache="no",Dizzy="yes",Stressed_or_anxious="yes"))
    def stressed_or_anxious(self):
        print("beginning decreasing \nEat and  take a rest.")

    @Rule(patient(Headache="no",Dizzy="no",Sweating="yes"))
    def sweating(self):
        print("Decreasing \ndrink Juice and don’t move at least 5 minutes.")

def declare():
    headache= input("Do you have a headache? \n").lower()
    if headache=="yes":
        fatigue=input("Do you feel Fatigue? \n").lower()
        if fatigue=="yes":
            increased_thirst=input("Do you have increased thirst? \n").lower()
            if increased_thirst=="yes":
                urinate_a_lot=input("Do you urinate a lot? \n").lower()
                if urinate_a_lot=="yes": 
                 return patient(Headache="yes",Fatigue="yes",Increased_thirst="yes",Urinate_a_lot="yes")
            else:
                feeling_dryness=input("Do you feeling dryness in the tongue and throat? \n").lower()
                return patient(Headache="yes",Fatigue="yes",Increased_thirst="no",Feeling_dryness="yes")
        else:
            tachycardia=input("Do you fell a Tachycardia? \n").lower()
            if tachycardia=="yes":
                blurred_vision=input("Do you have Blurred vision? \n").lower()
                return patient(Headache="yes",Fatigue="no",Tachycardia="no",Shortness_of_breath="yes")
            else:
                shortness_of_breath=input("Do you have Shortness of breath? \n").lower()
                return patient(Headache="yes",Fatigue="no",Tachycardia="no",Shortness_of_breath="yes")
    else:
        dizzy=input("Do you feel Dizzy? \n").lower()
        if dizzy=="yes":
            stressed_or_anxious=input("Do you feel stressed or anxious? \n").lower()
            return patient(Headache="no",Dizzy="yes",Stressed_or_anxious="yes")
        else:
            sweating=input("Do you feel sweating? \n").lower()
            return patient(Headache="no",Dizzy="no",Sweating="yes")


engine = GoToDoctor()
engine.reset()
engine.declare(declare())
engine.run()