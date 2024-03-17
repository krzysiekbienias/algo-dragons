from typing import List


# 2383 easy but not efficient solution
def minNumberOfHours(initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        training_energy=0
        current_energy=initialEnergy
        for i in range(len(energy)):
            while current_energy-energy[i]<=0:
                training_energy+=1
                current_energy+=1
            else:
              current_energy-=energy[i]
        training_exp=0
        current_experience=initialExperience
        for i in range(len(experience)):
            while current_experience-experience[i]<=0:
                training_exp+=1
                current_experience+=1
            else:
                training_exp+=0
                current_experience+=experience[i]    
        return training_energy+training_exp


minNumberOfHours(initialEnergy=1,initialExperience=1,energy=[1,1,1,1],experience=[1,1,1,50])
