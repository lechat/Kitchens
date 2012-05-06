
def base(kit):
    kit.add_cookbook_path(
        '/home/aleksey/src/cookbooks', 'kokki.cookbooks'
        )
    kit.update_config({
        'managed_server_1_port': 12010,
        'managed_server_2_port': 12020,
        'admin_server_port': 12001,
    })
    kit.include_recipe("stop_server")

    # kit.include_recipe("weblogic_base", 'wl_datasource', 'wl_jms')

