from handler import ask

event = {
  "queryStringParameters": {
    "question": "what number do i call to certify"
  }
}

ask(event=event, context={})
