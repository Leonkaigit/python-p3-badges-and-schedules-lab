def badge_maker(name):
    return f"Hello, my name is {name}." 

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    return ["Hello, {0}! You'll be assigned to room {1}!".format(name, index + 1) for index, name in enumerate(names)]

def printer(names):
    badge_messages = batch_badge_creator(names)

    for message in badge_messages:
        print(message)
    
    room_assignments = assign_rooms(names)
    for assignment in room_assignments:
        print(assignment)
    

    
