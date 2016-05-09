#!/bin/bash
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

workload_folder=`dirname "$0"`
workload_folder=`cd "$workload_folder"; pwd`
workload_root=${workload_folder}/../..
. "${workload_root}/../../bin/functions/load-bench-config.sh"

enter_bench HadoopSort ${workload_root} ${workload_folder}
show_bannar start

rmr-hdfs $OUTPUT_HDFS || true

if [ $# -eq 1  ]
then
    OUTPUT_HDFS=$1
fi

if [ $# -eq 2  ]
then
    OUTPUT_HDFS=$1
    QUEUE_NAME=$2
fi


SIZE=`dir_size $INPUT_HDFS`
START_TIME=`timestamp`
run-hadoop-job ${HADOOP_EXAMPLES_JAR} sort -D mapreduce.job.queuename=${QUEUE_NAME} ${COMPRESS_OPT} -outKey org.apache.hadoop.io.Text -outValue org.apache.hadoop.io.Text -r 20 ${INPUT_HDFS} ${OUTPUT_HDFS} 
END_TIME=`timestamp`

gen_report ${START_TIME} ${END_TIME} ${SIZE}
show_bannar finish
leave_bench


