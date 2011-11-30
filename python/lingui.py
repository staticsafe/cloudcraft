from gi.repository import Gtk

class MyWindow(Gtk.Window):

	#just a test does nothing
	def __init__(self):
		Gtk.Window.__init__(self, title='Minecraft Server Manager')
		self.button = Gtk.Button(label='Start Server')
		self.button.connect('clicked', self.on_button_clicked)
		self.add(self.button)
		
	def on_button_clicked(self, widget):
		print('Server Shutdown')
		
win = MyWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()

