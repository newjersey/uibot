from handler import ask

event = {
  "queryStringParameters": {
    "question": "what is this program and how to I apply?"
  }
}

ask(event=event, context={})
