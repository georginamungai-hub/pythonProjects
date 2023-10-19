from flask import(
    # flash,
    render_template,
    request,
    # session,
    url_for,
)

from twilio.twiml.voice_response import VoiceResponse
from capstoneProject.init import app
from capstoneProject.callinfo import twiml
from capstoneProject import ChurchInventory

@app.route('/')
@app.route('/ivr')

def home():
    return render_template('index.html')

@app.route('/ivr/welcome', methods=['POST'])
def welcome():
    response = VoiceResponse()
    with response.gather(
        num_digits= 1, action=url_for('menu'), method="POST"
    ) as g:
        g.say(message="Thank You For Calling Community4You Service" + "Press 1 for churches in Nairobi" + "Press 2 for churches in Nakuru" + "Press 3 for churches in Mombasa" + "Press 4 for Churches in Kisumu" + "Press 5 for churches in Eldoret", loop=3)
        return twiml(response)
    
@app.route('/ivr/menu', methods=['POST'])
def menu():
    selected_option = request.form['Digits']
    option_actions = {'1': nairobiChurches,
                        '2': nakuruChurches,
                        '3': mombasaChurches,
                         '4':kisumuChurches,
                         '5':eldoretChurches}
    if option_actions.has_key(selected_option):
        response = VoiceResponse()
        option_actions[selected_option](response)
        return twiml(response)
    
    return _redirect_welcome()

def nairobiChurches(response):
    response.say(ChurchInventory,voice="Polly.Amy",language= "en-GB")
    response.say("Thank you for Calling Community4You Services")

    response.hangup()
    return response

def _redirect_welcome():
    response = VoiceResponse()
    response.say("Returning to the main menu", voice="Polly.Amy",language="en-GB")
    response.redirect(url_for("welcome"))

    return twiml