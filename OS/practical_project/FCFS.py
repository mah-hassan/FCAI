def fcfs(processes):
    completed_processes = 0
    current_time = 0
    output = []
    n = len(processes)

    while completed_processes < n:
        selected_at = 100000
        selected_process = None
        for i in range(n):
            if processes[i].at <= current_time and processes[i].rt > 0 and processes[i].at < selected_at:
                selected_process = processes[i]
                selected_at = processes[i].at

        if selected_process == None:
            current_time += 1
            continue

        def update_wt():
            for i in range(n):
                if processes[i].at <= current_time and processes[i] != selected_process and processes[i].rt > 0:
                    processes[i].wt += 1

        while selected_process.rt > 0:
            selected_process.rt -= 1
            update_wt()
            current_time += 1

        if selected_process.rt == 0:
            completed_processes += 1
            completion_time = current_time
            waiting_time = completion_time - selected_process.at - selected_process.bt
            selected_process.wt = waiting_time
            selected_process.completion_time = completion_time
            output.append(selected_process)

    return output
