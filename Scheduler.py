#!/bin/python
import ConfUtils
import Queue

class SchedulerPlan:

    
    def __init__(self):
        ##global variable, we only have one plan at any time
        self.conf = ConfUtils.Configure()
        self.cluster_url = self.conf.get("hadoop.url")+"/ws/v1/cluster/info"

        ##check the cluster is running
        clusterInfo=ConfUtils.read_json_url(self.cluster_url)
        if clusterInfo.get("clusterInfo") is None:
            raise Exception("cluster is not running")         
        ##try to make Queue Monitor objects
        scheduler_type = Queue.QueueMonitor.get_scheduler_type(self.conf)
        if  scheduler_type == "capacityScheduler":
            self.queueMonitor=Queue.CapacityQueueMonitor(self.conf)
        elif scheduler_type == "fifoScheduler":
            self.queueMonitor=Queue.FifoQueueMonitor(self.conf)
        else:
            raise Exception("scheduler is not supported")

        ##monitor queue for the first time
        self.queueMonitor.monitor_queue()


        slef.generatos = []
        ##try to make generator
        generator_types = self.conf.get("generators")

        if generator_types is None:
            raise Exception("missing generators")

        ##TODO reflection
        for generator_type in generator_types:
            if generator_type == "OrderGenerator":
                generator = OrderGenerator(self.conf,self.queueMonitor) 
            elif generator_type == "PoissonGenerator":
                generator = PoissonGenerator(self.conf,self.queueMonitor)
            elif generator_type == "CapacityGenerator":
                generator = CapacityGenerator(self.conf,self.queueMonitor)
            else:
                raise Exception("unknown generator")
            generatos.append(generator)

        ##get run time
        self.run_time = self.conf.get("runtime")
        assert(self.run_time > 100) 

        ##whole job set
        self.jobs = []            


    def run(self):

        print "start"
        ##main loop
        while self.run_time > 0:
            for generator in self.generators:
                new_jobs = generator.generate_request()
                ##store new jobs
                self.jobs += new_jobs 
            time.sleep(1)
                 
        
         
if __name__ =="__main__":

    scheduelr_plan = SchedulerPlan()
    scheduler_plan.run()



