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
1. Wait while additional files are installed to support the C# code projects in the repo.

    > **Note**: If you are prompted to add required assets to build and debug, select **Not Now**.

1. Right click on the **03-composed-model** directory, open in the integrated terminal, and execute the setup script:

   ``` bash
   bash setup.sh
   ```

## Create the 1040 Forms custom model

To create a composed model, we must first create two or more custom models. To create the first custom model:

1. In a new browser tab, start the [Azure AI Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio).
1. Scroll down, and then under **Custom model**, select **Custom model**.
1. If you're asked to sign into your account, use your Azure credentials.
1. If you're asked which Azure AI Document Intelligence resource to use, select the subscription and resource name you used when you created the Azure AI Document Intelligence resource.
1. Under **My Projects**, select **+ Create a project**.
1. In the **Project name** textbox, type **1040 Forms**, and then select **Continue**.
1. On the **Configure service resource** page, in the **Subscription** drop-down list, select your Azure subscription.
1. In the **Resource group** drop-down list, select **DocumentIntelligenceResources**.
1. In the **Azure AI Document Intelligence or Azure AI Service Resource** drop-down list, select **DocumentIntelligence**
1. In the **API version** drop-down list, ensure that **2022-06-30-preview** is selected and then select **Continue**.

    :::image type="content" source="../media/4-configure-service-resources.png" alt-text="Screenshot showing the Configure service resources page in Azure AI Document Intelligence Studio custom model wizard." lightbox="../media/4-configure-service-resources.png":::

1. On the **Configure training data source** page, in the **Subscription** drop-down list, select your Azure subscription.
1. In the **Resource group** drop-down list, select **DocumentIntelligenceResources**.
1. In the **Storage account** drop-down list, select the only storage account listed.
1. In the **Blob container** drop-down list, select **1040examples**, and then select **Continue**.

    :::image type="content" source="../media/4-connect-training-data-source.png" alt-text="Screenshot showing the Connect training data source page in Azure AI Document Intelligence Studio custom model wizard." lightbox="../media/4-connect-training-data-source.png":::

1. In the **Review and create** page, select **Create project**.

## Label the 1040 Forms custom model

Now, let's label the fields in the example forms:

1. In the **Label data** page, in the top-right of the page, select **+**, and then select **Field**.

    :::image type="content" source="../media/4-add-label.png" alt-text="Screenshot showing how to add a new label in Azure AI Document Intelligence Studio." lightbox="../media/4-add-label.png":::

1. Type **FirstName** and then press <kbd>Enter</kbd>.
1. In the document, select **John** and then select **FirstName**.

    :::image type="content" source="../media/4-label-first-name.png" alt-text="Screenshot showing how to complete a new label in Azure AI Document Intelligence Studio." lightbox="../media/4-label-first-name.png":::

1. In the top-right of the page, select **+**, and then select **Field**.
1. Type **LastName** and then press <kbd>Enter</kbd>.
1. In the document, select **Doe** and then select **LastName**.
1. In the top-right of the page, select **+**, and then select **Field**.
1. Type **City** and then press <kbd>Enter</kbd>.
1. In the document, select **Los Angeles** and then select **City**.
1. In the top-right of the page, select **+**, and then select **Field**.
1. Type **State** and then press <kbd>Enter</kbd>.
1. In the document, select **CA** and then select **State**.
1. Repeat the labeling process for the remaining forms in the list on the left. Label the same four fields: *FirstName*, *LastName*, *City*, and *State*.

> [!IMPORTANT]
> For the purposes of this exercise, we're using only five example forms and labeling only four fields. In your real-world models, you should use as many samples as possible to maximize the accuracy and confidence of your predictions. You should also label all the available fields in the forms, rather than just four fields.

## Train the 1040 Forms custom model

Now that the sample forms are labeled, we can train the first custom model:

1. In the Azure AI Document Intelligence Studio, select **Train**.
1. In the **Train a new model** dialog, in the **Model ID** textbox, type **1040FormsModel**.
1. In the **Build mode** drop-down list, select **Template**, and then select **Train**. 
1. In the **Training in progress** dialog, select **Go to Models**.

## Create the 1099 Forms custom model

Now, you must create a second model, which you'll train on example 1099 tax forms:

1. In Azure AI Document Intelligence Studio, select **Custom model**.
1. Under **My Projects**, select **+ Create a project**.
1. In the **Project name** textbox, type **1099 Forms**, and then select **Continue**.
1. On the **Configure service resource** page, in the **Subscription** drop-down list, select your Azure subscription.
1. In the **Resource group** drop-down list, select **DocumentIntelligenceResources**.
1. In the **Azure AI Document Intelligence or Azure AI Service Resource** drop-down list, select **DocumentIntelligence**
1. In the **API version** drop-down list, ensure that **2022-06-30-preview** is selected and then select **Continue**.

    :::image type="content" source="../media/4-configure-service-resources.png" alt-text="Screenshot showing the Configure service resources page in Azure AI Document Intelligence Studio custom model wizard." lightbox="../media/4-configure-service-resources.png":::

1. On the **Configure training data source** page, in the **Subscription** drop-down list, select your Azure subscription.
1. In the **Resource group** drop-down list, select **DocumentIntelligenceResources**.
1. In the **Storage account** drop-down list, select the only storage account listed.
1. In the **Blob container** drop-down list, select **1099examples**, and then select **Continue**.
1. In the **Review and create** page, select **Create project**.

## Label the 1099 Forms custom model

Now, label the example forms with some fields:

1. In the **Label data** page, in the top-right of the page, select **+**, and then select **Field**.
1. Type **FirstName** and then press <kbd>Enter</kbd>.
1. In the document, select **John** and then select **FirstName**.
1. In the top-right of the page, select **+**, and then select **Field**.
1. Type **LastName** and then press <kbd>Enter</kbd>.
1. In the document, select **Doe** and then select **LastName**.
1. In the top-right of the page, select **+**, and then select **Field**.
1. Type **City** and then press <kbd>Enter</kbd>.
1. In the document, select **New Haven** and then select **City**.
1. In the top-right of the page, select **+**, and then select **Field**.
1. Type **State** and then press <kbd>Enter</kbd>.
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

    :::image type="content" source="../media/4-start-compose-model.png" alt-text="Screenshot showing how to begin composing a model in Azure AI Document Intelligence Studio." lightbox="../media/4-start-compose-model.png":::

1. In the **Compose a new model** dialog, in the **Model ID** textbox, type **TaxFormsModel** and then select **Compose**. Azure AI Document Intelligence creates the composed model and displays it in the list of custom models:

## Use the composed model

Now that the composed model is complete, let's test it with an example form:

1. In the [Azure portal](https://portal.azure.com/learn.docs.microsoft.com?azure-portal=true), select **All resources** and then select the **formsrecstorage&lt;xxxxx&gt;** storage account, where &lt;xxxxx&gt; is a random number.
1. Under **Data storage** select **Containers** and then select **TestDoc**.
1. To the right of **f1040_7.pdf**, select **...** and then select **Download**.
1. Save the PDF document to your local computer and make a note of the saved location.
1. In the Azure AI Document Intelligence Studio, select **TaxFormsModel**, and then select **Test**.
1. Select **+ Add** and then browse to the location where you saved the PDF document.
1. Select **f1040_7.pdf**, and then select **Open**.
1. Select **Analyze**. Azure AI Document Intelligence analyses the form by using the composed model.

    :::image type="content" source="../media/4-composed-model-analysis.png" alt-text="Screenshot showing how to use a composed model in Azure AI Document Intelligence Studio." lightbox="../media/4-composed-model-analysis.png":::

1. The document you analyzed is an example of the 1040 tax form. Check the **DocType** property to see if the correct custom model has been used. Also check the **FirstName**, **LastName**, **City**, and **State** values identified by the model.

## Clean up the exercise resources

Now that you've seen how composed models work, let's remove the resources you created in your Azure subscription.

1. In the [Azure portal](https://portal.azure.com/learn.docs.microsoft.com?azure-portal=true), select **Resource groups**.
1. In the list of **Resource groups**, select **DocumentIntelligenceResources**, and then select **Delete resource group**. 
1. In the **TYPE THE RESOURCE GROUP NAME** textbox, type **DocumentIntelligenceResources** and then select **Delete** to delete the Document Intelligence resource and the storage account.

## Learn more

- [Compose custom models](/azure/ai-services/document-intelligence/concept-composed-models)
- [Build your training dataset for a custom model](/azure/applied-ai-services/form-recognizer/how-to-guides/build-custom-model-v3)
