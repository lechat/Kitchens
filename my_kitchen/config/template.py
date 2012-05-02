def template(kit):

    kit.add_cookbook_path(
        '/home/xleap/src/cookbooks', 'kokki.cookbooks'
        )

    kit.update_config({
        'file_path' : '/tmp/sample_file',
        'users' : ['user1', 'user2'],
    })

    kit.include_recipe("simple_file")
