---
lab:
    title: 'Use prebuilt Document Intelligence models'
    module: 'Module 11 - Reading Text in Images and Documents'
---

# Use prebuilt Document Intelligence models

In this exercise, you'll set up an Azure AI Document Intelligence resource in your Azure subscription. You'll use both the Azure AI Document Intelligence Studio and C# code to submit forms to that resource for analysis.

## Create an Azure AI Document Intelligence resource

Before you can call the Azure AI Document Intelligence service, you must create a resource to host that service in Azure:

1. In the [Azure portal](https://portal.azure.com/learn.docs.microsoft.com?azure-portal=true), on the home page in the top search box, type **Document intelligence** and then press <kbd>Enter</kbd>.
1. On the **Document Intelligence** page, select **Create**.
1. On the **Basics** page of **Create Document Intelligence** wizard, in the **Subscription** list, select your subscription.
1. Under the **Resource group** list, select **Create new**.
1. In the **Name** textbox, type **DocIntelligenceResources** and then select **OK**.
1. In the **Region** list, select a region near you.
1. In the **Name** box, type a globally unique name for your resource.
1. In the **Pricing tier** list, select **Free F0** and then select **Review + create**.

    :::image type="content" source="../media/5-create-resource-details.png" alt-text="Screenshot showing how to complete the Create Azure AI Document Intelligence wizard in the Azure portal.":::

1. On the **Review + create** page, select **Create**, and then wait while Azure creates the Azure AI Document Intelligence resource.
1. When the deployment is complete, select **Go to resource**. Keep this page open for the rest of this exercise. 

## Use the read model

Let's start by using the **Azure AI Document Intelligence Studio** and the read model to analyze a document with multiple languages. You'll connect Azure AI Document Intelligence Studio to the resource you just created to perform the analysis:

1. Open a new browser tab and go to [Azure AI Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio).
1. Under **Document Analysis**, select **Read**.

    :::image type="content" source="../media/5-studio-home-page.png" alt-text="Screenshot showing the home page of the Azure AI Document Intelligence Studio with Read selected." lightbox="../media/5-studio-home-page.png":::

1. If you are asked to sign into your account, use your Azure credentials.
1. If you are asked which Azure AI Document Intelligence resource to use, select the subscription and resource name you used when you created the Azure AI Document Intelligence resource.
1. In the list of documents on the left, select **read-german.png**.

    :::image type="content" source="../media/5-read-german-sample.png" alt-text="Screenshot showing the Read page in Azure AI Document Intelligence Studio." lightbox="../media/5-read-german-sample.png":::

1. At the top-left, select **Analyze**.
1. When the analysis is complete, the text extracted from the image is shown on the right in the **Content** tab. Review this text and compare it to the text in the original image for accuracy.
1. Select the **Result** tab. This tab displays the extracted JSON code. 
1. Scroll to the bottom of the JSON code in the **Result** tab. Notice that the read model has detected the language of each span. Most spans are in German (language code `de`) but the last span is in English (language code `en`).

    :::image type="content" source="../media/5-language-detection.png" alt-text="Screenshot showing the detection of language for two spans in the results from the read model in Azure AI Document Intelligence Studio.":::

## Run Cloud Shell

We'll use Cloud Shell in your Azure subscription to host a console application that calls Azure AI Document Intelligence. Follow these steps to start the Cloud Shell:

1. In the Azure portal select the **[>_]** (Cloud Shell) button at the top of the page to the right of the search box. This opens a Cloud Shell pane at the bottom of the portal.

    :::image type="content" source="../media/5-open-cloud-shell.png" alt-text="Screenshot showing how to open Cloud Shell in the Azure portal." lightbox="../media/5-open-cloud-shell.png":::

1. The first time you open the Cloud Shell, you may be prompted to choose the type of shell you want to use (*Bash* or *PowerShell*). Select **Bash**. If you do not see this option, skip the step.
1. If you are prompted to create storage for your Cloud Shell, ensure your subscription is specified and select **Create storage**. Then wait a minute or so for the storage to be created.

    :::image type="content" source="../media/5-create-storage.png" alt-text="Screenshot showing how to mount storage with Create storage highlighted." lightbox="../media/5-create-storage.png":::

1. Make sure the type of shell indicated on the top left of the Cloud Shell pane is switched to *Bash*. If it is *PowerShell*, switch to *Bash* by using the drop-down menu.

    :::image type="content" source="../media/5-switch-bash.png" alt-text="Screenshot showing how to change the Cloud Shell to Bash in the Azure portal.":::

1. Wait for Bash to start. You should see the following screen in the Azure portal:

    :::image type="content" source="../media/5-cloud-shell-ready.png" alt-text="Screenshot showing the Cloud Shell ready to use in the Azure portal.":::

## Use the invoice model

Now, let's write some code that uses your Azure AI Document Intelligence resource. You'll add your connection details to the sample code, and complete the project with lines that send a sample invoice and display data from it:

1. Open a new browser tab and go to the [sample invoice document](https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-invoice.pdf).
1. Examine the form and note some of its fields and values. This is the document that your code will analyze.

    :::image type="content" source="../media/5-sample-invoice.png" alt-text="Screenshot showing the sample invoice that the code will analyze." lightbox="../media/5-sample-invoice.png":::

1. In the Cloud Shell, to clone the code repository, enter this command:

    ```bash
    git clone https://github.com/MicrosoftLearning/mslearn-formrecognizer.git
    ```

1. Change to the starter directory and then start the code editor:

    ```bash
    cd formsreadermodules/Mod2/starter/invoicereader
    code Program.cs
    ```

1. Switch to the browser tab that displays the Azure AI Document Intelligence overview in the Azure portal. To the right of the **Endpoint** value, click the **Copy to clipboard** button.

    :::image type="content" source="../media/5-find-endpoint-key.png" alt-text="Screenshot showing  where to find the endpoint and API key in the Azure portal." lightbox="../media/5-find-endpoint-key.png":::

1. In the Cloud Shell code editor, in the list of files on the left, locate this line and replace `<Endpoint URL>` with the string you just copied:

    ```csharp
    string endpoint = "<Endpoint URL>";
    ```

1. Switch to the browser tab that displays the Azure AI Document Intelligence overview in the Azure portal. To the right of the **KEY 1** value, click the *Copy to clipboard** button.
1. In the Cloud Shell code editor, locate this line and replace `<API Key>` with the string you just copied:

    ```csharp
    string apiKey = "<API Key>";
    ```

1. Locate the comment `// Create the client`. Following that, on new lines, enter the following code:

    ```csharp
    var cred = new AzureKeyCredential(apiKey);
    var client = new DocumentAnalysisClient(new Uri(endpoint), cred);
    ```

1. Locate the comment `// Analyze the invoice`. Following that, on new lines, enter the following code:

    ```csharp
    AnalyzeDocumentOperation operation = await client.StartAnalyzeDocumentFromUriAsync("prebuilt-invoice", fileUri);
    await operation.WaitForCompletionAsync();
    ```

1. Locate the comment `// Display invoice information to the user`. Following that, on news lines, enter the following code:

    ```csharp
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
    ```

    > [!NOTE]
    > You've added code to display the vendor name. The starter project also includes code to display the customer name and invoice total.

1. To save your code and exit the editor, press <kbd>CTRL + S</kbd> and then press <kbd>CTRL + Q</kbd>.
1. To build your project, enter this command:

    ```bash
    dotnet build
    ```

1. To run your code, enter this command:

    ```bash
    dotnet run
    ```

    The program displays the vendor name, customer name, and invoice total with confidence levels. Compare the values it reports with the sample invoice you opened at the start of this section.
