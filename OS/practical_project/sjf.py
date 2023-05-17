
def sjf_non_preempetive(processes):
    current_time = 0
    completed_processes = 0
    output = []

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

        def update_wt():
            for i in range(n):
                if processes[i].at <= current_time and processes[i] != shortest_process and processes[i].rt > 0:
                    processes[i].wt += 1

        while shortest_process.rt > 0:
            shortest_process.rt -= 1
            update_wt()
            current_time += 1

        if shortest_process.rt == 0:
            completed_processes += 1
            completion_time = current_time
            waiting_time = completion_time - shortest_process.at - shortest_process.bt
            shortest_process.wt = waiting_time
            shortest_process.completion_time = completion_time
            output.append(shortest_process)

    return output


def sjf_preempetive(processes):
    current_time = 0
    completed_processes = 0
    output = []

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
                processes[i].wt += 1
        if shortest_process.rt == 0:
            completed_processes += 1
            completion_time = current_time + 1
            waiting_time = completion_time - shortest_process.at - shortest_process.bt
            shortest_process.wt = waiting_time
            shortest_process.completion_time = completion_time
            output.append(shortest_process)

        current_time += 1

    return output
