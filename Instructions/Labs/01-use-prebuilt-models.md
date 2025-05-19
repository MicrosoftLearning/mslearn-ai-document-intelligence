---
lab:
    title: 'Use prebuilt Document Intelligence models'
    module: 'Module 6 - Document Intelligence'
---

# Use prebuilt Document Intelligence models

In this exercise, you'll set up an Azure AI Foundry project with all the necessary resources for document analysis. You'll use both the Azure AI Foundry and C# or Python to submit forms to that resource for analysis.

## Create an Azure AI Foundry project

Let's start by creating an Azure AI Foundry project.

1. In a web browser, open the [Azure AI Foundry portal](https://ai.azure.com) at `https://ai.azure.com` and sign in using your Azure credentials. Close any tips or quick start panes that are opened the first time you sign in, and if necessary use the **Azure AI Foundry** logo at the top left to navigate to the home page, which looks similar to the following image:

    ![Screenshot of Azure AI Foundry portal.](../media/ai-foundry-home.png)

1. In the home page, select **+ Create project**.
1. In the **Create a project** wizard, enter a suitable project name for (for example, `my-ai-project`) then review the Azure resources that will be automatically created to support your project.
1. Select **Customize** and specify the following settings for your hub:
    - **Hub name**: *A unique name - for example `my-ai-hub`*
    - **Subscription**: *Your Azure subscription*
    - **Resource group**: *Create a new resource group with a unique name (for example, `my-ai-resources`), or select an existing one*
    - **Location**: Choose any available region
    - **Connect Azure AI Services or Azure OpenAI**: *Create a new AI Services resource with an appropriate name (for example, `my-ai-services`) or use an existing one*
    - **Connect Azure AI Search**: Skip connecting

1. Select **Next** and review your configuration. Then select **Create** and wait for the process to complete.
1. When your project is created, close any tips that are displayed and review the project page in Azure AI Foundry portal, which should look similar to the following image:

    ![Screenshot of a Azure AI project details in Azure AI Foundry portal.](../media/ai-foundry-project.png)

## Use the Read model

Let's start by using the **Azure AI Foundry** portal and the Read model to analyze a document with multiple languages:

1. In the navigation panel on the left, select **AI Services**.
1. In the **Azure AI Services** page, select the **Vision + Document** tile.
1. In the **Vision + Document** page, verify that the **Document** tab is selected, then select the **OCR/Read** tile.

    In the **Read** page, the Azure AI Services resource created with your project should already be connected.

1. In the list of documents on the left, select **read-german.pdf**.

    ![Screenshot showing the Read page in Azure AI Document Intelligence Studio.](../media/read-german-sample.png#lightbox)

1. At the top toolbar, select **Analyze options**, then enable the **Language** check-box (under **Optional detection**) in the **Analyze options** pane and click on **Save**. 
1. At the top-left, select **Run Analysis**.
1. When the analysis is complete, the text extracted from the image is shown on the right in the **Content** tab. Review this text and compare it to the text in the original image for accuracy.
1. Select the **Result** tab. This tab displays the extracted JSON code. 
1. Scroll to the bottom of the JSON code in the **Result** tab. Notice that the read model has detected the language of each span indicated by `locale`. Most spans are in German (language code `de`) but you can find other language codes in the spans (e.g. English - language code `en` - in one of the first span).

    ![Screenshot showing the detection of language for two spans in the results from the read model in Azure AI Document Intelligence Studio.](../media/language-detection.png#lightbox)

## Prepare to develop an app in Cloud Shell

Now let's explore the app that uses the Azure Document Intelligence service SDK. You'll develop your app using Cloud Shell. The code files for your app have been provided in a GitHub repo.

> **Tip**: If you have already cloned the **mslearn-ai-document-intelligence** repo, you can skip this task. Otherwise, follow these steps to clone it to your development environment.

1. In the Azure AI Foundry portal, view the **Overview** page for your project.
1. In the **Endpoints and keys** area, note the **API Key** and **Azure AI Services endpoint** under the **Azure AI Services** option. You'll use these credentials to connect to your Azure AI Services in a client application.
1. Open a new browser tab (keeping the Azure AI Foundry portal open in the existing tab). Then in the new tab, browse to the [Azure portal](https://portal.azure.com) at `https://portal.azure.com`; signing in with your Azure credentials if prompted.
1. Use the **[\>_]** button to the right of the search bar at the top of the page to create a new Cloud Shell in the Azure portal, selecting a ***PowerShell*** environment. The cloud shell provides a command line interface in a pane at the bottom of the Azure portal.

    > **Note**: If you have previously created a cloud shell that uses a *Bash* environment, switch it to ***PowerShell***.

1. In the cloud shell toolbar, in the **Settings** menu, select **Go to Classic version** (this is required to use the code editor).

    > **Tip**: As you paste commands into the cloudshell, the ouput may take up a large amount of the screen buffer. You can clear the screen by entering the `cls` command to make it easier to focus on each task.

1. In the PowerShell pane, enter the following commands to clone the GitHub repo for this exercise:

    ```
   rm -r mslearn-ai-document-intelligence -f
   git clone https://github.com/microsoftlearning/mslearn-ai-document-intelligence mslearn-ai-document-intelligence
    ```

Applications for both C# and Python have been provided, as well as a sample pdf file you'll use to test Document Intelligence. Both apps feature the same functionality. First, you'll complete some key parts of the application to enable using your Azure Document Intelligence resource.

1. Examine the following invoice and note some of its fields and values. This is the invoice that your code will analyze.

    ![Screenshot showing a sample invoice document.](../media/sample-invoice.png#lightbox)

    ***Now follow the steps for your chosen programming language.***

1. After the repo has been cloned, navigate to the folder containing the code files:  

    **C#**

    ```
   cd mslearn-ai-document-intelligence/Labfiles/01-prebuild-models/C-Sharp
    ```

    **Python**

    ```
   cd mslearn-ai-document-intelligence/Labfiles/01-prebuild-models/Python
    ```

1. In the cloud shell command line pane, enter the following command to install the libraries you'll use:

    **C#**

    ```
   dotnet add package Azure.AI.FormRecognizer --version 4.1.0
    ```

    **Python**

    ```
   pip install azure-ai-formrecognizer==3.3.3
    ```

## Add code to use the Azure Document Intelligence service

Now you're ready to use the SDK to evaluate the pdf file.

1. Enter the following command to edit the app file that has been provided:

    **C#**

    ```
   code Program.cs
    ```

    **Python**

    ```
   code document-analysis.py
    ```

    The file is opened in a code editor.

1. In the code file, replace the `<Endpoint URL>` and `<API Key>` placeholders with the **Azure AI Services endpoint** and **API Key** for your project (copied from the project **Overview** page, in the **Azure AI Services** capability option in the Azure AI Foundry portal):

    **C#**: ***Program.cs***

    ```csharp
    string endpoint = "<Endpoint URL>";
    string apiKey = "<API Key>";
    ```

    **Python**: ***document-analysis.py***

    ```python
    endpoint = "<Endpoint URL>"
    key = "<API Key>"
    ```

1. Locate the comment `Create the client`. Following that, on new lines, enter the following code:

    **C#**

    ```csharp
    var cred = new AzureKeyCredential(apiKey);
    var client = new DocumentAnalysisClient(new Uri(endpoint), cred);
    ```

    **Python**

    ```python
    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )
    ```

1. Locate the comment `Analyze the invoice`. Following that, on new lines, enter the following code:

    **C#**

    ```csharp
    AnalyzeDocumentOperation operation = await client.AnalyzeDocumentFromUriAsync(WaitUntil.Completed, "prebuilt-invoice", fileUri);
    ```

    **Python**

    ```python
    poller = document_analysis_client.begin_analyze_document_from_url(
        fileModelId, fileUri, locale=fileLocale
    )
    ```

1. Locate the comment `Display invoice information to the user`. Following that, on news lines, enter the following code:

    **C#**

    ```csharp
    AnalyzeResult result = operation.Value;
    
    foreach (AnalyzedDocument invoice in result.Documents)
    {
        if (invoice.Fields.TryGetValue("VendorName", out DocumentField? vendorNameField))
        {
            if (vendorNameField.FieldType == DocumentFieldType.String)
            {
                string vendorName = vendorNameField.Value.AsString();
                Console.WriteLine($"Vendor Name: '{vendorName}', with confidence {vendorNameField.Confidence}.");
            }
        }
    ```

    **Python**

    ```python
    receipts = poller.result()
    
    for idx, receipt in enumerate(receipts.documents):
    
        vendor_name = receipt.fields.get("VendorName")
        if vendor_name:
            print(f"\nVendor Name: {vendor_name.value}, with confidence {vendor_name.confidence}.")
    ```

    > [!NOTE]
    > You've added code to display the vendor name. The starter project also includes code to display the *customer name* and *invoice total*.


1. In the code editor, use the **CTRL+S** command or **Right-click > Save** to save your changes and then use the **CTRL+Q** command or **Right-click > Quit** to close the code editor while keeping the cloud shell command line open.

1. In the command line pane, enter the following command to run the application.

1. ***For C# only***, to build your project, enter this command:

    **C#**:

    ```powershell
    dotnet build
    ```

1. To run your code, enter this command:

    **C#**:

    ```powershell
    dotnet run
    ```

    **Python**:

    ```powershell
    python document-analysis.py
    ```

The program displays the vendor name, customer name, and invoice total with confidence levels. Compare the values it reports with the sample invoice you opened at the start of this section.

## Clean up

If you're done with your Azure resource, remember to delete the resource in the [Azure portal](https://portal.azure.com/?azure-portal=true) to avoid further charges.

## More information

For more information about the Document Intelligence service, see the [Document Intelligence documentation](https://learn.microsoft.com/azure/ai-services/document-intelligence/?azure-portal=true).
