def fabfile(kit):

    kit.add_cookbook_path(
        '/home/xleap/src/cookbooks', 'kokki.cookbooks'
        )

    kit.update_config({
        'roles' : ['forge'],
        'roledefs' : { 'forge': ['ama385@forge.xleap.apmoller.net']},
        'local_path' : '/home/xleap/src/kitchens/my_kitchen/kitchen.yml',
        'remote_path' : '/tmp/kitchen.yml',
        'command' : 'touch asdasdasd; rm asdasdasd'
    })

    kit.include_recipe("collect_logs")
