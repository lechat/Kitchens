
def base(kit):
    kit.add_cookbook_path(
        '/home/xleap/src/cookbooks', 'kokki.cookbooks'
        )
    kit.update_config({
        'users': ['user_ss1', 'user2'],
        'file_path': '/tmp/simple_user_file.txt',
        # 'uname_param': '-s',
        'weblogic_base_port': 8080,
        'wl_datasource': { 'ds1': 'MDM', 'ds2': 'XLEAP' },
        'wl_jms' : {'q1'}
    })
    kit.include_recipe("stop_server")

    # kit.include_recipe("weblogic_base", 'wl_datasource', 'wl_jms')

