import os.path

def dev(kit):
    base(kit)

    kit.update_config({
        'users': ['dev_user1', 'dev_user2'],
    })
