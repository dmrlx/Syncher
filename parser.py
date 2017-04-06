from re import match as re_match
from os.path import isdir as path_isdir, isfile as path_isfile


def execute(args, results):
    results.cli = options_parse(args)
    results.password = password_parse(args)
    results.dirs = dirs_parse(args)
    results.files = files_parse(args)
    results.user = rem_user_parse(args)
    results.port = rem_port_parse(args)
    results.host = rem_host_parse(args)
    results.dist = rem_dirs_parse(args)

def check_for_match(pattern, some_list):
    match_list = []
    for element in some_list:
        match = re_match(pattern, element)
        if match:
            match_list.append(element)
    return " ".join(match_list)

def options_parse(some_list):
    options_pattern = r'(^-\w+|^--[\w\-\=]+[\w\d\/\.\_]+|^[\'"].+[\'"]$)'
    password_pattern = r'-pass=.+'
    options = check_for_match(options_pattern, some_list)
    password = check_for_match(password_pattern, some_list)
    return options.replace(password, '')

def password_parse(some_list):
    pattern = r'-pass=.+'
    return check_for_match(pattern, some_list).lstrip('-pass=')

def pull_local_info(some_list):
    pattern = r'^[^-\'"].+'
    found = check_for_match(pattern, some_list)
    remote_info = pull_remote_info(some_list)
    return found.replace(remote_info, '')

def dirs_parse(some_list):
    dirs = []
    for element in pull_local_info(some_list).split():
        if path_isdir(element):
            dirs.append(element)
    return " ".join(dirs)

def files_parse(some_list):
    files = []
    for element in pull_local_info(some_list).split():
        if path_isfile(element):
            files.append(element)
    return " ".join(files)

def pull_remote_info(some_list):
    pattern_full = r'^.+@.+'
    pattern_host = r'^.+:.*'
    for element in some_list:
        remote_full = re_match(pattern_full, element)
        remote_host = re_match(pattern_host, element)
        if remote_full:
            return element
        elif remote_host:
            return element
    return ''

def rem_user_parse(some_list):
    pattern = r'^\w+[^\:\.\,\@]*'
    remote_info = pull_remote_info(some_list)
    if '@' in remote_info:
        user = re_match(pattern, remote_info)
        if user:
            return user.group()
    return ''

def rem_port_parse(some_list):
    user = rem_user_parse(some_list)
    remote_info = pull_remote_info(some_list)
    if '@' in remote_info:
        remote_info = remote_info.split('@')
        port = remote_info[0].lstrip(user)
        if port:
            port = port.lstrip(':,.')
            return port
    return ''

def rem_host_parse(some_list):
    remote_info = pull_remote_info(some_list)
    if '@' in remote_info:
        host_plus_dir = remote_info.split('@')[1].split(':')
        return host_plus_dir[0]
    else:
        host_plus_dir = remote_info.split(':')
        return host_plus_dir[0]

def rem_dirs_parse(some_list):
    remote_info = pull_remote_info(some_list)
    if '@' in remote_info:
        host_plus_dir = remote_info.split('@')[1].split(':')
        if len(host_plus_dir) > 1:
            return host_plus_dir[1]
    else:
        host_plus_dir = remote_info.split(':')
        if len(host_plus_dir) > 1:
            return host_plus_dir[1]
        return ''


if __name__ == "__main__":
    from receiver import ArgsReceiver
    from variables import ParserResults
# Пример вызова функции
    execute(ArgsReceiver.receiver(), ParserResults)
    for attr in ['cli', 'password', 'dirs', 'files', 'user', 'port', 'host', 'dist']:
        print('{}: '.format(attr), end='')
        eval('print(ParserResults.{})'.format(attr))
