from Plugins.Plugin import PluginDescriptor

print "[ServiceMP3] importing...."
import servicemp3

def autostart(reason, **kwargs):
	print "[ServiceMP3] autostart...."
	import servicemp3

def Plugins(**kwargs):
	return [
		PluginDescriptor(where = PluginDescriptor.WHERE_AUTOSTART, needsRestart = True, fnc = autostart)
	]
