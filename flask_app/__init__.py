from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, join_room, leave_room, send, emit
import random, string
from saladbowl.saladbowl_game import Saladbowl_game
import json
from saladbowl import saladbowl_sockets

DATA_NUM_WORDS_PER_PLAYER="numWordsPerPlayer"
DATA_USERNAME="username"
DATA_ROOM_ID="room_id"
DATA_WORD_LIST="word_list"

app = Flask(__name__)
socketio = SocketIO(app)
app.secret_key = b'FF\x90}\xdc\xc5\xaeaT\xd6\xbc\x86O\xa6B\xdd\xa2qp\x9e\xd2f\xe8\xe8'

ROOMS = {}
#SID_TO_ROOM = {}

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

# def add_player_to_game(game, username, sid):
#     game.add_id_to_player(username, sid)
#     if len(game.players_by_username) % 2 == 0:
#         player = game.get_player(username)
#         player.team = saladbowl_player.TEAM_RED
#         player.order = len(

@socketio.on('create')
def on_create(data):
    room_id = get_unique_room_id()
    cur_user=data[DATA_USERNAME]
    sid = request.sid
    new_game = Saladbowl_game(room_id=room_id,
                              num_words_per_player=int(data[DATA_NUM_WORDS_PER_PLAYER]))
    new_game.add_id_to_player(cur_user, sid)
    
    ROOMS[room_id] = new_game
    join_room(room_id)
    #SID_TO_ROOM[sid] = room_id
    #ROOMS[room_id] = {'num_people':3, 'room_id':room_id}
    print ("CREATED " + room_id)
    print (json.dumps(new_game.to_dic()))
    emit (saladbowl_sockets.SOCKET_JOIN_ROOM, saladbowl_sockets.msg_join_room(new_game))
    
@socketio.on('join')
def on_join(data):
    print ("ON JOIN")
    room_id = data[DATA_ROOM_ID]
    username = data[DATA_USERNAME]
    sid = request.sid
    
    if not room_id in ROOMS:
        print ("EMITTING ERROR")
        emit ('error', {'error': 'Unable to join room. Room does not exist.'})
    else:
        # if data[DATA_USERNAME] in ROOMS[data[DATA_ROOM_ID]].players:
        #     print ("User already exists in room")
        #     emit ('error', {'error': 'Unable to join room. A user with that name is currently connected.'})
        print ("EMITTING JOIN ROOM")
        game = ROOMS[data[DATA_ROOM_ID]]
        #game.players.append(data[DATA_USERNAME])
        game.add_id_to_player(username, sid)
        print (json.dumps(game.to_dic()))
        #emit ('join_room', game.to_dic())
        join_room(room_id)
        #SID_TO_ROOM[sid] = room_id
        #emit (saladbowl_sockets.SOCKET_JOIN_ROOM_CAST, saladbowl_sockets.msg_join_room_cast(game), room=room_id)
        emit (saladbowl_sockets.SOCKET_GAME_UPDATE_CAST, saladbowl_sockets.msg_game_update_cast(game), room=room_id)

@socketio.on('disconnect')
def on_disconnect():
    print ("RECEIVED DISCONNECT")
    #sid = request.sid
    #if sid in SID_TO_ROOM:
    #    cur_room_id = SID_TO_ROOM[sid]
    #    print ("REMOVED USER: " + ROOMS[cur_room_id].get_player_from_id(sid).username)
    #    ROOMS[cur_room_id].remove_player_id(sid)
    #    SID_TO_ROOM.pop(sid)
    #    send(ROOMS[cur_room_id].to_dic(), room=cur_room_id)

@socketio.on('submit_words')
def on_submit_words(data):
    room_id = data[DATA_ROOM_ID]
    username = data[DATA_USERNAME]
    words = data[DATA_WORD_LIST]
    game = ROOMS[room_id]
    game.players_by_username[username].submitted_words = True
    game.word_list.extend([x.strip() for x in words.split(';')])
    print ("RECEIVED MESSAGE: {} {} WORDS: {}".format(room_id, username, words))
    emit (saladbowl_sockets.SOCKET_GAME_UPDATE_CAST, saladbowl_sockets.msg_game_update_cast(game), room=room_id)
    #send(game.to_dic(), room=room_id)

@socketio.on('change_team')
def on_change_team(data):
    username = data[DATA_USERNAME]
    room_id = data[DATA_ROOM_ID]
    print ("RECEIVED CHANGE TEAM: " + username)
    game = ROOMS[room_id]
    game.get_player(username).change_team()
    print (json.dumps(game.to_dic()))
    emit (saladbowl_sockets.SOCKET_GAME_UPDATE_CAST, saladbowl_sockets.msg_game_update_cast(game), room=room_id)

@socketio.on('start')
def on_start(data):
    room_id = data[DATA_ROOM_ID]
    print ("RECEIVED START")
    game = ROOMS[room_id]
    game.game_state = Saladbowl_game.GS_WAITING_ON_TURN
    game.cur_player = random.choice(list(game.players_by_username.keys()))
    emit (saladbowl_sockets.SOCKET_GAME_UPDATE_CAST, saladbowl_sockets.msg_game_update_cast(game), room=room_id)

@socketio.on('leave')
def on_leave(data):
    username = data[DATA_USERNAME]
    room_id = data[DATA_ROOM_ID]
    print ("RECEIVED LEAVE GAME: " + username)
    
    game = ROOMS[room_id]
    game.remove_player(username)
    print (json.dumps(game.to_dic()))
    emit (saladbowl_sockets.SOCKET_GAME_UPDATE_CAST, saladbowl_sockets.msg_game_update_cast(game), room=room_id)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)

