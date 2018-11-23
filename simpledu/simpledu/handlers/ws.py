from flask import Blueprint
import redis
import gevent

ws = Blueprint('ws', __name__, url_prefix = '/ws')


redis = redis.from_url('redis://127.0.0.1:6379')

class Chatroom(object):
    def __init__(self):
        self.clients = []
        self.pubsub = redis.pubsub()
        self.pubsub.subscribe('char')

    def register(self, client):
        self.clients.append(client)

    def send(self, client, data):
        try:
            client.send(data.decode('utf-8'))
        except:
            self.clients.remove(client)

    def run(self):
        print("this is run")
        for message in self.pubsub.listen():
            print("run ", message)
            if message['type'] == 'message':
                data = message.get('data')
                for client in self.clients:
                    print("data ", data)
                    gevent.spawn(self.send, client, data)

    def start(self):
        print("this is start")
        gevent.spawn(self.run)


chat = Chatroom()
chat.start()

@ws.route('/send')
def inbox(ws):
    while not ws.closed:
        message = ws.receive()

        print(message)
        if message:
            print("this is inbox")
            redis.publish('chat', message)

@ws.route('/recv')
def outbox(ws):
    print("/recv")
    chat.register(ws)
    while not ws.closed:
        gevent.sleep(0.1)

