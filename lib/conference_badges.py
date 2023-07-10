def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    badge_list = [badge_maker(name) for name in names]
    return badge_list


def assign_rooms(names):
    room_assignment = [
        f"Hello, {name}! You'll be assigned to room {index+1}!"
        for index, name in enumerate(names)
    ]
    return room_assignment


def printer(names):
    [print(badge) for badge in batch_badge_creator(names)]
    [print(assignment) for assignment in assign_rooms(names)]


printer(["Arel", "Carol"])
