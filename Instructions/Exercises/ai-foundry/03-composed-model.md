---
lab:
    title: 'Create a composed Document Intelligence model'
    module: 'Module 6 - Document Intelligence'
---

# Create a composed Document Intelligence model

In this exercise, you'll create and train two custom models that analyze different tax forms. Then, you'll create a composed model that includes both of these custom models. You'll test the model by submitting a form and you'll check that it recognizes the document type and labeled fields correctly.

## Set up resources

We'll use a script to create the Azure AI Document Intelligence resource, a storage account with sample forms, and a resource group:

1. In a browser tab, open the Azure portal at `https://portal.azure.com`, signing in with the Microsoft account associated with your Azure subscription.
1. Once signed in, use the **[\>_]** button to the right of the search bar at the top of the page to create a new Cloud Shell in the Azure portal, selecting a ***PowerShell*** environment. The cloud shell provides a command line interface in a pane at the bottom of the Azure portal.

    > **Note**: If you have previously created a cloud shell that uses a *Bash* environment, switch it to ***PowerShell***.

1. In the cloud shell toolbar, in the **Settings** menu, select **Go to Classic version** (this is required to use the code editor).

    > **Tip**: As you paste commands into the cloudshell, the ouput may take up a large amount of the screen buffer. You can clear the screen by entering the `cls` command to make it easier to focus on each task.

1. In the PowerShell pane, enter the following commands to clone the GitHub repo for this exercise:

    ```
    rm -r mslearn-ai-document-intelligence -f
    git clone https://github.com/microsoftlearning/mslearn-ai-document-intelligence mslearn-ai-document-intelligence
    ```

1. After the repo has been cloned, navigate to the folder containing this exercise's files:  

    ```
   cd mslearn-ai-document-intelligence/Labfiles/03-composed-model
    ```

1. Run the following command to set up resources:

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
1. In the **Document Intelligence or Cognitive Service Resource** drop-down list, select **DocumentIntelligence&lt;xxxx&gt;**.
1. In the **API version** drop-down list, ensure that **2024-11-30 (4.0 General Availability)** is selected and then select **Continue**.
1. On the **Connect training data source** page, in the **Subscription** drop-down list, select your Azure subscription.
1. In the **Resource group** drop-down list, select **DocumentIntelligenceResources&lt;xxxx&gt;**.
1. In the **Storage account** drop-down list, select the only storage account listed. If you have multiple storage accounts in your subscription, choose the one starting with *docintelstorage*
1. In the **Blob container** drop-down list, select **1040examples**, and then select **Continue**.
1. In the **Review and create** page, select **Create project**.
1. Select **Run now** under *Run layout* in the *Start labeling now* pop up, and wait for the analysis to complete.

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
1. Repeat the labeling process for the remaining forms in the list on the left, using the labels you created. Label the same four fields: *FirstName*, *LastName*, *City*, and *State*. Notice that one of the documents does not have city or state data.

> **IMPORTANT**
> For the purposes of this exercise, we're using only five example forms and labeling only four fields. In your real-world models, you should use as many samples as possible to maximize the accuracy and confidence of your predictions. You should also label all the available fields in the forms, rather than just four fields.

## Train the 1040 Forms custom model

Now that the sample forms are labeled, we can train the first custom model:

1. In the Azure AI Document Intelligence Studio, on the top right of the screen, select **Train**.
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
1. In the **Document Intelligence or Cognitive Service Resource** drop-down list, select **DocumentIntelligence&lt;xxxx&gt;**.
1. In the **API version** drop-down list, ensure that **2024-11-30 (4.0 General Availability)** is selected and then select **Continue**.
1. On the **Connnect training data source** page, in the **Subscription** drop-down list, select your Azure subscription.
1. In the **Resource group** drop-down list, select **DocumentIntelligenceResources&lt;xxxx&gt;**.
1. In the **Storage account** drop-down list, select the only storage account listed.
1. In the **Blob container** drop-down list, select **1099examples**, and then select **Continue**.
1. In the **Review and create** page, select **Create project**.
1. Select the drop-down button for **Run layout**  and select **Unanalyzed documents**.
1. Wait for the analysis to complete.

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
1. Repeat the labeling process for the remaining forms in the list on the left. Label the same four fields: *FirstName*, *LastName*, *City*, and *State*. Notice that two of the documents don't have any name data to label.

## Train the 1099 Forms custom model

You can now train the second custom model:

1. In the Azure AI Document Intelligence Studio, on the top right, select **Train**.
1. In the **Train a new model** dialog, in the **Model ID** textbox, type **1099FormsModel**.
1. In the **Build mode** drop-down list, select **Template**, and then select **Train**.
1. In the **Training in progress** dialog, select **Go to Models**.
1. The training process can take a few minutes. Refresh the browser occasionally until both models display the **succeeded** status.

## Create a custom classification model

Before creating the composed model, you need to create a custom classification model. It will be used to first define which type of form a given input file is before extracting data from it.

1. In Azure AI Document Intelligence Studio home page, select **Custom classification model**.
1. Under **My Projects**, select **+ Create a project**.
1. In the **Project name** textbox, type **Classify Forms**, and then select **Continue**.
1. On the **Configure service resource** page, in the **Subscription** drop-down list, select your Azure subscription.
1. In the **Resource group** drop-down list, select **DocumentIntelligenceResources&lt;xxxx&gt;**.
1. In the **Document Intelligence or Cognitive Service Resource** drop-down list, select **DocumentIntelligence&lt;xxxx&gt;**.
1. In the **API version** drop-down list, ensure that **2024-11-30 (4.0 General Availability)** is selected and then select **Continue**.
1. On the **Connnect training data source** page, in the **Subscription** drop-down list, select your Azure subscription.
1. In the **Resource group** drop-down list, select **DocumentIntelligenceResources&lt;xxxx&gt;**.
1. In the **Storage account** drop-down list, select the only storage account listed.
1. In the **Blob container** drop-down list, select **classifyexamples**, and then select **Continue**.
1. In the **Review and create** page, select **Create project**.

## Label the custom classification model

Now, label the example forms with with each type:

1. In the **Label data** page, in the top-right of the page, select **+ Add type**.
1. Type **1040Form** and then press *Enter*.
1. Select each **f1040...** document and then select **1040Form**.
1. In the top-right of the page, select **+ Add type**.
1. Type **1099Form** and then press *Enter*.
1. Select each **f1099...** document and then select **1099Form**.

## Train the custom classification model

You can now train the custom classification model:

1. In the Azure AI Document Intelligence Studio, on the top right, select **Train**.
1. In the **Train a new model** dialog, in the **Model ID** textbox, type **ClassifyModel**.
1. Check the confirmation checkbox and then select **Train**.
1. In the **Training in progress** dialog, select **Go to Models**.
1. The training process can take a few minutes. Refresh the browser occasionally until the model displays the **succeeded** status.

## Create a composed model

Now that all required models are trained, let's create the composed model:

1. In Azure AI Document Intelligence Studio home page, select **Custom extraction model**.
1. Under **My Projects**, select **+ Create a project**.
1. In the **Project name** textbox, type **Compose Model**, and then select **Continue**.
1. On the **Configure service resource** page, in the **Subscription** drop-down list, select your Azure subscription.
1. In the **Resource group** drop-down list, select **DocumentIntelligenceResources&lt;xxxx&gt;**.
1. In the **Document Intelligence or Cognitive Service Resource** drop-down list, select **DocumentIntelligence&lt;xxxx&gt;**.
1. In the **API version** drop-down list, ensure that **2024-11-30 (4.0 General Availability)** is selected and then select **Continue**.
1. On the **Connnect training data source** page, in the **Subscription** drop-down list, select your Azure subscription.
1. In the **Resource group** drop-down list, select **DocumentIntelligenceResources&lt;xxxx&gt;**.
1. In the **Storage account** drop-down list, select the only storage account listed.
1. In the **Blob container** drop-down list, select **testdoc**, and then select **Continue**.
1. In the **Review and create** page, select **Create project**.
1. In the left pane, select **Models**.
1. In the Models list, select both **1040Forms** and **1099Forms** and then select **Compose**.
1. In the **Compose a new model** dialog, in the **Model ID** textbox, type **ComposeModel**.
1. In the **Classification model** drop-down list, select **ClassifyModel**.
1. In the **1040Form** drop-down list, select **1040FormsModel**.
1. In the **1099Form** drop-down list, select **1099FormsModel**. Then select **Compose**.

## Use the model

Now that the composed model is created, let's test it with an example form:

1. Download the test form at `https://github.com/MicrosoftLearning/mslearn-ai-document-intelligence/raw/refs/heads/main/Labfiles/03-composed-model/trainingdata/TestDoc/f1040_7.pdf`.
1. In the Azure AI Document Intelligence Studio, select the **Models** page, and then select the **ComposeModel**.
1. Select **Test**.
1. Select **Browse for files** and then browse to the location where you downloaded the form.
1. Select **f1040_7.pdf**, and then select **Open**.
1. Select **Run analysis**. Azure AI Document Intelligence analyses the form by using the composed model.
1. The document you analyzed is an example of the 1040 tax form. Check the **DocType** property to see if the correct custom model has been used. Also check the **FirstName**, **LastName**, **City**, and **State** values identified by the model.

## Clean up resources

Now that you've seen how composed models work, let's remove the resources you created in your Azure subscription.

1. In the **Azure portal** at `https://portal.azure.com/`, select **Resource groups**.
1. In the list of **Resource groups**, select the **DocumentIntelligenceResources&lt;xxxx&gt;** that you created, and then select **Delete resource group**.
1. In the **TYPE THE RESOURCE GROUP NAME** textbox, type the name of the resource group, and then select **Delete** to delete the Document Intelligence resource and the storage account.

## Learn more

- [Compose custom models](/azure/ai-services/document-intelligence/concept-composed-models)
