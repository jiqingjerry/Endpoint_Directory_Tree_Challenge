# Set this to True to see debug statements
DEBUG = False
# To read commands from a file, enter the path here (ex: foo/bar/test_input.txt)
TEST_FILE = ''

class Directory():
    def __init__(self, name='root'):
        self.name = name
        self.subdirectories = {}

    def create(self, path):
        '''
        Create directory/subdirectory.

        Only creates when directory doesn't exist
        '''
        debug_print(f'Create directory: {path}')

        curr_dir = path[0]
        if curr_dir not in self.subdirectories:
            new_dir = Directory(curr_dir)
            self.subdirectories[curr_dir] = new_dir
            path.pop(0)
            if path:
                new_dir.create(path)
        else:
            path.pop(0)
            if not path:
                print(f'Cannot create directory: {curr_dir} already exists')
                return
            self.subdirectories[curr_dir].create(path)
    
    def get(self, path):
        '''
        Helper function to get a directory from path
        '''
        debug_print(f'Get directory: {path}')

        current_dir = self
        path_list = path.split('/')
        invalid_dir = None
        for dir in path_list:
            if dir in current_dir.subdirectories:
                current_dir = current_dir.subdirectories[dir]
            else:
                invalid_dir = dir
        if current_dir.name != path_list[-1]:
            return {'success': False, 'directory': invalid_dir}
        else:
            return {'success': True, 'directory': current_dir}

    def delete(self, path):
        '''
        Delete directory from path
        '''
        debug_print(f'Delete directory: {path}')

        current_dir = self
        invalid_dir = None
        path_list = path.split('/')
        for dir in path_list:
            if dir in current_dir.subdirectories:
                if dir == path_list[-1]:
                    current_dir = current_dir.subdirectories.pop(dir)
                else:
                    current_dir = current_dir.subdirectories[dir]
            else:
                invalid_dir = dir
                break
        if invalid_dir:
            print(f'Cannot delete {path} - {invalid_dir} does not exist')
        return
    
    def move(self, source_path, dest_path):
        '''
        Move directory from source_path to dest_path
        '''
        debug_print(f'Move directory: from {source_path} to {dest_path}')
        
        source_dir = self.get(source_path)
        if not source_dir['success']:
            print(f'Cannot move {source_path} to {dest_path} - {source_dir['directory']} does not exist')
            return
        
        destination_dir = self.get(dest_path)
        if not destination_dir['success']:
            print(f'Cannot move {source_path} to {dest_path} - {destination_dir['directory']} does not exist')
            return
        
        destination_dir['directory'].subdirectories[source_dir['directory'].name] = source_dir['directory']
        self.delete(source_path)

    def list(self, debug = False, prefix = ''):
        '''
        Pretty print the current directory structure starting from the root, subdirectories are indented
        '''
        for dir in sorted(self.subdirectories):
            if debug:
                print(f'[DEBUG] {prefix}{dir}')
            else:
                print(f'{prefix}{dir}')
            self.subdirectories[dir].list(debug, prefix + '  ')

def debug_print(message):
    '''
    Debug function to print more info
    '''
    if DEBUG:
        print(f'[DEBUG] {message}')

if __name__ == '__main__':
    directory = Directory()
    debug_print('Endpoint - Backend Coding Challenge')
    if TEST_FILE:
        with open(TEST_FILE, 'r') as file:
            commands = file.readlines()

    while True:
        cmd = ''
        if TEST_FILE:
            if commands:
                cmd = commands.pop(0).strip()
            else:
                break
        else:
            cmd = input()

        cmd_args = cmd.split(' ')
        debug_print(f'command: {cmd}')
        debug_print(f'cmd_args: {cmd_args}')

        if cmd_args[0] == 'CREATE':
            if len(cmd_args) == 2:
                path = cmd_args[1].split('/')
                directory.create(path)
        elif cmd_args[0] == 'MOVE':
            if len(cmd_args) == 3:
                directory.move(cmd_args[1], cmd_args[2])
        elif cmd_args[0] == 'DELETE':
            if len(cmd_args) == 2:
                directory.delete(cmd_args[1])
        elif cmd_args[0] == 'LIST':
            directory.list()
        else:
            print('Invalid Command')

        if DEBUG and cmd_args[0] != 'LIST':
            debug_print('Current directory structure:')
            directory.list(debug = DEBUG)