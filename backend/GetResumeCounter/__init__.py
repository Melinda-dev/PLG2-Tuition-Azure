import logging
import azure.functions as func
import json
from azure.cosmos import CosmosClient
from azure.functions import HttpRequest, HttpResponse


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE',
        'Access-Control-Allow-Headers': 'Content-Type',
          }    
    
        # Connect to Azure Cosmos DB        
        
        endpoint = 'https://tuition-school.documents.azure.com:443'
        key = '9947ChQSPP8FGF5jnLQS2DTnzBhpd6v1xDunFfxBgVm1L1kRYFQrczuPUgrf1Uzb2QFcVT0m8vthACDbAL1WXw=='
        client = CosmosClient(endpoint, key)

        database_name = 'tuitionschool'
        container_name = 'counter'
        database = client.get_database_client(database_name)
        container = database.get_container_client(container_name)

             
        # Create the counter document if it doesn't exist
        document_id = '1'
        counter_document = container.read_item(item=document_id, partition_key=document_id)
        if counter_document is None:
            document = {'id': document_id, 'count': 0}
            container.create_item(document)
            counter_document = container.read_item(item=document_id, partition_key=document_id)
            
            
        # Update the counter
        counter_document['count'] += 1
        container.replace_item(item=counter_document, body=counter_document)

        # Serialize counter document to JSON
        json_to_return = json.dumps(counter_document)

        # Create and return HTTP response
        return HttpResponse(body=json_to_return, status_code=200, mimetype="application/json",headers=headers)
        
    
    except Exception as e:
        logging.error(f'An error occurred: {str(e)}')
        return func.HttpResponse(
            "An error occurred while processing the request.",
            status_code=500
        )

        
