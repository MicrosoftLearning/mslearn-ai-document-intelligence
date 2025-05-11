from dotenv import load_dotenv
from datetime import datetime
import os
import sys
import requests
import json

# Import namespaces
from azure.ai.projects.models import ConnectionType
from azure.identity import DefaultAzureCredential
from azure.core.credentials import AzureKeyCredential
from azure.ai.projects import AIProjectClient


def main():

    # Clear the console
    os.system('cls' if os.name=='nt' else 'clear')

    # Get invoice
    invoice_file = 'invoice-1236.pdf'
    if len(sys.argv) > 1:
        invoice_file = sys.argv[1]

    try:
        global speech_config

        # Get config settings
        load_dotenv()
        project_connection = os.getenv('PROJECT_CONNECTION')
        analyzer = os.getenv('ANALYZER')

        # Get AI Services endpoint and key from the project
        project_client = AIProjectClient.from_connection_string(
            conn_str=project_connection,
            credential=DefaultAzureCredential())

        ai_svc_connection = project_client.connections.get_default(
            connection_type=ConnectionType.AZURE_AI_SERVICES,
            include_credentials=True, 
            )

        ai_svc_endpoint = ai_svc_connection.endpoint_url
        ai_svc_key = ai_svc_connection.key

        # Analyze invoice
        analyze_invoice (invoice_file, analyzer, ai_svc_endpoint, ai_svc_key)

    except Exception as ex:
        print(ex)

def analyze_invoice (invoice_file, analyzer, endpoint, key):
    print (f"Analyzing {invoice_file}")

    CU_VERSION = "2024-12-01-preview";

    with open(invoice_file, "rb") as file:
        data = file.read()
    
    headers = {
    "Ocp-Apim-Subscription-Key": key,
    "Content-Type": "application/octet-stream"}


    url = endpoint + f'/contentunderstanding/analyzers/{analyzer}:analyze?api-version={CU_VERSION}'

    print ('Analyzing document...')
    response = requests.post(url, headers=headers, data=data)

    print(response.status_code)
    response_json = response.json()

    # Extract the "id" value from the response
    id_value = response_json.get("id")

    # Perform a GET request tO get the results
    print ('Getting results...')
    result_url = f'{endpoint}/contentunderstanding/analyzers/{analyzer}/results/{id_value}?api-version={CU_VERSION}'
    result_response = requests.get(result_url, headers=headers)
    print(result_response.status_code)

    status = result_response.json().get("status")
    while status == "Running":
        result_response = requests.get(result_url, headers=headers)
        status = result_response.json().get("status")

    if status == "Succeeded":
        print("Analysis succeeded.")
        result_json = result_response.json()
        contents = result_json["result"]["contents"]

        # Iterate through the fields and extract the names and values
        for content in contents:
            if "fields" in content:
                fields = content["fields"]
                for field_name, field_data in fields.items():
                    if "valueNumber" in field_data:
                        print(f"{field_name}: {field_data['valueNumber']}")
                    elif "valueString" in field_data:
                        print(f"{field_name}: {field_data['valueString']}")
                    elif field_name == "Items":
                        print("Items:")
                        item_list = field_data["valueArray"]
                        for item in item_list:
                            print("  Item:")
                            item_values = item["valueObject"]
                            for item_field_name, item_field_data in item_values.items():
                                if "valueNumber" in item_field_data:
                                    print(f"    {item_field_name}: {item_field_data['valueNumber']}")
                                elif "valueString" in item_field_data:
                                    print(f"    {item_field_name}: {item_field_data['valueString']}")


if __name__ == "__main__":
    main()        
