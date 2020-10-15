from pynput import mouse

def on_move(x, y):
    print("Mouse moved to ({0}, {1})".format(x, y))

listener = mouse.Listener(on_move=on_move)

listener.start()
