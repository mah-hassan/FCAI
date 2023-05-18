import sjf
import FCFS
import Round_Robin
import tkinter as tk

class Process:
    def __init__(self, p_id, at, bt):
        self.p_id = p_id
        self.at = at
        self.bt = bt
        self.rt = bt 
        self.wt = 0
        self.completion_time = 0 
        self.wt = 0

global processes

def create_processes():
    processes = []
    for i in range(len(process_ids)):
        p_id = int(process_ids[i].get())
        at = int(arrival_times[i].get())
        bt = int(burst_times[i].get())
        processes.append(Process(p_id, at, bt))
    return processes

def generate_inputs():
    for widget in input_frame.winfo_children():
        widget.destroy()

    global process_ids
    global arrival_times
    global burst_times
    process_ids = []
    arrival_times = []
    burst_times = []

    for i in range(num_of_processes.get()):
        process_id_label = tk.Label(input_frame, text=f"Process ID {i+1}:")
        process_id_label.grid(row=i, column=0, padx=5, pady=5)
        process_id_var = tk.StringVar()
        process_id_entry = tk.Entry(input_frame, textvariable=process_id_var)
        process_id_entry.grid(row=i, column=1, padx=5, pady=5)
        process_ids.append(process_id_entry)

        arrival_time_label = tk.Label(input_frame, text=f"Arrival time {i+1}:")
        arrival_time_label.grid(row=i, column=2, padx=5, pady=5)
        arrival_time_var = tk.StringVar()
        arrival_time_entry = tk.Entry(
            input_frame, textvariable=arrival_time_var)
        arrival_time_entry.grid(row=i, column=3, padx=5, pady=5)
        arrival_times.append(arrival_time_entry)

        burst_time_label = tk.Label(input_frame, text=f"Burst time {i+1}:")
        burst_time_label.grid(row=i, column=4, padx=5, pady=5)
        burst_time_var = tk.StringVar()
        burst_time_entry = tk.Entry(input_frame, textvariable=burst_time_var)
        burst_time_entry.grid(row=i, column=5, padx=5, pady=5)
        burst_times.append(burst_time_entry)


def avarrage_waiting_time(output):
    total_waiting_time = 0
    for p in output:
        total_waiting_time += p.wt
    return total_waiting_time / len(output)


def show_output(output, algorithm_name):
    output_text.delete('1.0', 'end')
    output_text.insert('end', f"{algorithm_name} Algorithm\n")
    output_text.insert('end', "Process ID | Completion Time | Waiting Time\n")
    for p in output:
        output_text.insert(
            'end', f"{p.p_id}\t\t| {p.completion_time}\t\t| {p.wt}\n")
    output_text.insert(
        'end', f"average waiting time : {avarrage_waiting_time(output)}")


def show_FCFS_output(output):
    show_output(output, "FCFS")


def show_sjfPreemptive_output(output):
    show_output(output, "SJF Preemptive")


def show_sjfNonPreemptive_output(output):
    show_output(output, "SJF Non-Preemptive")

def show_RoundRobin_output(output):
    show_output(output, "Round Robin")

root = tk.Tk()
root.title("CPU Scheduler")
root.configure(bg="white",padx=100,pady=20)

title_label = tk.Label(root,text="Welcome to CPU Scheduler",font=("Arial",18),bg="white")
title_label.pack(pady=10)

input_button_frame = tk.Frame(root,bg="white")
input_button_frame.pack()

num_of_processes_label = tk.Label(input_button_frame,text="Number of processes:",justify=tk.RIGHT,bg="white")
num_of_processes_label.grid(row=0,column=0,padx=10,pady=10)
num_of_processes = tk.IntVar(value=3)
num_of_processes_entry = tk.Entry(input_button_frame,textvariable=num_of_processes)
num_of_processes_entry.grid(row=0,column=1,padx=10,pady=10)
generate_button = tk.Button(input_button_frame,text="Enter inputs",command=generate_inputs,bg="#00bfff",fg="white",relief=tk.RAISED)
generate_button.grid(row=0,column=2,padx=10,pady=10)

input_frame = tk.Frame(root,bg="white")
input_frame.pack()

algorithm_frame = tk.LabelFrame(root,text="Choose an algorithm",bg="white",borderwidth=5,relief=tk.GROOVE)
algorithm_frame.pack(pady=(20,10))

run_non_preempetive_button = tk.Button(algorithm_frame,text="Run sjf_non_preempetive",command=lambda: show_sjfNonPreemptive_output(
 sjf.sjf_non_preempetive(create_processes())),font=("Arial",12),bg="#00bfff",fg="white",relief=tk.RAISED)
run_non_preempetive_button.pack(fill=tk.X,padx=(10),pady=(10))

run_preempetive_button = tk.Button(algorithm_frame,text="Run sjf_preempetive",command=lambda: show_sjfPreemptive_output(
 sjf.sjf_preempetive(create_processes())),font=("Arial",12),bg="#00bfff",fg="white",relief=tk.RAISED)
run_preempetive_button.pack(fill=tk.X,padx=(10),pady=(10))

run_fcfs_button = tk.Button(algorithm_frame,text="Run FCFS",command=lambda: show_FCFS_output(
 FCFS.fcfs(create_processes())),font=("Arial",12),bg="#00bfff",fg="white",relief=tk.RAISED)
run_fcfs_button.pack(fill=tk.X,padx=(10),pady=(10))
quantum_label = tk.Label(root,text="Quantum:",justify=tk.RIGHT,bg="white")
quantum_label.pack(pady=(20,10))
quantum_input = tk.IntVar(value=4)
quantum_entry = tk.Entry(root,textvariable=quantum_input)
quantum_entry.pack(pady=(0,10))
run_round_robin_button = tk.Button(algorithm_frame, text='Round Robin', command=lambda: show_RoundRobin_output(Round_Robin.round_robin(create_processes(), quantum_input.get())), font=("Arial", 12), bg="#00bfff", fg="white", relief=tk.RAISED)
run_round_robin_button.pack(fill=tk.X,padx=(10),pady=(10))

output_frame = tk.LabelFrame(root,text="Output",bg="white",borderwidth=5,relief=tk.GROOVE)
output_frame.pack(pady=(20))

output_text = tk.Text(output_frame,width=50,height=10)
output_text.pack()

root.mainloop()
