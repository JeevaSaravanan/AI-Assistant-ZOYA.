# wolfram_utils.py

import wolframalpha
from constants import WOLFRAM_APP_ID
from speech_utils import speak

client = wolframalpha.Client(WOLFRAM_APP_ID)

def resolveListOrDict(variable):
    if isinstance(variable, list):
        return variable[0]['plaintext']
    else:
        return variable['plaintext']

def removeBrackets(variable):
    return variable.split('(')[0]

def wolfram_search(query):
    res = client.query(query)
    if res['@success'] == 'false':
        return False
    else:
        pod0 = res['pod'][0]
        pod1 = res['pod'][1]

        if (('definition' in pod1['@title'].lower()) or 
            ('result' in pod1['@title'].lower()) or 
            (pod1.get('@primary', 'false') == 'true')):
            result = resolveListOrDict(pod1['subpod'])
            speak(result)
            return True
        else:
            question = resolveListOrDict(pod0['subpod'])
            question = removeBrackets(question)
            speak(f"I found this: {question}")
            return True
