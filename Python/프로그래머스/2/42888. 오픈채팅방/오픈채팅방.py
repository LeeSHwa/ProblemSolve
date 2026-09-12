def solution(record):
    
    logs = []
    answer = []
    
    users = {}
    # 0 : Enter / 1 : Change / 2 : Leave
    for log in record:        
        if log[:5] == "Leave":
            comm, uuid = log.split()
        else:
            comm, uuid, nickname = log.split()

            
        if comm == "Enter":
            users[uuid] = nickname
            logs.append((0, uuid))
        elif comm == "Change":
            users[uuid] = nickname
        else:
            logs.append((2, uuid))
            
    
    for comm, uid in logs:
        
        temp = users[uid] + "님이 들어왔습니다." if comm == 0 else users[uid] + "님이 나갔습니다."
    
        answer.append(temp)


    return answer
