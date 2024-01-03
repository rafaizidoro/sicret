import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins="*")
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ):
    print(f"Client connected: {sid}")
    sio.emit("message", f"User {sid} has joined the chat.", skip_sid=sid)


@sio.event
def message(sid, data):
    print(f"Message from {sid}: {data}")
    sio.emit("message", f"{sid}: {data}", skip_sid=sid)


@sio.event
def disconnect(sid):
    print(f"Client disconnected: {sid}")


def start(host, port):
    eventlet.wsgi.server(eventlet.listen((host, port)), app)


def run_server(host="0.0.0.0", port=6969):
    start(host, port)


# import eventlet
# import socketio

# sio = socketio.Server(cors_allowed_origins='*')
# app = socketio.WSGIApp(sio)

# @sio.event
# def connect(sid, environ):
#     print(f"Client connected: {sid}")
#     sio.emit('message', f"User {sid} has joined the chat.", skip_sid=sid)

# @sio.event
# def message(sid, data):
#     print(f"Message from {sid}: {data}")
#     sio.emit('message', f"{sid}: {data}", skip_sid=sid)

# @sio.event
# def disconnect(sid):
#     print(f"Client disconnected: {sid}")
