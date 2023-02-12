# Author: Sai Vikhyath Kudhroli
# Date: 05 November, 2022


"""
Description:
Given a set of jobs with start and finish times,
Interval Scheduling algorithm finds the maximum number of mutually compatible jobs.
"""

import cmath


class IntervalScheduling:
    """
    Given a set of jobs with start and finish times,
    Sort the jobs by finish times
    Then for each job, check if it is compatible with existing jobs and add to selected jobs if it is
    """

    def __init__(self, numberOfJobs: int) -> None:
        """
        Initialize number of jobs
        Maintain a list of job id's
        Maintain a list of start times
        Maintain a list of finish times
        """

        self.numberOfJobs = numberOfJobs
        self.jobId = []
        self.startTimes = []
        self.finishTimes = []

        for i in range(self.numberOfJobs):
            startTime = float(input("Enter start time of job " + str(i + 1) + " : "))
            self.startTimes.append(startTime)
            endTime = float(input("Enter finish time of job " + str(i + 1) + " : "))
            if startTime >= endTime:
                print("Job has to start and then end!! Quitting.....")
                quit()
            self.finishTimes.append(endTime)
            self.jobId.append(i + 1)


    def sortByFinishTime(self) -> None:
        """ Sorting the jobs by finish times"""
        
        for i1 in range(len(self.finishTimes) - 1):
            minIndex = i1
            for i2 in range(i1 + 1, len(self.finishTimes)):
                if self.finishTimes[minIndex] > self.finishTimes[i2]:
                    minIndex = i2
            self.finishTimes[i1], self.finishTimes[minIndex] = self.finishTimes[minIndex], self.finishTimes[i1]
            self.startTimes[i1], self.startTimes[minIndex] = self.startTimes[minIndex], self.startTimes[i1]
            self.jobId[i1], self.jobId[minIndex] = self.jobId[minIndex], self.jobId[i1]


    def intervalScheduling(self) -> None:
        """ After sorting the jobs by finish times, select the compatible jobs"""
        
        selectedJobs = set()
        finishTimeOfLastJob = - cmath.inf

        for i in range(self.numberOfJobs):
            if finishTimeOfLastJob == []:
                selectedJobs.add(self.jobId[i])
                finishTimeOfLastJob = self.finishTimes[i]
            elif self.startTimes[i] >= finishTimeOfLastJob:
                selectedJobs.add(self.jobId[i])
                finishTimeOfLastJob = self.finishTimes[i]

        print("Selected Jobs : ", selectedJobs)


if __name__ == "__main__":
    numberOfJobs = int(input("Enter total number of jobs: "))
    i = IntervalScheduling(numberOfJobs)
    i.sortByFinishTime()
    i.intervalScheduling()