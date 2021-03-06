#!/bin/python


from threading import Thread
import time
class JobSet:


    def __init__(self):
        self.job_set = {}
        self.jobs    = []
        self.job_all_finished = False


    def add_jobs(self,jobs,sync):
        for job in jobs:
            if sync != 0:
                time.sleep(sync)
            job.run_job()
            self.jobs.append(job)
            self.job_set[job.current_id]  = job


    def submitted_jobs(self):
        return len(self.jobs)

    def get_job_all_finished(self):
        pass
        
    def wait_to_complete(self):
        for job in self.jobs:
            while job.is_finish() is False:
                time.sleep(2)
        
