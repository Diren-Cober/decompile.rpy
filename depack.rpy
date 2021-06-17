# RenPy archive unpacker 1.2

# Modified by DC



init -9000 python:

    import os
    import shutil

    g_open = open
    os_path = os.path
    os_makedirs = os.makedirs
    os_path_join = os_path.join
    os_path_exists = os_path.exists
    os_path_dirname = os_path.dirname
    shutil_copyfileobj = shutil.copyfileobj

    _LB_game_dir = os.path.join(config.basedir, "game")
    _LB_output_dir = os.path.join(config.basedir, "unpacked", "game")

    try:
        _LB_list_files = renpy.list_files

    except AttributeError:
        # for RenPy before 6.11.0
        _LB_list_files = lambda: [
            fn for dn, fn in renpy.loader.listdirfiles() if dn != renpy.config.commondir
        ]

    try:
        _LB_file = renpy.file
    except AttributeError:
        try:
            _LB_file = renpy.notl_file
        except AttributeError:
            # for RenPy before 6.3.0
            _LB_file = renpy.loader.load

    for filename in _LB_list_files():

        if filename[0] not in ('_', '0'):
            
            in_path = os_path_join(_LB_game_dir, filename)
            out_path = os_path_join(_LB_output_dir, filename)

            if  not os_path_exists(in_path) and not os_path_exists(out_path):

                out_dir_name = os_path_dirname(out_path)
                if  not os_path_exists(out_dir_name):
                    os_makedirs(out_dir_name)
            
                with g_open(out_path, "wb") as dest, _LB_file(filename) as origin:
                    shutil_copyfileobj(origin, dest)
