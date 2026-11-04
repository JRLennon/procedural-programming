def count_available(events, expiry_time):
    # store each process's last valid time
    expiry = {}
    
    for operation, process_id, time in events:
        if operation == 0: # create a process
            expiry[process_id] = time + expiry_time
        elif operation == 1: # restart it if it has not expired (giving it a new expiry time)
            if process_id in expiry and time <= expiry[process_id]:
                expiry[process_id] = time + expiry_time
    
    if not events:
        return 0 # create a new process
    
    # a process is active at the final event time if it has not expired yet?
    final_time = events[-1][2]
    return sum (deadline >= final_time for deadline in expiry.values())

events = [
    [0, 1, 1],
    [0, 2, 2],
    [1, 1, 3],
    [1, 2, 10]
]

expiry_time = 5

print(count_available(events, expiry_time))  # 0
