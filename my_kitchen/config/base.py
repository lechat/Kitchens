
def sbase(kit):

    kit.add_cookbook_path(
        '/home/aleksey/src/cookbooks', 'kokki.cookbooks'
        )
    kit.update_config({
        'managed_server_1_port': 8010,
        'managed_server_2_port': 8020,
        'admin_server_port': 8001,
    })

