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
           
        return HttpResponse()