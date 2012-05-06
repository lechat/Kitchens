
def stop(kit):
    sbase(kit)
    kit.include_recipe("simplehttpserver.stop")

    # kit.include_recipe("weblogic_base", 'wl_datasource', 'wl_jms')

