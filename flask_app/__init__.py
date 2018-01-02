from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, join_room, leave_room, send, emit
import random, string
from saladbowl.saladbowl_game import Saladbowl_game

DATA_NUM_WORDS_PER_PLAYER="numWordsPerPlayer"
DATA_USERNAME="username"
DATA_ROOM_ID="room_id"

app = Flask(__name__)
socketio = SocketIO(app)
app.secret_key = b'FF\x90}\xdc\xc5\xaeaT\xd6\xbc\x86O\xa6B\xdd\xa2qp\x9e\xd2f\xe8\xe8'

ROOMS = {}

@app.route('/stats')
def stats():
    resp = {
        "total": len(ROOMS)
    }
    if 'rooms' in request.args:
        resp["rooms"] = {k: v.to_dic() for k, v in ROOMS.items()}
    return jsonify (resp)

def create_room_id():
    id_length = 4
    return ''.join([random.choice(string.ascii_uppercase) for _ in range(0,id_length)])

def get_unique_room_id():
    new_room = create_room_id()
    while new_room in ROOMS:
        new_room = create_room_id()
    return new_room

@socketio.on('create')
def on_create(data):
    room_id = get_unique_room_id()
    ROOMS[room_id] = Saladbowl_game(game_id=room_id,
                                    num_words_per_player=int(data[DATA_NUM_WORDS_PER_PLAYER]),
                                    players=[data[DATA_USERNAME]])
    join_room(room_id)
    #ROOMS[room_id] = {'num_people':3, 'game_id':room_id}
    print ("CREATED " + room_id)
    emit ('join_room', {'room_id' : room_id})
    
@socketio.on('join')
def on_join(data):
    print ("ON JOIN")
    room_id = data['room_id']
    if not room_id in ROOMS:
        print ("EMITTING ERROR")
        emit ('error', {'error': 'Unable to join room. Room does not exist.'})
    else:
        if data[DATA_USERNAME] in ROOMS[data[DATA_ROOM_ID]].players:
            print ("User already exists in room")
            emit ('error', {'error': 'Unable to join room. A user with that name is currently connected.'})
        print ("EMITTING JOIN ROOM")
        ROOMS[data[DATA_ROOM_ID]].players.append(data[DATA_USERNAME])
        emit ('join_room', {'room_id' : room_id })

@socketio.on('leave')
def on_leave(data):
    send('left', room='a')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8001, debug=True)

#def app(environ, start_response):
#    """Simplest possible application object"""
#    data = 'Hello, World!\n'
#    status = '200 OK'
#    response_headers = [
#        ('Content-type','text/plain'),
#        ('Content-Length', str(len(data)))
#    ]
#    start_response(status, response_headers)
#    return iter([data])
