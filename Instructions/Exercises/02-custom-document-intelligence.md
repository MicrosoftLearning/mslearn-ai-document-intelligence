---
lab:
    title: 'Extract Data from Forms'
    module: 'Module 11 - Reading Text in Images and Documents'
---

# Extract Data from Forms 

Suppose a company currently requires employees to manually purchase order sheets and enter the data into a database. They would like you to utilize AI services to improve the data entry process. You decide to build a machine learning model that will read the form and produce structured data that can be used to automatically update a database.

**Azure AI Document Intelligence** is an Azure AI service that enables users to build automated data processing software. This software can extract text, key/value pairs, and tables from form documents using optical character recognition (OCR). Azure AI Document Intelligence has pre-built models for recognizing invoices, receipts, and business cards. The service also provides the capability to train custom models. In this exercise, we will focus on building custom models.

## Clone the repo into your Azure Cloud Shell

1. In the [Azure portal](https://portal.azure.com?azure-portal=true), select the **[>_]** (*Cloud Shell*) button at the top of the page to the right of the search box. A Cloud Shell pane will open at the bottom of the portal.

    ![Screenshot of starting Cloud Shell by clicking on the icon to the right of the top search box.](../media/cloudshell-launch-portal.png#lightbox)

1. The first time you open the Cloud Shell, you may be prompted to choose the type of shell you want to use (*Bash* or *PowerShell*). Select **Bash**. If you don't see this option, skip the step.

1. If you're prompted to create storage for your Cloud Shell, ensure your subscription is specified and select **Create storage**. Then wait a minute or so for the storage to be created.

1. Once the terminal starts, run the following commands to download a copy of the repo into your Cloud Shell:

    ```bash
    rm -r doc-intelligence -f
    git clone https://github.com/MicrosoftLearning/mslearn-ai-document-intelligence doc-intelligence
    ```
  
    > **TIP**
    > If you recently used this command in another lab to clone the *doc-intelligence* repository, you can skip this step.
 
1. The files have been downloaded into a folder called **doc-intelligence**. Let's use the Cloud Shell Code editor to open the appropriate folder by running:

    ```bash
    cd doc-intelligence/Labfiles/02-custom-document-intelligence
    ```

    ```bash
    code .
    ```

## Create a Azure AI Document Intelligence resource

To use the Azure AI Document Intelligence service, you need a Azure AI Document Intelligence or Azure AI Services resource in your Azure subscription. You'll use the Azure portal to create a resource.

1.  In the Azure portal, search for *Document intelligence*, select **Document intelligence**, and create a resource with the following settings:

    - **Subscription**: *Your Azure subscription*
    - **Resource group**: *Choose or create a resource group (if you are using a restricted subscription, you may not have permission to create a new resource group - use the one provided)*
    - **Region**: *Choose any available region*
    - **Name**: *Enter a unique name*
    - **Pricing tier**: F0

    > **Note**: If you already have an F0 Document Intelligence service in your subscription, select **S0** for this one.

1. When the resource has been deployed, go to it and view its **Keys and Endpoint** page. You will need the **endpoint** and one of the **keys** from this page to manage access from your code later on.

## Gather documents for training

![An image of an invoice.](../02-custom-document-intelligence/sample-forms/Form_1.jpg)  

You'll use the sample forms from the **02-custom-document-intelligence/sample-forms** folder in this repo, which contain all the files you'll need to train and test a model.

1. In Cloud Shell Code, in the **02-custom-document-intelligence** folder,  expand the **sample-forms** folder. Notice there are files ending in **.json** and **.jpg** in the folder.

    You will use the **.jpg** files to train your model.  

    The **.json** files have been generated for you and contain label information. The files will be uploaded into your blob storage container alongside the forms.

    You can view the images we are using in the [sample-forms folder](https://github.com/MicrosoftLearning/mslearn-ai-document-intelligence/tree/main/Labfiles/02-custom-document-intelligence/sample-forms?azure-portal=true) of this repo on GitHub.

1. Return to the Azure portal and view the **Resource group** in which you created the Document Intelligence resource previously.

1. On the **Overview** page for your resource group, note the **Subscription ID** and **Location**. You will need these values, along with your **resource group** name in subsequent steps.

![An example of the resource group page.](./images/resource_group_variables.png)

1. In the terminal pane, run the following command to list Azure locations.

```
az account list-locations -o table
```

1. In the output, find the **Name** value that corresponds with the location of your resource group (for example, for *East US* the corresponding name is *eastus*).

    > **Important**: Record the **Name** value and use it in Step 12.

1. In the Code window, in the **02-custom-document-intelligence** folder, select **setup.sh**. You will use this script to run the Azure command line interface (CLI) commands required to create the other Azure resources you need.

1. In the **setup.sh** script, review the commands. The program will: 
    - Create a storage account in your Azure resource group
    - Upload files from your local _sampleforms_ folder to a container called _sampleforms_ in the storage account
    - Print a Shared Access Signature URI

12. Modify the **subscription_id**, **resource_group**, and **location** variable declarations with the appropriate values for the subscription, resource group, and location name where you deployed the Document Intelligence resource. 
Then **save** your changes.

    Leave the **expiry_date** variable as it is for the exercise. This variable is used when generating the Shared Access Signature (SAS) URI. In practice, you will want to set an appropriate expiry date for your SAS. You can learn more about SAS [here](https://docs.microsoft.com/azure/storage/common/storage-sas-overview#how-a-shared-access-signature-works).  

13. In the terminal for the **02-custom-document-intelligence** folder, enter the following command to run the script:

```
sh setup.sh
```

14. When the script completes, review the displayed output and note your Azure resource's SAS URI.

> **Important**: Before moving on, paste the SAS URI somewhere you will be able to retrieve it again later (for example, in a new text file in notepad or the Code window).

15. In the Azure portal, refresh the resource group and verify that it contains the Azure Storage account just created. Open the storage account and in the pane on the left, select **Storage Browser (preview)**. Then in Storage Browser, expand **Blob containers** and select the **sampleforms** container to verify that the files have been uploaded from your local **02-custom-document-intelligence/sample-forms** folder.

## Train the model using Document Intelligence Studio

Now you will train the model using the files uploaded to the storage account.

1. In your browser, navigate to the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio) and sign into your subscription.
1. Scroll down to **Custom models** and create a new **Custom extraction model**.
1. Create a new project:

    - **Project name**: Enter a unique name.
        - Select *Continue*.
    - **Configure service resource**: Select the subscription, resource group, and document intelligence resource you created previously in this lab.
        - Select *Continue*.
    - **Connect training data source**: Select the subscription, resource group, and storage account that was created by the setup script. Select the `sampleforms` blob container, and leave the folder path blank.
        - Select *Continue*.
    - Select *Create project*

1. Once your project is created, select **Train** to train your model. Provide a model ID (which you'll need in the next step) and choose *Template* build mode.
1. Training can take some time. You'll see a notification when it's complete.

## Test your custom Document Intelligence model

1. In the terminal of Azure portal, navigate to the folder of your preferred language.

1. Install the Document Intelligence package by running the appropriate command for your language preference:

**C#**

```
dotnet add package Azure.AI.FormRecognizer --version 4.1.0 
```

**Python**

```
pip install azure-ai-formrecognizer==3.3.0
```
1. Open the code files for your preferred language in the code editor.

    ```bash
    code .
    ```

1. Edit the configuration file (**appsettings.json** or **.env**, depending on your language preference) to add the following values:
    - Your Document Intelligence endpoint.
    - Your Document Intelligence key.
    - The Model ID generated you provided when training your model. You can find this on the **Models** page of the Document Intelligence Studio. **Save** your changes.

6. In the code editor, open the code file for your client application (*Program.cs* for C#, *test-model.py* for Python) and review the code it contains, particularly that the image in the URL refers to the file in this GitHub repo on the web.    

7. Return the terminal, and enter the following command to run the program:

**C#**

```
dotnet run
```

**Python**

```
python test-model.py
```

8. View the output and observe how the output for the model provides field names like `Merchant` and `CompanyPhoneNumber`.

## Clean up

When you're done with your Azure resource, remember to delete the resource in the [Azure portal](https://portal.azure.com/?azure-portal=true) to avoid further charges.

## More information

For more information about the Document Intelligence service, see the [Document Intelligence documentation](https://learn.microsoft.com/azure/ai-services/document-intelligence/?azure-portal=true).
