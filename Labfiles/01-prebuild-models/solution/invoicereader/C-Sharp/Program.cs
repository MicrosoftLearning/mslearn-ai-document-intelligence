using Azure;
using Azure.AI.FormRecognizer.DocumentAnalysis;

// Store connection information
string endpoint = "<Endpoint URL>";
string apiKey = "<API Key>";

Uri fileUri = new Uri("https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-invoice.pdf");

Console.WriteLine("Connecting to Forms Recognizer at: {0}", endpoint);
Console.WriteLine("Analyzing invoice at: {0}", fileUri.ToString());

// Create the client
var cred = new AzureKeyCredential(apiKey);
var client = new DocumentAnalysisClient(new Uri(endpoint), cred);

// Analyze the invoice
AnalyzeDocumentOperation operation = await client.StartAnalyzeDocumentFromUriAsync("prebuilt-invoice", fileUri);
await operation.WaitForCompletionAsync();

// Display invoice information to the user
AnalyzeResult result = operation.Value;
AnalyzedDocument invoice = result.Documents[0];

if (invoice.Fields.TryGetValue("VendorName", out DocumentField vendorNameField))
{
    if (vendorNameField.ValueType == DocumentFieldType.String)
    {
        string vendorName = vendorNameField.AsString();
        Console.WriteLine($"Vendor Name: '{vendorName}', with confidence {vendorNameField.Confidence}.");
    }
}

if (invoice.Fields.TryGetValue("CustomerName", out DocumentField customerNameField))
{
    if (customerNameField.ValueType == DocumentFieldType.String)
    {
        string customerName = customerNameField.AsString();
        Console.WriteLine($"Customer Name: '{customerName}', with confidence {customerNameField.Confidence}.");
    }
}

if (invoice.Fields.TryGetValue("InvoiceTotal", out DocumentField invoiceTotalField))
{
    if (invoiceTotalField.ValueType == DocumentFieldType.Currency)
    {
        CurrencyValue invoiceTotal = invoiceTotalField.AsCurrency();
        Console.WriteLine($"Invoice Total: '{invoiceTotal.Symbol}{invoiceTotal.Amount}', with confidence {invoiceTotalField.Confidence}.");
    }
}

Console.WriteLine("Analysis complete.");