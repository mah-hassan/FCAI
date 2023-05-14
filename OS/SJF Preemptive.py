class Process():
    p_id = 0
    at = 0
    bt = 0
    rt = 0
    wt = 0             
    def __init__(self, p_id, at, bt):
        self.p_id = p_id
        self.at = at
        self.bt = bt
        self.rt = bt
        self.wt = 0    

current_time = 0
completed_processes = 0
total_waiting_time = 0   

# inputs
num_of_processes = int(input('Number of processes: '))
processes = []
for i in range(num_of_processes):
    p_id = int(input('Process ID: '))
    at = int(input('Arrival time: '))
    bt = int(input('Burst time: '))
    processes.append(Process(p_id, at, bt))

def sjf_preempetive(processes):
    global completed_processes  
    global current_time
    global total_waiting_time

    n = len(processes)
    while completed_processes < n:
        shortest_rt = 1000
        shortest_process = None                                 
        
        for i in range(n):                         
            if processes[i].at <= current_time and processes[i].rt < shortest_rt and processes[i].rt > 0:
                shortest_process = processes[i] 
                shortest_rt = processes[i].rt

        if shortest_process is None:
            current_time += 1
            continue
        shortest_process.rt -= 1
        for i in range(n):
            if processes[i].at <= current_time and processes[i] != shortest_process and processes[i].rt > 0:
                processes[i].wt += 1    # Increment waiting time of other processes that are waiting
        if shortest_process.rt == 0:
            completed_processes += 1
            completion_time = current_time + 1
            waiting_time = completion_time - shortest_process.at - shortest_process.bt
            shortest_process.wt = waiting_time
            total_waiting_time += waiting_time   # Update total waiting time
            print(f"P {shortest_process.p_id} completed at time {completion_time}, waiting time: {waiting_time}")
        current_time += 1

    avg_waiting_time = total_waiting_time / n   # Calculate average waiting time
    print(f"Average waiting time: {avg_waiting_time}")

sjf_preempetive(processes)