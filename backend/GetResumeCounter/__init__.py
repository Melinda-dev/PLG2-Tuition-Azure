import azure.functions as func
import json

def main(req: func.HttpRequest, inputDocument: func.DocumentList,
         outputDocument: func.Out[func.Document]) -> func.HttpResponse:
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE',
        'Access-Control-Allow-Headers': 'Content-Type',
    }
    
    try:
        count = 0
        if inputDocument:
            # Retrieve the count value from the input document
            count = inputDocument[0].get('count', 0)
        
        count += 1
        inputDocument[0]['count'] = count
        outputDocument.set(inputDocument[0])
        
        json_to_return = json.dumps({"id": 1,"count": count})
    
        return func.HttpResponse(body=json_to_return, status_code=200, mimetype="application/json", headers=headers)
    except Exception as e:
        error_message = str(e)
        return func.HttpResponse(body=error_message, status_code=500, headers=headers)


        
