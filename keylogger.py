from ctypes import *
import pythoncom
import pyHook
import win32clipboard

user32		= windll.user32
kernel32	= windll.kernel32
psapi		= windll.psapi
current_window = None

def get_current_process():

	# get a handle to the foreground windpw
	hwnd = user32.GetForegroundWindow()

	# find the process ID
	pid = c_ulong(o)
	user32.GetWindowThreadProcessId(hwnd, byref(pid))

	# store the current process ID
	process_id = "%d" % pid.value

	# grab the executable
	executable = create_string_buffer("\x00" * 512)
	h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)

	psapi.GetModuleBaseNameA(h_process,None,byref(executable),512)

	# now read it's title
	window_title = create_string_buffer("\x00" * 512)
	length = user32.GetWindowTextA(hwnd, byref(window_title),512)

	# print out the header if we're in the right process
	print
	print "[ PID: %s - %s - %s ]" % (process_id, executable.value, window_title.value)
	print


	# close handles
	kernel32.CloseHandle(hwnd)
	kernel32.CloseHandle(h_process)
