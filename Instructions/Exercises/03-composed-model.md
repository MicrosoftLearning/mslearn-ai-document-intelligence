---
lab:
    title: 'Create a composed Document Intelligence model'
    module: 'Module 6 - Document Intelligence'
---

# Create a composed Document Intelligence model

In this exercise, you'll create and train two custom models that analyze different tax forms. Then, you'll create a composed model that includes both of these custom models. You'll test the model by submitting a form and you'll check that it recognizes the document type and labeled fields correctly.

## Set up resources

We'll use a script to create the Azure AI Document Intelligence resource, a storage account with sample forms, and a resource group:

1. Start Visual Studio Code.
1. Open the palette (SHIFT+CTRL+P) and run a **Git: Clone** command to clone the `https://github.com/MicrosoftLearning/mslearn-ai-document-intelligence` repository to a local folder (it doesn't matter which folder).
1. When the repository has been cloned, open the folder in Visual Studio Code.

    > **Note**: If you are prompted to add required assets to build and debug, select **Not Now**. If there are any other pop ups from Visual Studio Code, you can safely dismiss them.

1. Expand the **Labfiles** folder in the left pane, and right click on the **03-composed-model** directory. Select the option to open in the integrated terminal, and execute the following script:

    ```powershell
    az login --output none
    ```

    > **Note**: If you get an error about no active subscriptions and have MFA enabled, you may need to login to Azure portal at `https://portal.azure.com` first, then rerun the `az login`.

1. When prompted, sign into your Azure subscription. Then return to Visual Studio Code and wait for the sign-in process to complete.
1. In the integrated terminal, run the following command to set up resources:

   ```powershell
   ./setup.ps1
   ```

   > **IMPORTANT**: The last resource created by the script is your Azure AI Document Intelligence service. If that command fails due to you already having an F0 tier resource, either use that resource for this lab or create one manually using the S0 tier in the Azure portal.

## Create the 1040 Forms custom model

To create a composed model, we must first create two or more custom models. To create the first custom model:

1. In a new browser tab, start the **Azure AI Document Intelligence Studio** at `https://documentintelligence.ai.azure.com/studio`
1. Scroll down, and then under **Custom models**, select **Custom extraction model**.
1. If you're asked to sign into your account, use your Azure credentials.
1. If you're asked which Azure AI Document Intelligence resource to use, select the subscription and resource name you used when you created the Azure AI Document Intelligence resource.
1. Under **My Projects**, select **+ Create a project**.
1. In the **Project name** textbox, type **1040 Forms**, and then select **Continue**.
1. On the **Configure service resource** page, in the **Subscription** drop-down list, select your Azure subscription.
1. In the **Resource group** drop-down list, select the **DocumentIntelligenceResources&lt;xxxx&gt;** created for you.
1. In the **Azure AI Document Intelligence or Azure AI Service Resource** drop-down list, select **DocumentIntelligence&lt;xxxx&gt;**.
1. In the **API version** drop-down list, ensure that **2023-10-31-preview** is selected and then select **Continue**.
1. On the **Connect training data source** page, in the **Subscription** drop-down list, select your Azure subscription.
1. In the **Resource group** drop-down list, select **DocumentIntelligenceResources&lt;xxxx&gt;**.
1. In the **Storage account** drop-down list, select the only storage account listed. If you have multiple storage accounts in your subscription, choose the one starting with *docintelstorage*
1. In the **Blob container** drop-down list, select **1040examples**, and then select **Continue**.
1. In the **Review and create** page, select **Create project**.
1. Select **Run layout** in the *Start labeling now* pop up, and wait for the analysis to complete.

## Label the 1040 Forms custom model

Now, let's label the fields in the example forms:

1. In the **Label data** page, in the top-right of the page, select **+ Add a field**, and then select **Field**.
1. Type **FirstName** and then press *Enter*.
1. Select the document called **f1040_1.pdf** on the left list, select **John** and then select **FirstName**.
1. In the top-right of the page, select **+ Add a field**, and then select **Field**.
1. Type **LastName** and then press *Enter*.
1. In the document, select **Doe** and then select **LastName**.
1. In the top-right of the page, select **+ Add a field**, and then select **Field**.
1. Type **City** and then press *Enter*.
1. In the document, select **Los Angeles** and then select **City**.
1. In the top-right of the page, select **+ Add a field**, and then select **Field**.
1. Type **State** and then press *Enter*.
1. In the document, select **CA** and then select **State**.
1. Repeat the labeling process for the remaining forms in the list on the left, using the labels you created. Label the same four fields: *FirstName*, *LastName*, *City*, and *State*.

> **IMPORTANT**
> For the purposes of this exercise, we're using only five example forms and labeling only four fields. In your real-world models, you should use as many samples as possible to maximize the accuracy and confidence of your predictions. You should also label all the available fields in the forms, rather than just four fields.

## Train the 1040 Forms custom model

Now that the sample forms are labeled, we can train the first custom model:

1. In the Azure AI Document Intelligence Studio, select **Train**.
1. In the **Train a new model** dialog, in the **Model ID** textbox, type **1040FormsModel**.
1. In the **Build mode** drop-down list, select **Template**, and then select **Train**. 
1. In the **Training in progress** dialog, select **Go to Models**.

## Create the 1099 Forms custom model

Now, you must create a second model, which you'll train on example 1099 tax forms:

1. In Azure AI Document Intelligence Studio, select **Custom extraction model**.
1. Under **My Projects**, select **+ Create a project**.
1. In the **Project name** textbox, type **1099 Forms**, and then select **Continue**.
1. On the **Configure service resource** page, in the **Subscription** drop-down list, select your Azure subscription.
1. In the **Resource group** drop-down list, select **DocumentIntelligenceResources&lt;xxxx&gt;**.
1. In the **Azure AI Document Intelligence or Azure AI Service Resource** drop-down list, select **DocumentIntelligence&lt;xxxx&gt;**.
1. In the **API version** drop-down list, ensure that **20223-10-31-preview** is selected and then select **Continue**.
1. On the **Connnect training data source** page, in the **Subscription** drop-down list, select your Azure subscription.
1. In the **Resource group** drop-down list, select **DocumentIntelligenceResources&lt;xxxx&gt;**.
1. In the **Storage account** drop-down list, select the only storage account listed.
1. In the **Blob container** drop-down list, select **1099examples**, and then select **Continue**.
1. In the **Review and create** page, select **Create project**.
1. Select **Run layout** in the *Start labeling now* pop up, and wait for the analysis to complete.

## Label the 1099 Forms custom model

Now, label the example forms with some fields:

1. In the **Label data** page, in the top-right of the page, select **+ Add a field**, and then select **Field**.
1. Type **FirstName** and then press *Enter*.
1. Select the document called **f1099msc_payer.pdf**, select **John** and then select **FirstName**.
1. In the top-right of the page, select **+ Add a field**, and then select **Field**.
1. Type **LastName** and then press *Enter*.
1. In the document, select **Doe** and then select **LastName**.
1. In the top-right of the page, select **+ Add a field**, and then select **Field**.
1. Type **City** and then press *Enter*.
1. In the document, select **New Haven** and then select **City**.
1. In the top-right of the page, select **+ Add a field**, and then select **Field**.
1. Type **State** and then press *Enter*.
1. In the document, select **CT** and then select **State**.
1. Repeat the labeling process for the remaining forms in the list on the left. Label the same four fields: *FirstName*, *LastName*, *City*, and *State*.

## Train the 1099 Forms custom model

You can now train the second custom model:

1. In the Azure AI Document Intelligence Studio, select **Train**.
1. In the **Train a new model** dialog, in the **Model ID** textbox, type **1099FormsModel**.
1. In the **Build mode** drop-down list, select **Template**, and then select **Train**.
1. In the **Training in progress** dialog, select **Go to Models**.
1. The training process can take a few minutes. Refresh the browser occasionally until both models display the **succeeded** status.

## Create and assemble a composed model

The two custom models, which analyze 1040 and 1099 tax forms, are now complete. You can proceed to create the composed model:

1. In the Azure AI Document Intelligence Models page, select both **1040FormsModel** and **1099FormsModel**.
1. At the top of the list of models, select **Compose**.
1. In the **Compose a new model** dialog, in the **Model ID** textbox, type **TaxFormsModel** and then select **Compose**. Azure AI Document Intelligence creates the composed model and displays it in the list of custom models:

## Use the composed model

Now that the composed model is complete, let's test it with an example form:

1. In the Azure AI Document Intelligence Studio, select the **Test** page, select the  **TaxFormsModel** from the dropdown.
1. Select **Browse for files** and then browse to the location where you cloned the repository.
1. Select **03-composed-model/trainingdata/TestDoc/f1040_7.pdf**, and then select **Open**.
1. Select **Run analysis**. Azure AI Document Intelligence analyses the form by using the composed model.
1. The document you analyzed is an example of the 1040 tax form. Check the **DocType** property to see if the correct custom model has been used. Also check the **FirstName**, **LastName**, **City**, and **State** values identified by the model.

## Clean up resources

Now that you've seen how composed models work, let's remove the resources you created in your Azure subscription.

1. In the **Azure portal** at `https://portal.azure.com/`, select **Resource groups**.
1. In the list of **Resource groups**, select the **DocumentIntelligenceResources&lt;xxxx&gt;** that you created, and then select **Delete resource group**.
1. In the **TYPE THE RESOURCE GROUP NAME** textbox, type the name of the resource group, and then select **Delete** to delete the Document Intelligence resource and the storage account.

## Learn more

- [Compose custom models](/azure/ai-services/document-intelligence/concept-composed-models)
