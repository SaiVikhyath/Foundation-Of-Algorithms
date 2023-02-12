# Author: Sai Vikhyath Kudhroli
# Date: 02 November, 2022


"""
Description:
Given n men and n women and the preferences of each man and woman, 
Gale-Shapley's stable matching algorithm finds a perfect matching without any unstable pairs.
"""


from collections import defaultdict
from collections import deque


class StableMatching:
    """
    Given the preference lists of n men and n women, Gale Shapley's stable matching finds the stable matching
    Stable matching is a monogamous matching without any unstable pairs
    """
    
    def __init__(self, numberOfMen: int, numberOfWomen: int) -> None:
        """
        Initialize all the data structures used to implement stable matching algorithm
        Maintain two default dictionaries to maintain preference lists of men and women
        Maintain a queue to store all the free men.
        Maintain two lists, to store the wife and husband information of men and women respectively
        Maintain a dictionary that stores the number of proposals made by the men
        """

        self.numberOfMen = numberOfMen
        self.numberOfWomen = numberOfWomen

        self.freeMen = deque()

        self.wifeOf = [0] * self.numberOfMen
        self.husbandOf = [0] * self.numberOfWomen
        
        self.countOfProposals = defaultdict()

        for i in range(self.numberOfMen):
            self.countOfProposals[i + 1] = 0
    

        self.mensPreferences = defaultdict(list)
        self.womensPreferences = defaultdict(list)

        for iM in range(self.numberOfMen):
            for iP in range(self.numberOfWomen):
                self.mensPreferences[iM + 1].append(int(input("\nEnter man " + str(iM + 1) + "'s preference " + str(iP + 1) + ": ")))
        
        for iW in range(self.numberOfWomen):
            for iP in range(self.numberOfMen):
                self.womensPreferences[iW + 1].append(int(input("\nEnter women " + str(iW + 1) + "'s preference " + str(iP + 1) + ": ")))
        
        for iM in range(self.numberOfMen):
            self.freeMen.append(iM + 1)

        print("\nMen's preference list: ", self.mensPreferences)
        print("\nWomen's preference list: ", self.womensPreferences)
        print("\nFree men: ", self.freeMen)
        print("\nWife of: ", self.wifeOf)
        print("\nHusband of: ", self.husbandOf)
        print("\nCount of proposals: ", self.countOfProposals)
        print("\n\n")


    def findPerfectMatchingGaleShapley(self) -> None:
        """
        Gale-Shapley implementation for the stable matching problem
        """
        
        while self.freeMen and all([True if i != self.numberOfWomen else False for i in self.countOfProposals.values()]):
            
            print("\n\n")
            print("Free Men: ", self.freeMen)
            
            man = self.freeMen.popleft()
            
            woman = self.mensPreferences[man][self.countOfProposals[man]]
            
            print(str(man) + " proposing to " + str(woman))
            
            self.countOfProposals[man] += 1
            womanPreferenceList = self.womensPreferences[woman]
            print("\nWoman's preference list: ", womanPreferenceList)
            
            if woman not in self.wifeOf:
                self.husbandOf[woman - 1] = man
                self.wifeOf[man - 1] = woman
                print("\nEngaged for first time")
            
            elif womanPreferenceList.index(self.husbandOf[woman - 1]) > womanPreferenceList.index(man):
                self.freeMen.append(womanPreferenceList[womanPreferenceList.index(self.husbandOf[woman - 1])])
                self.wifeOf[self.husbandOf[woman - 1] - 1] = 0
                self.husbandOf[woman - 1] = man
                self.wifeOf[man - 1] = woman
                print("\nDitched and Engaged")
            
            else:
                self.freeMen.append(man)
                print("\nRejected")
                continue
            
            print("\n")
            print("Proposal count: ", self.countOfProposals)
            print("Husbands of: ", self.husbandOf)
            print("Wives of: ", self.wifeOf)

        print("\n\nStable husbands for wives: ", self.husbandOf)


if __name__ == "__main__":
    numberOfMen = int(input("\nEnter number of men or women: "))
    s = StableMatching(numberOfMen, numberOfMen)
    s.findPerfectMatchingGaleShapley()
