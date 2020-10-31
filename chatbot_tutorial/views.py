from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import random
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse
from django.shortcuts import render
from pprint import pprint
import spacy

def processinput(inputstring):
    print(inputstring)
    post_message_url = 'https://api.telegram.org/bot1495665981:AAE1pKov14O-QBFCD1pOvJEv37eHdjjjBuE/sendMessage'    

    try:
        inputstring['message']
        mes='message'
    except:
        mes='edited_message'
    if(inputstring[mes]['text']=="/start"):
        data= {
                "chat_id": inputstring[mes]['chat']['id'],
                "text": "Please enter your name"
            }
        response = requests.get(post_message_url, data=data)
        return
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(inputstring[mes]['text'])
    flag=0
    for ent in doc.ents: 
        if(ent.label_=="PERSON"):
            flag=1
            response_msg= "Hello " + ent.text
            print(response_msg)
            data= {
                "chat_id": inputstring[mes]['chat']['id'],
                "text": response_msg
            }
    if(flag==0):
        data= {
                "chat_id": inputstring[mes]['chat']['id'],
                "text": "Sorry the name is not recognised. Do enter a valid name"
            }        
    response = requests.get(post_message_url, data=data)
    print(response)
    return
    
def post_facebook_message(fbid, recevied_message):           
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=<page-access-token>' 
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":recevied_message}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    pprint(status.json())
# @csrf_exempt 
# def chat(request):
#     print(request)
#     context = {}
#     return render(request, 'chatbot_tutorial/chatbot.html', context)


# def respond_to_websockets(message):
#     jokes = {
#      'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
#                 """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
#      'fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
#                 """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
#      'dumb':   ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
#                 """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""] 
#      }  

#     result_message = {
#         'type': 'text'
#     }
#     if 'fat' in message['text']:
#         result_message['text'] = random.choice(jokes['fat'])
    
#     elif 'stupid' in message['text']:
#         result_message['text'] = random.choice(jokes['stupid'])
    
#     elif 'dumb' in message['text']:
#         result_message['text'] = random.choice(jokes['dumb'])

#     elif message['text'] in ['hi', 'hey', 'hello']:
#         result_message['text'] = "Hello to you too! If you're interested in yo mama jokes, just tell me fat, stupid or dumb and i'll tell you an appropriate joke."
#     else:
#         result_message['text'] = "I don't know any responses for that. If you're interested in yo mama jokes tell me fat, stupid or dumb."

#     return result_message
    
class YoMamaBotView(generic.View):
    # The get method is the same as before.. omitted here for brevity
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        print(incoming_message)
        processinput(incoming_message)
        # Facebook recommends going through every entry since they might send
        # multiple messages in a single call during high load
        # for entry in incoming_message['entry']:
        #     for message in entry['messaging']:
        #         # Check to make sure the received call is a message call
        #         # This might be delivery, optin, postback for other events 
        #         if 'message' in message:
        #             # Print the message to the terminal
        #             pprint(message)     
        return HttpResponse()