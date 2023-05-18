class Process:
    def __init__(self, p_id, at, bt):
        self.p_id = p_id
        self.at = at
        self.bt = bt
        self.rt = bt 
        self.wt = 0
        self.completion_time = 0 

def round_robin(processes, quantum):
    # print(quantum)
    queue = []
    processes.sort(key=lambda x: x.at)
    queue.append(processes.pop(0))
    time = 0
    n = len(processes)
    output = []
    while queue and n > 0:
        selected_process = queue.pop(0)
        if selected_process.at <= time:
            if selected_process.rt > 0:
                if selected_process.rt > quantum:
                    selected_process.rt -= quantum
                    time += quantum
                else:
                    time += selected_process.rt
                    selected_process.rt = 0

                selected_process.completion_time = time
                selected_process.wt = time - selected_process.at - selected_process.bt

            else:
                Process.num_of_processes -= 1

            while processes and processes[0].at <= time:
                queue.append(processes.pop(0))

            if selected_process.rt > 0:
                queue.append(selected_process)

            if selected_process.rt == 0:
                output.append(selected_process)

        else:
            queue.append(selected_process)
            time += 1

    return output

