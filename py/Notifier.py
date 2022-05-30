#os.environ['LOGNAME'] = 'daniel'
#os.environ['HOME'] = '/home/daniel'
#os.environ['USER'] = 'daniel'
#os.environ['XDG_RUNTIME_DIR'] = '/run/user/1000'
#os.environ['DBUS_SESSION_BUS_ADDRESS'] = 'unix:path=/run/user/1000/bus'
import notify2

def notify(title, body):
  notify2.init(title)
  notify2.Notification(str(title), str(body)).show()
