# Author: Sai Vikhyath Kudhroli
# Date: 14 November, 2022


"""
Description:
Given n tasks along with the number of units of time to complete each of the jobs and the respective deadlines,
Find a way to schedule the tasks in such a way that maximum lateness is minimized
"""

import cmath


class MinimizingLateness:
    """
    Given n tasks with their processing times and deadlines,
    Sort the tasks in increasing order of their deadlines,
    Then schedule each job while maintaining the start time, finish time of the job and the maximum lateness.
    """

    def __init__(self, numberOfJobs: int) -> None:
        """
        Maintain a list of all job IDs.
        Maintain a list of processing times of the jobs.
        Maintain a list of deadlines of the jobs.
        """

        self.numberOfJobs = numberOfJobs
        self.jobId = []
        self.processingTimes = []
        self.dueTimes = []
        
        for i in range(self.numberOfJobs):
            processingTime = float(input("Enter processing time of job " + str(i + 1) + " : "))
            self.processingTimes.append(processingTime)
            dueTime = float(input("Enter due time of job " + str(i + 1) + " : "))
            if processingTime >= dueTime:
                print("Error: Job can't have processing time greater than due time!! Quitting.....")
                quit()
            self.dueTimes.append(dueTime)
            self.jobId.append(i + 1)


    def sortByDueTime(self) -> None:
        """ Sort the jobs in increasing order of the job deadlines."""
        
        for i1 in range(len(self.dueTimes) - 1):
            minIndex = i1
            for i2 in range(i1 + 1, len(self.dueTimes)):
                if self.dueTimes[minIndex] > self.dueTimes[i2]:
                    minIndex = i2
            self.dueTimes[i1], self.dueTimes[minIndex] = self.dueTimes[minIndex], self.dueTimes[i1]
            self.processingTimes[i1], self.processingTimes[minIndex] = self.processingTimes[minIndex], self.processingTimes[i1]
            self.jobId[i1], self.jobId[minIndex] = self.jobId[minIndex], self.jobId[i1]


    def minimizingLateness(self) -> None:
        """ Once the jobs are sorted based on their deadlines,
            Take one job at a time and schedule them while noting the start time, finish time and maximum lateness.    
        """
        
        currentTime = 0
        maxLateness = 0
        jobIntervals = dict()
 
        for i in range(self.numberOfJobs):
            if currentTime + self.processingTimes[i] > self.dueTimes[i]:
                maxLateness = max(maxLateness, currentTime + self.processingTimes[i] - self.dueTimes[i])
            jobIntervals[self.jobId[i]] = (currentTime, currentTime + self.processingTimes[i])
            currentTime = currentTime + self.processingTimes[i]
        
        print("\n\nScheduled start and end times of jobs: ", jobIntervals)
        print("\nMax Lateness: ", maxLateness)


if __name__ == "__main__":
    numberOfJobs = int(input("Enter total number of jobs: "))
    i = MinimizingLateness(numberOfJobs)
    i.sortByDueTime()
    i.minimizingLateness()