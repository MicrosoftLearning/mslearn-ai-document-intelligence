from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

endpoint = "Endpoint URL"
key = "API Key"

document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

poller = document_analysis_client.begin_analyze_document_from_url(
    "prebuilt-receipt", "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-invoice.pdf", locale="en-US"
)

receipts = poller.result()

for idx, receipt in enumerate(receipts.documents):
    print(f"--------Analysis of receipt #{idx + 1}--------")
    print(f"Receipt type: {receipt.doc_type if receipt.doc_type else 'N/A'}")
    merchant_name = receipt.fields.get("MerchantName")
    if merchant_name:
        print(
            f"Merchant Name: {merchant_name.value} has confidence: "
            f"{merchant_name.confidence}"
        )
    transaction_date = receipt.fields.get("TransactionDate")
    if transaction_date:
        print(
            f"Transaction Date: {transaction_date.value} has confidence: "
            f"{transaction_date.confidence}"
        )
    if receipt.fields.get("Items"):
        print("Receipt items:")
        for idx, item in enumerate(receipt.fields.get("Items").value):
            print(f"...Item #{idx + 1}")
            item_description = item.value.get("Description")
            if item_description:
                print(
                    f"......Item Description: {item_description.value} has confidence: "
                    f"{item_description.confidence}"
                )
            item_quantity = item.value.get("Quantity")
            if item_quantity:
                print(
                    f"......Item Quantity: {item_quantity.value} has confidence: "
                    f"{item_quantity.confidence}"
                )
            item_price = item.value.get("Price")
            if item_price:
                print(
                    f"......Individual Item Price: {item_price.value} has confidence: "
                    f"{item_price.confidence}"
                )
            item_total_price = item.value.get("TotalPrice")
            if item_total_price:
                print(
                    f"......Total Item Price: {item_total_price.value} has confidence: "
                    f"{item_total_price.confidence}"
                )
    subtotal = receipt.fields.get("Subtotal")
    if subtotal:
        print(f"Subtotal: {subtotal.value} has confidence: {subtotal.confidence}")
    tax = receipt.fields.get("TotalTax")
    if tax:
        print(f"Total tax: {tax.value} has confidence: {tax.confidence}")
    tip = receipt.fields.get("Tip")
    if tip:
        print(f"Tip: {tip.value} has confidence: {tip.confidence}")
    total = receipt.fields.get("Total")
    if total:
        print(f"Total: {total.value} has confidence: {total.confidence}")
    print("--------------------------------------")