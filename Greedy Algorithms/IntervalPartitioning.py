# Author: Sai Vikhyath Kudhroli
# Date: 14 November, 2022


"""
Description:
Given n lectures with their start times and finish times respectively,
Compute the minimum number of classrooms required to accomodate the lectures.
"""

"""
Note: 
Assign the start and finish times as numbers after mapping the timestamps relatively to numericals via any convention.
"""


import cmath


class IntervalPartitioning:
    """
    Given n lectures with start and finish times,
    Sort the lectures in ascending order of their start times.
    Then for each lecture check if it can be accomodated in existing classrooms, if not, add another classrooms and assign it to the lecture
    """

    def __init__(self, numberOfLectures: int) -> None:
        """
        Initialize number of lectures
        Maintain a list of lecture numbers
        Maintain a list of start times of the lectures
        Maintain a list of finish times of the lectures
        """

        self.numberOfLectures = numberOfLectures
        self.lectureId = []
        self.startTimes = []
        self.finishTimes = []

        for i in range(self.numberOfLectures):
            startTime = float(input("Enter start time of lecture " + str(i + 1) + " : "))
            self.startTimes.append(startTime)
            endTime = float(input("Enter finish time of lecture " + str(i + 1) + " : "))
            if startTime >= endTime:
                print("Invalid Input: Lecture has to start and then end!! Quitting.....")
                quit()
            self.finishTimes.append(endTime)
            self.lectureId.append(i + 1)


    def sortByStartTime(self) -> None:
        """ Sort the lectures by start time"""
        
        for i1 in range(len(self.startTimes) - 1):
            minIndex = i1
            for i2 in range(i1 + 1, len(self.finishTimes)):
                if self.startTimes[minIndex] > self.startTimes[i2]:
                    minIndex = i2
            self.startTimes[i1], self.startTimes[minIndex] = self.startTimes[minIndex], self.startTimes[i1]
            self.finishTimes[i1], self.finishTimes[minIndex] = self.finishTimes[minIndex], self.finishTimes[i1]
            self.lectureId[i1], self.lectureId[minIndex] = self.lectureId[minIndex], self.lectureId[i1]



    def intervalPartitioning(self) -> None:
        """ After sorting the lectures by finish time,
            Check if the class can be accomodated in one of the existing classes.
            If not, assign a new classroom to that lecture and update the finish time of the classroom.
        """
        numberOfClassroomsAllocated = 0
        finishTimesOfClassrooms = []

        for i in range(self.numberOfLectures):
            if numberOfClassroomsAllocated == 0:
                numberOfClassroomsAllocated += 1
                finishTimesOfClassrooms.append(self.finishTimes[i])
            else:
                for j in range(len(finishTimesOfClassrooms)):
                    if self.startTimes[i] >= finishTimesOfClassrooms[j]:
                        finishTimesOfClassrooms[j] = self.finishTimes[i]
                        break
                else:
                    numberOfClassroomsAllocated += 1
                    finishTimesOfClassrooms.append(self.finishTimes[i])
        
        print("Number of classrooms required: ", numberOfClassroomsAllocated)




if __name__ == "__main__":
    numberOfLectures = int(input("Enter total number of lectures: "))
    i = IntervalPartitioning(numberOfLectures)
    i.sortByStartTime()
    i.intervalPartitioning()