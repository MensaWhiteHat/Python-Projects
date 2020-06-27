Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def start(nice=0, mean=0, name=""):
	#get users name
	name = describe_game(name)
	nice, mean, name = nice_mean(nice, mean, name)

	
>>> def describe_game(name):
	if name != "":
		print("\nThank you for playing again, {}.".format(name))
	else:
		stop = True
		while stop:
			if name == "":
				name = input("\nWhat is your name? \n>>>").capitalize()
				if name != "":
					print("\nWelcome {}".format(name))
					print("\nIn this game, you will be greeted by \nmany different people. You may choose to be \nnice or mean")
					print("but your actions will determine your fate")
					stop = False
	return name

>>> def nice_mean(nice, mean, name):
	stop = True
	while stop:
		show_score(nice, mean, name)
		pick = input()"\nA stranger approaches you, \nare you nice?\nor mean? (N/M) \n>>>").lower()
		
SyntaxError: invalid syntax
>>> def nice_mean(nice, mean, name):
	stop = True
	while stop:
		show_score(nice, mean, name)
		pick = input("\nA stranger approaches you, \nare you nice?\nor mean? (N/M) \n>>>").lower()
		if pick == "n":
			print("walks away smiling")
			nice = (nice + 1)
			stop = False
		if pick == "m":
			print("the stranger is angry")
			mean = (mean + 1)
			stop = False
	score(nice, mean, name)

	
>>> def show_score(nice, mean, name):
	print("\n{}, your current total is: \n({}, Nice) and ({}, Mean)".format(name, nice, mean))

	
>>> def score(nice, mean, name):
	if nice > 2:
		win(nice, mean, name)
	if mean > 2:
		lose(nice, mean, name)
	else:
		nice_mean(nice, mean, name)

		
>>> def win(nice, mean, name):
	print("\nNice job!")
	again(nice, mean, name)

	
>>> def again(nice, mean, name):
	stop = True
	while stop:
		choice = input("\nDo you want to play again? (y/n):\n>>>").lower()
		if choice = "y":
			
SyntaxError: invalid syntax
>>> def again(nice, mean, name):
	stop = True
	while stop:
		choice = input("\nDo you want to play again? (y/n):\n>>>").lower()
		if choice == "y":
			stop = False
			reset(nice, mean, name)
		if choice == "n":
			stop = False
			quit()
		else:
			print("Enter (Y) for YES and (N) for NO:\n>>>")

			
>>> def reset(nice, mean, name):
	nice = 0
	mean = 0
	start(nice, mean, name)def win(nice, mean, name):
		print("\nNice job!")
		again(nice, mean, name)
		
SyntaxError: invalid syntax
>>> def reset(nice, mean, name):
	nice = 0
	mean = 0
	start(nice, mean, name)

	
>>> def lose(nice, mean, name):
	print("Ahh too bad, you lost!")
	again(nice, mean, name)

	
>>> 
============================================================== RESTART: C:/Users/samsp/Desktop/PyThOn/Nice_or_Mean(Runable).py =============================================================
>>> 
============================================================== RESTART: C:/Users/samsp/Desktop/PyThOn/Nice_or_Mean(Runable).py =============================================================

What is your name? 
>>>Samuel

Welcome Samuel

In this game, you will be greeted by 
many different people. You may choose to be 
nice or mean
but your actions will determine your fate

Samuel, your current total is: 
(0, Nice) and (0, Mean)

A stranger approaches you, 
are you nice?
or mean? (N/M) 
>>>N
walks away smiling

Samuel, your current total is: 
(1, Nice) and (0, Mean)

A stranger approaches you, 
are you nice?
or mean? (N/M) 
>>>N
walks away smiling

Samuel, your current total is: 
(2, Nice) and (0, Mean)

A stranger approaches you, 
are you nice?
or mean? (N/M) 
>>>N
walks away smiling

Nice job!

Do you want to play again? (y/n):
>>>y

Thank you for playing again, Samuel.

Samuel, your current total is: 
(0, Nice) and (0, Mean)

A stranger approaches you, 
are you nice?
or mean? (N/M) 
>>>
================================================================== RESTART: C:/Users/samsp/Desktop/PyThOn/NotesPage156.py ==================================================================
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> import os
>>> print(dir(os))
['DirEntry', 'F_OK', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_AddedDllDirectory', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_check_methods', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_putenv', '_unsetenv', '_wrap_close', 'abc', 'abort', 'access', 'add_dll_directory', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'urandom', 'utime', 'waitpid', 'walk', 'write']
>>> print(help(os))
Help on module os:

NAME
    os - OS routines for NT or Posix depending on what system we're on.

MODULE REFERENCE
    https://docs.python.org/3.8/library/os
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This exports:
      - all functions from posix or nt, e.g. unlink, stat, etc.
      - os.path is either posixpath or ntpath
      - os.name is either 'posix' or 'nt'
      - os.curdir is a string representing the current directory (always '.')
      - os.pardir is a string representing the parent directory (always '..')
      - os.sep is the (or a most common) pathname separator ('/' or '\\')
      - os.extsep is the extension separator (always '.')
      - os.altsep is the alternate pathname separator (None or '/')
      - os.pathsep is the component separator used in $PATH etc
      - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
      - os.defpath is the default search path for executables
      - os.devnull is the file path of the null device ('/dev/null', etc.)
    
    Programs that import and use 'os' stand a better chance of being
    portable between different platforms.  Of course, they must then
    only use functions that are defined by all platforms (e.g., unlink
    and opendir), and leave all pathname manipulation to os.path
    (e.g., split and join).

CLASSES
    builtins.Exception(builtins.BaseException)
        builtins.OSError
    builtins.object
        nt.DirEntry
    builtins.tuple(builtins.object)
        nt.times_result
        nt.uname_result
        stat_result
        statvfs_result
        terminal_size
    
    class DirEntry(builtins.object)
     |  Methods defined here:
     |  
     |  __fspath__(self, /)
     |      Returns the path for the entry.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  inode(self, /)
     |      Return inode of the entry; cached per entry.
     |  
     |  is_dir(self, /, *, follow_symlinks=True)
     |      Return True if the entry is a directory; cached per entry.
     |  
     |  is_file(self, /, *, follow_symlinks=True)
     |      Return True if the entry is a file; cached per entry.
     |  
     |  is_symlink(self, /)
     |      Return True if the entry is a symbolic link; cached per entry.
     |  
     |  stat(self, /, *, follow_symlinks=True)
     |      Return stat_result object for the entry; cached per entry.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  name
     |      the entry's base filename, relative to scandir() "path" argument
     |  
     |  path
     |      the entry's full path name; equivalent to os.path.join(scandir_path, entry.name)
    
    error = class OSError(Exception)
     |  Base class for I/O related errors.
     |  
     |  Method resolution order:
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Built-in subclasses:
     |      BlockingIOError
     |      ChildProcessError
     |      ConnectionError
     |      FileExistsError
     |      ... and 7 other subclasses
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class stat_result(builtins.tuple)
     |  stat_result(iterable=(), /)
     |  
     |  stat_result: Result from stat, fstat, or lstat.
     |  
     |  This object may be accessed either as a tuple of
     |    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
     |  or via the attributes st_mode, st_ino, st_dev, st_nlink, st_uid, and so on.
     |  
     |  Posix/windows: If your platform supports st_blksize, st_blocks, st_rdev,
     |  or st_flags, they are available as attributes only.
     |  
     |  See os.stat for more information.
     |  
     |  Method resolution order:
     |      stat_result
     |      builtins.tuple
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  st_atime
     |      time of last access
     |  
     |  st_atime_ns
     |      time of last access in nanoseconds
     |  
     |  st_ctime
     |      time of last change
     |  
     |  st_ctime_ns
     |      time of last change in nanoseconds
     |  
     |  st_dev
     |      device
     |  
     |  st_file_attributes
     |      Windows file attribute bits
     |  
     |  st_gid
     |      group ID of owner
     |  
     |  st_ino
     |      inode
     |  
     |  st_mode
     |      protection bits
     |  
     |  st_mtime
     |      time of last modification
     |  
     |  st_mtime_ns
     |      time of last modification in nanoseconds
     |  
     |  st_nlink
     |      number of hard links
     |  
     |  st_reparse_tag
     |      Windows reparse tag
     |  
     |  st_size
     |      total size, in bytes
     |  
     |  st_uid
     |      user ID of owner
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  n_fields = 18
     |  
     |  n_sequence_fields = 10
     |  
     |  n_unnamed_fields = 3
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __getnewargs__(self, /)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  count(self, value, /)
     |      Return number of occurrences of value.
     |  
     |  index(self, value, start=0, stop=9223372036854775807, /)
     |      Return first index of value.
     |      
     |      Raises ValueError if the value is not present.
    
    class statvfs_result(builtins.tuple)
     |  statvfs_result(iterable=(), /)
     |  
     |  statvfs_result: Result from statvfs or fstatvfs.
     |  
     |  This object may be accessed either as a tuple of
     |    (bsize, frsize, blocks, bfree, bavail, files, ffree, favail, flag, namemax),
     |  or via the attributes f_bsize, f_frsize, f_blocks, f_bfree, and so on.
     |  
     |  See os.statvfs for more information.
     |  
     |  Method resolution order:
     |      statvfs_result
     |      builtins.tuple
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  f_bavail
     |  
     |  f_bfree
     |  
     |  f_blocks
     |  
     |  f_bsize
     |  
     |  f_favail
     |  
     |  f_ffree
     |  
     |  f_files
     |  
     |  f_flag
     |  
     |  f_frsize
     |  
     |  f_fsid
     |  
     |  f_namemax
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  n_fields = 11
     |  
     |  n_sequence_fields = 10
     |  
     |  n_unnamed_fields = 0
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __getnewargs__(self, /)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  count(self, value, /)
     |      Return number of occurrences of value.
     |  
     |  index(self, value, start=0, stop=9223372036854775807, /)
     |      Return first index of value.
     |      
     |      Raises ValueError if the value is not present.
    
    class terminal_size(builtins.tuple)
     |  terminal_size(iterable=(), /)
     |  
     |  A tuple of (columns, lines) for holding terminal window size
     |  
     |  Method resolution order:
     |      terminal_size
     |      builtins.tuple
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  columns
     |      width of the terminal window in characters
     |  
     |  lines
     |      height of the terminal window in characters
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  n_fields = 2
     |  
     |  n_sequence_fields = 2
     |  
     |  n_unnamed_fields = 0
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __getnewargs__(self, /)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  count(self, value, /)
     |      Return number of occurrences of value.
     |  
     |  index(self, value, start=0, stop=9223372036854775807, /)
     |      Return first index of value.
     |      
     |      Raises ValueError if the value is not present.
    
    class times_result(builtins.tuple)
     |  times_result(iterable=(), /)
     |  
     |  times_result: Result from os.times().
     |  
     |  This object may be accessed either as a tuple of
     |    (user, system, children_user, children_system, elapsed),
     |  or via the attributes user, system, children_user, children_system,
     |  and elapsed.
     |  
     |  See os.times for more information.
     |  
     |  Method resolution order:
     |      times_result
     |      builtins.tuple
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  children_system
     |      system time of children
     |  
     |  children_user
     |      user time of children
     |  
     |  elapsed
     |      elapsed time since an arbitrary point in the past
     |  
     |  system
     |      system time
     |  
     |  user
     |      user time
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  n_fields = 5
     |  
     |  n_sequence_fields = 5
     |  
     |  n_unnamed_fields = 0
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __getnewargs__(self, /)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  count(self, value, /)
     |      Return number of occurrences of value.
     |  
     |  index(self, value, start=0, stop=9223372036854775807, /)
     |      Return first index of value.
     |      
     |      Raises ValueError if the value is not present.
    
    class uname_result(builtins.tuple)
     |  uname_result(iterable=(), /)
     |  
     |  uname_result: Result from os.uname().
     |  
     |  This object may be accessed either as a tuple of
     |    (sysname, nodename, release, version, machine),
     |  or via the attributes sysname, nodename, release, version, and machine.
     |  
     |  See os.uname for more information.
     |  
     |  Method resolution order:
     |      uname_result
     |      builtins.tuple
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  machine
     |      hardware identifier
     |  
     |  nodename
     |      name of machine on network (implementation-defined)
     |  
     |  release
     |      operating system release
     |  
     |  sysname
     |      operating system name
     |  
     |  version
     |      operating system version
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  n_fields = 5
     |  
     |  n_sequence_fields = 5
     |  
     |  n_unnamed_fields = 0
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __getnewargs__(self, /)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  count(self, value, /)
     |      Return number of occurrences of value.
     |  
     |  index(self, value, start=0, stop=9223372036854775807, /)
     |      Return first index of value.
     |      
     |      Raises ValueError if the value is not present.

FUNCTIONS
    _exit(status)
        Exit to the system with specified status, without normal exit processing.
    
    abort()
        Abort the interpreter immediately.
        
        This function 'dumps core' or otherwise fails in the hardest way possible
        on the hosting operating system.  This function never returns.
    
    access(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True)
        Use the real uid/gid to test for access to a path.
        
          path
            Path to be tested; can be string, bytes, or a path-like object.
          mode
            Operating-system mode bitfield.  Can be F_OK to test existence,
            or the inclusive-OR of R_OK, W_OK, and X_OK.
          dir_fd
            If not None, it should be a file descriptor open to a directory,
            and path should be relative; path will then be relative to that
            directory.
          effective_ids
            If True, access will use the effective uid/gid instead of
            the real uid/gid.
          follow_symlinks
            If False, and the last element of the path is a symbolic link,
            access will examine the symbolic link itself instead of the file
            the link points to.
        
        dir_fd, effective_ids, and follow_symlinks may not be implemented
          on your platform.  If they are unavailable, using them will raise a
          NotImplementedError.
        
        Note that most operations will use the effective uid/gid, therefore this
          routine can be used in a suid/sgid environment to test if the invoking user
          has the specified access to the path.
    
    chdir(path)
        Change the current working directory to the specified path.
        
        path may always be specified as a string.
        On some platforms, path may also be specified as an open file descriptor.
          If this functionality is unavailable, using it raises an exception.
    
    chmod(path, mode, *, dir_fd=None, follow_symlinks=True)
        Change the access permissions of a file.
        
          path
            Path to be modified.  May always be specified as a str, bytes, or a path-like object.
            On some platforms, path may also be specified as an open file descriptor.
            If this functionality is unavailable, using it raises an exception.
          mode
            Operating-system mode bitfield.
          dir_fd
            If not None, it should be a file descriptor open to a directory,
            and path should be relative; path will then be relative to that
            directory.
          follow_symlinks
            If False, and the last element of the path is a symbolic link,
            chmod will modify the symbolic link itself instead of the file
            the link points to.
        
        It is an error to use dir_fd or follow_symlinks when specifying path as
          an open file descriptor.
        dir_fd and follow_symlinks may not be implemented on your platform.
          If they are unavailable, using them will raise a NotImplementedError.
    
    close(fd)
        Close a file descriptor.
    
    closerange(fd_low, fd_high, /)
        Closes all file descriptors in [fd_low, fd_high), ignoring errors.
    
    cpu_count()
        Return the number of CPUs in the system; return None if indeterminable.
        
        This number is not equivalent to the number of CPUs the current process can
        use.  The number of usable CPUs can be obtained with
        ``len(os.sched_getaffinity(0))``
    
    device_encoding(fd)
        Return a string describing the encoding of a terminal's file descriptor.
        
        The file descriptor must be attached to a terminal.
        If the device is not a terminal, return None.
    
    dup(fd, /)
        Return a duplicate of a file descriptor.
    
    dup2(fd, fd2, inheritable=True)
        Duplicate file descriptor.
    
    execl(file, *args)
        execl(file, *args)
        
        Execute the executable file with argument list args, replacing the
        current process.
    
    execle(file, *args)
        execle(file, *args, env)
        
        Execute the executable file with argument list args and
        environment env, replacing the current process.
    
    execlp(file, *args)
        execlp(file, *args)
        
        Execute the executable file (which is searched for along $PATH)
        with argument list args, replacing the current process.
    
    execlpe(file, *args)
        execlpe(file, *args, env)
        
        Execute the executable file (which is searched for along $PATH)
        with argument list args and environment env, replacing the current
        process.
    
    execv(path, argv, /)
        Execute an executable path with arguments, replacing current process.
        
        path
          Path of executable file.
        argv
          Tuple or list of strings.
    
    execve(path, argv, env)
        Execute an executable path with arguments, replacing current process.
        
        path
          Path of executable file.
        argv
          Tuple or list of strings.
        env
          Dictionary of strings mapping to strings.
    
    execvp(file, args)
        execvp(file, args)
        
        Execute the executable file (which is searched for along $PATH)
        with argument list args, replacing the current process.
        args may be a list or tuple of strings.
    
    execvpe(file, args, env)
        execvpe(file, args, env)
        
        Execute the executable file (which is searched for along $PATH)
        with argument list args and environment env, replacing the
        current process.
        args may be a list or tuple of strings.
    
    fdopen(fd, *args, **kwargs)
        # Supply os.fdopen()
    
    fsdecode(filename)
        Decode filename (an os.PathLike, bytes, or str) from the filesystem
        encoding with 'surrogateescape' error handler, return str unchanged. On
        Windows, use 'strict' error handler if the file system encoding is
        'mbcs' (which is the default encoding).
    
    fsencode(filename)
        Encode filename (an os.PathLike, bytes, or str) to the filesystem
        encoding with 'surrogateescape' error handler, return bytes unchanged.
        On Windows, use 'strict' error handler if the file system encoding is
        'mbcs' (which is the default encoding).
    
    fspath(path)
        Return the file system path representation of the object.
        
        If the object is str or bytes, then allow it to pass through as-is. If the
        object defines __fspath__(), then return the result of that method. All other
        types raise a TypeError.
    
    fstat(fd)
        Perform a stat system call on the given file descriptor.
        
        Like stat(), but for an open file descriptor.
        Equivalent to os.stat(fd).
    
    fsync(fd)
        Force write of fd to disk.
    
    ftruncate(fd, length, /)
        Truncate a file, specified by file descriptor, to a specific length.
    
    get_exec_path(env=None)
        Returns the sequence of directories that will be searched for the
        named executable (similar to a shell) when launching a process.
        
        *env* must be an environment variable dict or None.  If *env* is None,
        os.environ will be used.
    
    get_handle_inheritable(handle, /)
        Get the close-on-exe flag of the specified file descriptor.
    
    get_inheritable(fd, /)
        Get the close-on-exe flag of the specified file descriptor.
    
    get_terminal_size(...)
        Return the size of the terminal window as (columns, lines).
        
        The optional argument fd (default standard output) specifies
        which file descriptor should be queried.
        
        If the file descriptor is not connected to a terminal, an OSError
        is thrown.
        
        This function will only be defined if an implementation is
        available for this system.
        
        shutil.get_terminal_size is the high-level function which should
        normally be used, os.get_terminal_size is the low-level implementation.
    
    getcwd()
        Return a unicode string representing the current working directory.
    
    getcwdb()
        Return a bytes string representing the current working directory.
    
    getenv(key, default=None)
        Get an environment variable, return None if it doesn't exist.
        The optional second argument can specify an alternate default.
        key, default and the result are str.
    
    getlogin()
        Return the actual login name.
    
    getpid()
        Return the current process id.
    
    getppid()
        Return the parent's process id.
        
        If the parent process has already exited, Windows machines will still
        return its id; others systems will return the id of the 'init' process (1).
    
    isatty(fd, /)
        Return True if the fd is connected to a terminal.
        
        Return True if the file descriptor is an open file descriptor
        connected to the slave end of a terminal.
    
    kill(pid, signal, /)
        Kill a process with a signal.
    
    link(src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True)
        Create a hard link to a file.
        
        If either src_dir_fd or dst_dir_fd is not None, it should be a file
          descriptor open to a directory, and the respective path string (src or dst)
          should be relative; the path will then be relative to that directory.
        If follow_symlinks is False, and the last element of src is a symbolic
          link, link will create a link to the symbolic link itself instead of the
          file the link points to.
        src_dir_fd, dst_dir_fd, and follow_symlinks may not be implemented on your
          platform.  If they are unavailable, using them will raise a
          NotImplementedError.
    
    listdir(path=None)
        Return a list containing the names of the files in the directory.
        
        path can be specified as either str, bytes, or a path-like object.  If path is bytes,
          the filenames returned will also be bytes; in all other circumstances
          the filenames returned will be str.
        If path is None, uses the path='.'.
        On some platforms, path may also be specified as an open file descriptor;\
          the file descriptor must refer to a directory.
          If this functionality is unavailable, using it raises NotImplementedError.
        
        The list is in arbitrary order.  It does not include the special
        entries '.' and '..' even if they are present in the directory.
    
    lseek(fd, position, how, /)
        Set the position of a file descriptor.  Return the new position.
        
        Return the new cursor position in number of bytes
        relative to the beginning of the file.
    
    lstat(path, *, dir_fd=None)
        Perform a stat system call on the given path, without following symbolic links.
        
        Like stat(), but do not follow symbolic links.
        Equivalent to stat(path, follow_symlinks=False).
    
    makedirs(name, mode=511, exist_ok=False)
        makedirs(name [, mode=0o777][, exist_ok=False])
        
        Super-mkdir; create a leaf directory and all intermediate ones.  Works like
        mkdir, except that any intermediate path segment (not just the rightmost)
        will be created if it does not exist. If the target directory already
        exists, raise an OSError if exist_ok is False. Otherwise no exception is
        raised.  This is recursive.
    
    mkdir(path, mode=511, *, dir_fd=None)
        Create a directory.
        
        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.
        
        The mode argument is ignored on Windows.
    
    open(path, flags, mode=511, *, dir_fd=None)
        Open a file for low level IO.  Returns a file descriptor (integer).
        
        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.
    
    pipe()
        Create a pipe.
        
        Returns a tuple of two file descriptors:
          (read_fd, write_fd)
    
    popen(cmd, mode='r', buffering=-1)
        # Supply os.popen()
    
    putenv(name, value, /)
        Change or add an environment variable.
    
    read(fd, length, /)
        Read from a file descriptor.  Returns a bytes object.
    
    readlink(path, *, dir_fd=None)
        Return a string representing the path to which the symbolic link points.
        
        If dir_fd is not None, it should be a file descriptor open to a directory,
        and path should be relative; path will then be relative to that directory.
        
        dir_fd may not be implemented on your platform.  If it is unavailable,
        using it will raise a NotImplementedError.
    
    remove(path, *, dir_fd=None)
        Remove a file (same as unlink()).
        
        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.
    
    removedirs(name)
        removedirs(name)
        
        Super-rmdir; remove a leaf directory and all empty intermediate
        ones.  Works like rmdir except that, if the leaf directory is
        successfully removed, directories corresponding to rightmost path
        segments will be pruned away until either the whole path is
        consumed or an error occurs.  Errors during this latter phase are
        ignored -- they generally mean that a directory was not empty.
    
    rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
        Rename a file or directory.
        
        If either src_dir_fd or dst_dir_fd is not None, it should be a file
          descriptor open to a directory, and the respective path string (src or dst)
          should be relative; the path will then be relative to that directory.
        src_dir_fd and dst_dir_fd, may not be implemented on your platform.
          If they are unavailable, using them will raise a NotImplementedError.
    
    renames(old, new)
        renames(old, new)
        
        Super-rename; create directories as necessary and delete any left
        empty.  Works like rename, except creation of any intermediate
        directories needed to make the new pathname good is attempted
        first.  After the rename, directories corresponding to rightmost
        path segments of the old name will be pruned until either the
        whole path is consumed or a nonempty directory is found.
        
        Note: this function can fail with the new directory structure made
        if you lack permissions needed to unlink the leaf directory or
        file.
    
    replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
        Rename a file or directory, overwriting the destination.
        
        If either src_dir_fd or dst_dir_fd is not None, it should be a file
          descriptor open to a directory, and the respective path string (src or dst)
          should be relative; the path will then be relative to that directory.
        src_dir_fd and dst_dir_fd, may not be implemented on your platform.
          If they are unavailable, using them will raise a NotImplementedError.
    
    rmdir(path, *, dir_fd=None)
        Remove a directory.
        
        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.
    
    scandir(path=None)
        Return an iterator of DirEntry objects for given path.
        
        path can be specified as either str, bytes, or a path-like object.  If path
        is bytes, the names of yielded DirEntry objects will also be bytes; in
        all other circumstances they will be str.
        
        If path is None, uses the path='.'.
    
    set_handle_inheritable(handle, inheritable, /)
        Set the inheritable flag of the specified handle.
    
    set_inheritable(fd, inheritable, /)
        Set the inheritable flag of the specified file descriptor.
    
    spawnl(mode, file, *args)
        spawnl(mode, file, *args) -> integer
        
        Execute file with arguments from args in a subprocess.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it.
    
    spawnle(mode, file, *args)
        spawnle(mode, file, *args, env) -> integer
        
        Execute file with arguments from args in a subprocess with the
        supplied environment.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it.
    
    spawnv(mode, path, argv, /)
        Execute the program specified by path in a new process.
        
        mode
          Mode of process creation.
        path
          Path of executable file.
        argv
          Tuple or list of strings.
    
    spawnve(mode, path, argv, env, /)
        Execute the program specified by path in a new process.
        
        mode
          Mode of process creation.
        path
          Path of executable file.
        argv
          Tuple or list of strings.
        env
          Dictionary of strings mapping to strings.
    
    startfile(...)
        Start a file with its associated application.
        
        When "operation" is not specified or "open", this acts like
        double-clicking the file in Explorer, or giving the file name as an
        argument to the DOS "start" command: the file is opened with whatever
        application (if any) its extension is associated.
        When another "operation" is given, it specifies what should be done with
        the file.  A typical operation is "print".
        
        startfile returns as soon as the associated application is launched.
        There is no option to wait for the application to close, and no way
        to retrieve the application's exit status.
        
        The filepath is relative to the current directory.  If you want to use
        an absolute path, make sure the first character is not a slash ("/");
        the underlying Win32 ShellExecute function doesn't work if it is.
    
    stat(path, *, dir_fd=None, follow_symlinks=True)
        Perform a stat system call on the given path.
        
          path
            Path to be examined; can be string, bytes, a path-like object or
            open-file-descriptor int.
          dir_fd
            If not None, it should be a file descriptor open to a directory,
            and path should be a relative string; path will then be relative to
            that directory.
          follow_symlinks
            If False, and the last element of the path is a symbolic link,
            stat will examine the symbolic link itself instead of the file
            the link points to.
        
        dir_fd and follow_symlinks may not be implemented
          on your platform.  If they are unavailable, using them will raise a
          NotImplementedError.
        
        It's an error to use dir_fd or follow_symlinks when specifying path as
          an open file descriptor.
    
    strerror(code, /)
        Translate an error code to a message string.
    
    symlink(src, dst, target_is_directory=False, *, dir_fd=None)
        Create a symbolic link pointing to src named dst.
        
        target_is_directory is required on Windows if the target is to be
          interpreted as a directory.  (On Windows, symlink requires
          Windows 6.0 or greater, and raises a NotImplementedError otherwise.)
          target_is_directory is ignored on non-Windows platforms.
        
        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.
    
    system(command)
        Execute the command in a subshell.
    
    times()
        Return a collection containing process timing information.
        
        The object returned behaves like a named tuple with these fields:
          (utime, stime, cutime, cstime, elapsed_time)
        All fields are floating point numbers.
    
    truncate(path, length)
        Truncate a file, specified by path, to a specific length.
        
        On some platforms, path may also be specified as an open file descriptor.
          If this functionality is unavailable, using it raises an exception.
    
    umask(mask, /)
        Set the current numeric umask and return the previous umask.
    
    unlink(path, *, dir_fd=None)
        Remove a file (same as remove()).
        
        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.
    
    urandom(size, /)
        Return a bytes object containing random bytes suitable for cryptographic use.
    
    utime(...)
        Set the access and modified time of path.
        
        path may always be specified as a string.
        On some platforms, path may also be specified as an open file descriptor.
          If this functionality is unavailable, using it raises an exception.
        
        If times is not None, it must be a tuple (atime, mtime);
            atime and mtime should be expressed as float seconds since the epoch.
        If ns is specified, it must be a tuple (atime_ns, mtime_ns);
            atime_ns and mtime_ns should be expressed as integer nanoseconds
            since the epoch.
        If times is None and ns is unspecified, utime uses the current time.
        Specifying tuples for both times and ns is an error.
        
        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        If follow_symlinks is False, and the last element of the path is a symbolic
          link, utime will modify the symbolic link itself instead of the file the
          link points to.
        It is an error to use dir_fd or follow_symlinks when specifying path
          as an open file descriptor.
        dir_fd and follow_symlinks may not be available on your platform.
          If they are unavailable, using them will raise a NotImplementedError.
    
    waitpid(pid, options, /)
        Wait for completion of a given process.
        
        Returns a tuple of information regarding the process:
            (pid, status << 8)
        
        The options argument is ignored on Windows.
    
    walk(top, topdown=True, onerror=None, followlinks=False)
        Directory tree generator.
        
        For each directory in the directory tree rooted at top (including top
        itself, but excluding '.' and '..'), yields a 3-tuple
        
            dirpath, dirnames, filenames
        
        dirpath is a string, the path to the directory.  dirnames is a list of
        the names of the subdirectories in dirpath (excluding '.' and '..').
        filenames is a list of the names of the non-directory files in dirpath.
        Note that the names in the lists are just names, with no path components.
        To get a full path (which begins with top) to a file or directory in
        dirpath, do os.path.join(dirpath, name).
        
        If optional arg 'topdown' is true or not specified, the triple for a
        directory is generated before the triples for any of its subdirectories
        (directories are generated top down).  If topdown is false, the triple
        for a directory is generated after the triples for all of its
        subdirectories (directories are generated bottom up).
        
        When topdown is true, the caller can modify the dirnames list in-place
        (e.g., via del or slice assignment), and walk will only recurse into the
        subdirectories whose names remain in dirnames; this can be used to prune the
        search, or to impose a specific order of visiting.  Modifying dirnames when
        topdown is false has no effect on the behavior of os.walk(), since the
        directories in dirnames have already been generated by the time dirnames
        itself is generated. No matter the value of topdown, the list of
        subdirectories is retrieved before the tuples for the directory and its
        subdirectories are generated.
        
        By default errors from the os.scandir() call are ignored.  If
        optional arg 'onerror' is specified, it should be a function; it
        will be called with one argument, an OSError instance.  It can
        report the error to continue with the walk, or raise the exception
        to abort the walk.  Note that the filename is available as the
        filename attribute of the exception object.
        
        By default, os.walk does not follow symbolic links to subdirectories on
        systems that support them.  In order to get this functionality, set the
        optional argument 'followlinks' to true.
        
        Caution:  if you pass a relative pathname for top, don't change the
        current working directory between resumptions of walk.  walk never
        changes the current directory, and assumes that the client doesn't
        either.
        
        Example:
        
        import os
        from os.path import join, getsize
        for root, dirs, files in os.walk('python/Lib/email'):
            print(root, "consumes", end="")
            print(sum(getsize(join(root, name)) for name in files), end="")
            print("bytes in", len(files), "non-directory files")
            if 'CVS' in dirs:
                dirs.remove('CVS')  # don't visit CVS directories
    
    write(fd, data, /)
        Write a bytes object to a file descriptor.

DATA
    F_OK = 0
    O_APPEND = 8
    O_BINARY = 32768
    O_CREAT = 256
    O_EXCL = 1024
    O_NOINHERIT = 128
    O_RANDOM = 16
    O_RDONLY = 0
    O_RDWR = 2
    O_SEQUENTIAL = 32
    O_SHORT_LIVED = 4096
    O_TEMPORARY = 64
    O_TEXT = 16384
    O_TRUNC = 512
    O_WRONLY = 1
    P_DETACH = 4
    P_NOWAIT = 1
    P_NOWAITO = 3
    P_OVERLAY = 2
    P_WAIT = 0
    R_OK = 4
    SEEK_CUR = 1
    SEEK_END = 2
    SEEK_SET = 0
    TMP_MAX = 2147483647
    W_OK = 2
    X_OK = 1
    __all__ = ['altsep', 'curdir', 'pardir', 'sep', 'pathsep', 'linesep', ...
    altsep = '/'
    curdir = '.'
    defpath = r'.;C:\bin'
    devnull = 'nul'
    environ = environ({'ALLUSERSPROFILE': 'C:\\ProgramData', '...E': 'C:\\...
    extsep = '.'
    linesep = '\r\n'
    name = 'nt'
    pardir = '..'
    pathsep = ';'
    sep = r'\'
    supports_bytes_environ = False

FILE
    c:\users\samsp\appdata\local\programs\python\python38\lib\os.py


None
>>> 
============== RESTART: C:/Users/samsp/Desktop/PROFESSIONAL PORTFOLIO/Python-Projects/Test.py =============
C:\Users\samsp\Desktop\PROFESSIONAL PORTFOLIO\Python-Projects
>>> print(help(open))
Help on built-in function open in module io:

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    Open file and return a stream.  Raise OSError upon failure.
    
    file is either a text or byte string giving the name (and the path
    if the file isn't in the current working directory) of the file to
    be opened or an integer file descriptor of the file to be
    wrapped. (If a file descriptor is given, it is closed when the
    returned I/O object is closed, unless closefd is set to False.)
    
    mode is an optional string that specifies the mode in which the file
    is opened. It defaults to 'r' which means open for reading in text
    mode.  Other common values are 'w' for writing (truncating the file if
    it already exists), 'x' for creating and writing to a new file, and
    'a' for appending (which on some Unix systems, means that all writes
    append to the end of the file regardless of the current seek position).
    In text mode, if encoding is not specified the encoding used is platform
    dependent: locale.getpreferredencoding(False) is called to get the
    current locale encoding. (For reading and writing raw bytes use binary
    mode and leave encoding unspecified.) The available modes are:
    
    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================
    
    The default mode is 'rt' (open for reading text). For binary random
    access, the mode 'w+b' opens and truncates the file to 0 bytes, while
    'r+b' opens the file without truncation. The 'x' mode implies 'w' and
    raises an `FileExistsError` if the file already exists.
    
    Python distinguishes between files opened in binary and text modes,
    even when the underlying operating system doesn't. Files opened in
    binary mode (appending 'b' to the mode argument) return contents as
    bytes objects without any decoding. In text mode (the default, or when
    't' is appended to the mode argument), the contents of the file are
    returned as strings, the bytes having been first decoded using a
    platform-dependent encoding or using the specified encoding if given.
    
    'U' mode is deprecated and will raise an exception in future versions
    of Python.  It has no effect in Python 3.  Use newline to control
    universal newlines mode.
    
    buffering is an optional integer used to set the buffering policy.
    Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
    line buffering (only usable in text mode), and an integer > 1 to indicate
    the size of a fixed-size chunk buffer.  When no buffering argument is
    given, the default buffering policy works as follows:
    
    * Binary files are buffered in fixed-size chunks; the size of the buffer
      is chosen using a heuristic trying to determine the underlying device's
      "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.
      On many systems, the buffer will typically be 4096 or 8192 bytes long.
    
    * "Interactive" text files (files for which isatty() returns True)
      use line buffering.  Other text files use the policy described above
      for binary files.
    
    encoding is the name of the encoding used to decode or encode the
    file. This should only be used in text mode. The default encoding is
    platform dependent, but any encoding supported by Python can be
    passed.  See the codecs module for the list of supported encodings.
    
    errors is an optional string that specifies how encoding errors are to
    be handled---this argument should not be used in binary mode. Pass
    'strict' to raise a ValueError exception if there is an encoding error
    (the default of None has the same effect), or pass 'ignore' to ignore
    errors. (Note that ignoring encoding errors can lead to data loss.)
    See the documentation for codecs.register or run 'help(codecs.Codec)'
    for a list of the permitted encoding error strings.
    
    newline controls how universal newlines works (it only applies to text
    mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as
    follows:
    
    * On input, if newline is None, universal newlines mode is
      enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
      these are translated into '\n' before being returned to the
      caller. If it is '', universal newline mode is enabled, but line
      endings are returned to the caller untranslated. If it has any of
      the other legal values, input lines are only terminated by the given
      string, and the line ending is returned to the caller untranslated.
    
    * On output, if newline is None, any '\n' characters written are
      translated to the system default line separator, os.linesep. If
      newline is '' or '\n', no translation takes place. If newline is any
      of the other legal values, any '\n' characters written are translated
      to the given string.
    
    If closefd is False, the underlying file descriptor will be kept open
    when the file is closed. This does not work when a file name is given
    and must be True in that case.
    
    A custom opener can be used by passing a callable as *opener*. The
    underlying file descriptor for the file object is then obtained by
    calling *opener* with (*file*, *flags*). *opener* must return an open
    file descriptor (passing os.open as *opener* results in functionality
    similar to passing None).
    
    open() returns a file object whose type depends on the mode, and
    through which the standard file operations such as reading and writing
    are performed. When open() is used to open a file in a text mode ('w',
    'r', 'wt', 'rt', etc.), it returns a TextIOWrapper. When used to open
    a file in a binary mode, the returned class varies: in read binary
    mode, it returns a BufferedReader; in write binary and append binary
    modes, it returns a BufferedWriter, and in read/write mode, it returns
    a BufferedRandom.
    
    It is also possible to use a string or bytearray as a file for both
    reading and writing. For strings StringIO can be used like a file
    opened in a text mode, and for bytes a BytesIO can be used like a file
    opened in a binary mode.

None
>>> 
============== RESTART: C:/Users/samsp/Desktop/PROFESSIONAL PORTFOLIO/Python-Projects/Test.py =============
Hello World!
>>> 
============== RESTART: C:/Users/samsp/Desktop/PROFESSIONAL PORTFOLIO/Python-Projects/Test.py =============
Hello World!
I love Python!
>>> 
============= RESTART: C:/Users/samsp/Desktop/PROFESSIONAL PORTFOLIO/Python-Projects/FiloIO.py ============
C:\A\Hello
>>> 
============= RESTART: C:/Users/samsp/Desktop/PROFESSIONAL PORTFOLIO/Python-Projects/FiloIO.py ============
C:\A\Hello.txt
>>> print(help(listdir()))
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    print(help(listdir()))
NameError: name 'listdir' is not defined
>>> 
======== RESTART: C:/Users/samsp/Desktop/PROFESSIONAL PORTFOLIO/Python-Projects/AssignmentScript.py =======
C:\A\Hello.txt
C:\A\NewFile.txt
>>> 
======== RESTART: C:/Users/samsp/Desktop/PROFESSIONAL PORTFOLIO/Python-Projects/AssignmentScript.py =======
C:\A\Hello.txt
C:\A\NewFile.txt
Traceback (most recent call last):
  File "C:/Users/samsp/Desktop/PROFESSIONAL PORTFOLIO/Python-Projects/AssignmentScript.py", line 14, in <module>
    print(os.path.getmtime(dirloc, file))
TypeError: getmtime() takes 1 positional argument but 2 were given
>>> 
======== RESTART: C:/Users/samsp/Desktop/PROFESSIONAL PORTFOLIO/Python-Projects/AssignmentScript.py =======
C:\A\Hello.txt
C:\A\NewFile.txt
Traceback (most recent call last):
  File "C:/Users/samsp/Desktop/PROFESSIONAL PORTFOLIO/Python-Projects/AssignmentScript.py", line 14, in <module>
    print(os.path.getmtime(file))
  File "C:\Users\samsp\AppData\Local\Programs\Python\Python38\lib\genericpath.py", line 55, in getmtime
    return os.stat(filename).st_mtime
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'Hello.txt'
>>> 
======== RESTART: C:/Users/samsp/Desktop/PROFESSIONAL PORTFOLIO/Python-Projects/AssignmentScript.py =======
C:\A\Hello.txt
C:\A\NewFile.txt
Traceback (most recent call last):
  File "C:/Users/samsp/Desktop/PROFESSIONAL PORTFOLIO/Python-Projects/AssignmentScript.py", line 14, in <module>
    print(os.path.getmtime(file))
  File "C:\Users\samsp\AppData\Local\Programs\Python\Python38\lib\genericpath.py", line 55, in getmtime
    return os.stat(filename).st_mtime
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'Hello.txt'
>>> 
======== RESTART: C:/Users/samsp/Desktop/PROFESSIONAL PORTFOLIO/Python-Projects/AssignmentScript.py =======
C:\A\Hello.txt
C:\A\NewFile.txt
Traceback (most recent call last):
  File "C:/Users/samsp/Desktop/PROFESSIONAL PORTFOLIO/Python-Projects/AssignmentScript.py", line 14, in <module>
    print(os.path.getmtime(file))
  File "C:\Users\samsp\AppData\Local\Programs\Python\Python38\lib\genericpath.py", line 55, in getmtime
    return os.stat(filename).st_mtime
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'Hello.txt'
>>> 
======== RESTART: C:/Users/samsp/Desktop/PROFESSIONAL PORTFOLIO/Python-Projects/AssignmentScript.py =======
C:\A\Hello.txt
C:\A\NewFile.txt
Traceback (most recent call last):
  File "C:/Users/samsp/Desktop/PROFESSIONAL PORTFOLIO/Python-Projects/AssignmentScript.py", line 14, in <module>
    print(os.path.getmtime(file))
  File "C:\Users\samsp\AppData\Local\Programs\Python\Python38\lib\genericpath.py", line 55, in getmtime
    return os.stat(filename).st_mtime
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'Hello.txt'
>>> 
======== RESTART: C:/Users/samsp/Desktop/PROFESSIONAL PORTFOLIO/Python-Projects/AssignmentScript.py =======
Traceback (most recent call last):
  File "C:/Users/samsp/Desktop/PROFESSIONAL PORTFOLIO/Python-Projects/AssignmentScript.py", line 10, in <module>
    print(os.path.getmtime(file))
  File "C:\Users\samsp\AppData\Local\Programs\Python\Python38\lib\genericpath.py", line 55, in getmtime
    return os.stat(filename).st_mtime
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'Hello.txt'
>>> 
======== RESTART: C:/Users/samsp/Desktop/PROFESSIONAL PORTFOLIO/Python-Projects/AssignmentScript.py =======
C:\A\Hello.txt
C:\A\NewFile.txt
Traceback (most recent call last):
  File "C:/Users/samsp/Desktop/PROFESSIONAL PORTFOLIO/Python-Projects/AssignmentScript.py", line 14, in <module>
    print(os.path.getmtime(file))
  File "C:\Users\samsp\AppData\Local\Programs\Python\Python38\lib\genericpath.py", line 55, in getmtime
    return os.stat(filename).st_mtime
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'Hello.txt'
>>> import sqlite3
>>> print(dir(sqlite3))
['Binary', 'Connection', 'Cursor', 'DataError', 'DatabaseError', 'Date', 'DateFromTicks', 'Error', 'IntegrityError', 'InterfaceError', 'InternalError', 'NotSupportedError', 'OperationalError', 'OptimizedUnicode', 'PARSE_COLNAMES', 'PARSE_DECLTYPES', 'PrepareProtocol', 'ProgrammingError', 'Row', 'SQLITE_ALTER_TABLE', 'SQLITE_ANALYZE', 'SQLITE_ATTACH', 'SQLITE_CREATE_INDEX', 'SQLITE_CREATE_TABLE', 'SQLITE_CREATE_TEMP_INDEX', 'SQLITE_CREATE_TEMP_TABLE', 'SQLITE_CREATE_TEMP_TRIGGER', 'SQLITE_CREATE_TEMP_VIEW', 'SQLITE_CREATE_TRIGGER', 'SQLITE_CREATE_VIEW', 'SQLITE_CREATE_VTABLE', 'SQLITE_DELETE', 'SQLITE_DENY', 'SQLITE_DETACH', 'SQLITE_DONE', 'SQLITE_DROP_INDEX', 'SQLITE_DROP_TABLE', 'SQLITE_DROP_TEMP_INDEX', 'SQLITE_DROP_TEMP_TABLE', 'SQLITE_DROP_TEMP_TRIGGER', 'SQLITE_DROP_TEMP_VIEW', 'SQLITE_DROP_TRIGGER', 'SQLITE_DROP_VIEW', 'SQLITE_DROP_VTABLE', 'SQLITE_FUNCTION', 'SQLITE_IGNORE', 'SQLITE_INSERT', 'SQLITE_OK', 'SQLITE_PRAGMA', 'SQLITE_READ', 'SQLITE_RECURSIVE', 'SQLITE_REINDEX', 'SQLITE_SAVEPOINT', 'SQLITE_SELECT', 'SQLITE_TRANSACTION', 'SQLITE_UPDATE', 'Time', 'TimeFromTicks', 'Timestamp', 'TimestampFromTicks', 'Warning', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'adapt', 'adapters', 'apilevel', 'collections', 'complete_statement', 'connect', 'converters', 'datetime', 'dbapi2', 'enable_callback_tracebacks', 'enable_shared_cache', 'paramstyle', 'register_adapter', 'register_converter', 'sqlite_version', 'sqlite_version_info', 'threadsafety', 'time', 'version', 'version_info']
>>> print(help(sqlite3))
Help on package sqlite3:

NAME
    sqlite3

MODULE REFERENCE
    https://docs.python.org/3.8/library/sqlite3
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    # pysqlite2/__init__.py: the pysqlite2 package.
    #
    # Copyright (C) 2005 Gerhard Häring <gh@ghaering.de>
    #
    # This file is part of pysqlite.
    #
    # This software is provided 'as-is', without any express or implied
    # warranty.  In no event will the authors be held liable for any damages
    # arising from the use of this software.
    #
    # Permission is granted to anyone to use this software for any purpose,
    # including commercial applications, and to alter it and redistribute it
    # freely, subject to the following restrictions:
    #
    # 1. The origin of this software must not be misrepresented; you must not
    #    claim that you wrote the original software. If you use this software
    #    in a product, an acknowledgment in the product documentation would be
    #    appreciated but is not required.
    # 2. Altered source versions must be plainly marked as such, and must not be
    #    misrepresented as being the original software.
    # 3. This notice may not be removed or altered from any source distribution.

PACKAGE CONTENTS
    dbapi2
    dump
    test (package)

CLASSES
    builtins.Exception(builtins.BaseException)
        Error
            DatabaseError
                DataError
                IntegrityError
                InternalError
                NotSupportedError
                OperationalError
                ProgrammingError
            InterfaceError
        Warning
    builtins.object
        Connection
        Cursor
        PrepareProtocol
        Row
    
    class Connection(builtins.object)
     |  SQLite database connection object.
     |  
     |  Methods defined here:
     |  
     |  __call__(self, /, *args, **kwargs)
     |      Call self as a function.
     |  
     |  __enter__(...)
     |      For context manager. Non-standard.
     |  
     |  __exit__(...)
     |      For context manager. Non-standard.
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  backup(...)
     |      Makes a backup of the database. Non-standard.
     |  
     |  close(...)
     |      Closes the connection.
     |  
     |  commit(...)
     |      Commit the current transaction.
     |  
     |  create_aggregate(...)
     |      Creates a new aggregate. Non-standard.
     |  
     |  create_collation(...)
     |      Creates a collation function. Non-standard.
     |  
     |  create_function(...)
     |      Creates a new function. Non-standard.
     |  
     |  cursor(...)
     |      Return a cursor for the connection.
     |  
     |  enable_load_extension(...)
     |      Enable dynamic loading of SQLite extension modules. Non-standard.
     |  
     |  execute(...)
     |      Executes a SQL statement. Non-standard.
     |  
     |  executemany(...)
     |      Repeatedly executes a SQL statement. Non-standard.
     |  
     |  executescript(...)
     |      Executes a multiple SQL statements at once. Non-standard.
     |  
     |  interrupt(...)
     |      Abort any pending database operation. Non-standard.
     |  
     |  iterdump(...)
     |      Returns iterator to the dump of the database in an SQL text format. Non-standard.
     |  
     |  load_extension(...)
     |      Load SQLite extension module. Non-standard.
     |  
     |  rollback(...)
     |      Roll back the current transaction.
     |  
     |  set_authorizer(...)
     |      Sets authorizer callback. Non-standard.
     |  
     |  set_progress_handler(...)
     |      Sets progress handler callback. Non-standard.
     |  
     |  set_trace_callback(...)
     |      Sets a trace callback called for each SQL statement (passed as unicode). Non-standard.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  DataError
     |  
     |  DatabaseError
     |  
     |  Error
     |  
     |  IntegrityError
     |  
     |  InterfaceError
     |  
     |  InternalError
     |  
     |  NotSupportedError
     |  
     |  OperationalError
     |  
     |  ProgrammingError
     |  
     |  Warning
     |  
     |  in_transaction
     |  
     |  isolation_level
     |  
     |  row_factory
     |  
     |  text_factory
     |  
     |  total_changes
    
    class Cursor(builtins.object)
     |  SQLite database cursor class.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __next__(self, /)
     |      Implement next(self).
     |  
     |  close(...)
     |      Closes the cursor.
     |  
     |  execute(...)
     |      Executes a SQL statement.
     |  
     |  executemany(...)
     |      Repeatedly executes a SQL statement.
     |  
     |  executescript(...)
     |      Executes a multiple SQL statements at once. Non-standard.
     |  
     |  fetchall(...)
     |      Fetches all rows from the resultset.
     |  
     |  fetchmany(...)
     |      Fetches several rows from the resultset.
     |  
     |  fetchone(...)
     |      Fetches one row from the resultset.
     |  
     |  setinputsizes(...)
     |      Required by DB-API. Does nothing in pysqlite.
     |  
     |  setoutputsize(...)
     |      Required by DB-API. Does nothing in pysqlite.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  arraysize
     |  
     |  connection
     |  
     |  description
     |  
     |  lastrowid
     |  
     |  row_factory
     |  
     |  rowcount
    
    class DataError(DatabaseError)
     |  Common base class for all non-exit exceptions.
     |  
     |  Method resolution order:
     |      DataError
     |      DatabaseError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Data descriptors inherited from Error:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class DatabaseError(Error)
     |  Common base class for all non-exit exceptions.
     |  
     |  Method resolution order:
     |      DatabaseError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Data descriptors inherited from Error:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class Error(builtins.Exception)
     |  Common base class for all non-exit exceptions.
     |  
     |  Method resolution order:
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class IntegrityError(DatabaseError)
     |  Common base class for all non-exit exceptions.
     |  
     |  Method resolution order:
     |      IntegrityError
     |      DatabaseError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Data descriptors inherited from Error:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class InterfaceError(Error)
     |  Common base class for all non-exit exceptions.
     |  
     |  Method resolution order:
     |      InterfaceError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Data descriptors inherited from Error:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class InternalError(DatabaseError)
     |  Common base class for all non-exit exceptions.
     |  
     |  Method resolution order:
     |      InternalError
     |      DatabaseError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Data descriptors inherited from Error:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class NotSupportedError(DatabaseError)
     |  Common base class for all non-exit exceptions.
     |  
     |  Method resolution order:
     |      NotSupportedError
     |      DatabaseError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Data descriptors inherited from Error:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class OperationalError(DatabaseError)
     |  Common base class for all non-exit exceptions.
     |  
     |  Method resolution order:
     |      OperationalError
     |      DatabaseError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Data descriptors inherited from Error:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class PrepareProtocol(builtins.object)
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
    
    class ProgrammingError(DatabaseError)
     |  Common base class for all non-exit exceptions.
     |  
     |  Method resolution order:
     |      ProgrammingError
     |      DatabaseError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Data descriptors inherited from Error:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class Row(builtins.object)
     |  Methods defined here:
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  keys(...)
     |      Returns the keys of the row.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
    
    class Warning(builtins.Exception)
     |  Common base class for all non-exit exceptions.
     |  
     |  Method resolution order:
     |      Warning
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args

FUNCTIONS
    adapt(...)
        adapt(obj, protocol, alternate) -> adapt obj to given protocol. Non-standard.
    
    complete_statement(...)
        complete_statement(sql)
        
        Checks if a string contains a complete SQL statement. Non-standard.
    
    connect(...)
        connect(database[, timeout, detect_types, isolation_level,
                check_same_thread, factory, cached_statements, uri])
        
        Opens a connection to the SQLite database file *database*. You can use
        ":memory:" to open a database connection to a database that resides in
        RAM instead of on disk.
    
    enable_callback_tracebacks(...)
        enable_callback_tracebacks(flag)
        
        Enable or disable callback functions throwing errors to stderr.
    
    enable_shared_cache(...)
        enable_shared_cache(do_enable)
        
        Enable or disable shared cache mode for the calling thread.
        Experimental/Non-standard.
    
    register_adapter(...)
        register_adapter(type, callable)
        
        Registers an adapter with pysqlite's adapter registry. Non-standard.
    
    register_converter(...)
        register_converter(typename, callable)
        
        Registers a converter with pysqlite. Non-standard.

DATA
    PARSE_COLNAMES = 2
    PARSE_DECLTYPES = 1
    SQLITE_ALTER_TABLE = 26
    SQLITE_ANALYZE = 28
    SQLITE_ATTACH = 24
    SQLITE_CREATE_INDEX = 1
    SQLITE_CREATE_TABLE = 2
    SQLITE_CREATE_TEMP_INDEX = 3
    SQLITE_CREATE_TEMP_TABLE = 4
    SQLITE_CREATE_TEMP_TRIGGER = 5
    SQLITE_CREATE_TEMP_VIEW = 6
    SQLITE_CREATE_TRIGGER = 7
    SQLITE_CREATE_VIEW = 8
    SQLITE_CREATE_VTABLE = 29
    SQLITE_DELETE = 9
    SQLITE_DENY = 1
    SQLITE_DETACH = 25
    SQLITE_DONE = 101
    SQLITE_DROP_INDEX = 10
    SQLITE_DROP_TABLE = 11
    SQLITE_DROP_TEMP_INDEX = 12
    SQLITE_DROP_TEMP_TABLE = 13
    SQLITE_DROP_TEMP_TRIGGER = 14
    SQLITE_DROP_TEMP_VIEW = 15
    SQLITE_DROP_TRIGGER = 16
    SQLITE_DROP_VIEW = 17
    SQLITE_DROP_VTABLE = 30
    SQLITE_FUNCTION = 31
    SQLITE_IGNORE = 2
    SQLITE_INSERT = 18
    SQLITE_OK = 0
    SQLITE_PRAGMA = 19
    SQLITE_READ = 20
    SQLITE_RECURSIVE = 33
    SQLITE_REINDEX = 27
    SQLITE_SAVEPOINT = 32
    SQLITE_SELECT = 21
    SQLITE_TRANSACTION = 22
    SQLITE_UPDATE = 23
    adapters = {(<class 'datetime.date'>, <class 'sqlite3.PrepareProtocol'...
    apilevel = '2.0'
    converters = {'DATE': <function register_adapters_and_converters.<loca...
    paramstyle = 'qmark'
    sqlite_version = '3.31.1'
    sqlite_version_info = (3, 31, 1)
    threadsafety = 1
    version = '2.6.0'
    version_info = (2, 6, 0)

FILE
    c:\users\samsp\appdata\local\programs\python\python38\lib\sqlite3\__init__.py


None
>>> 
=========== RESTART: C:/Users/samsp/Desktop/PROFESSIONAL PORTFOLIO/Python-Projects/Databases.py ===========
>>> 