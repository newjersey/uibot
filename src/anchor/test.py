from handler import ask

event = {
  "queryStringParameters": {
    "question": "what is this program"
  }
}

ask(event=event, context={})
