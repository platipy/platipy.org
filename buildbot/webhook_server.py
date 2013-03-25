from flask import Flask, request
import json
import tasks

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
	payload = request.form.get('payload', None)
	if payload is None:
		return 'Sad Panda'
	
	payload = json.loads(payload)
	ref = payload['ref']
	tasks.update.apply_async([ref])
	return 'Okay, thanks'

if __name__ == "__main__":
	app.run('platipy.org', debug=True)
