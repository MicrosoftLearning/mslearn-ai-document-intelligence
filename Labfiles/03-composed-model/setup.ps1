# Variables
$randomIdentifier = (New-Guid).ToString().Substring(0,4)
$resourceGroupName = "DocumentIntelligenceResources$randomIdentifier"
$storageAccName = "docintelstorage$randomIdentifier"
$docIntelligenceName = "DocumentIntelligence$randomIdentifier"

# Set up the resource group
Write-Output "Setting up the $resourceGroupName resource group."
az group create --location westus2 `
                --name $resourceGroupName
                
# Set up the Azure Storage account
Write-Output "Setting up the $storageAccName storage account."
az storage account create --name $storageAccName `
                          --resource-group $resourceGroupName `
                          --kind StorageV2 `
                          --sku Standard_LRS `
                          --allow-blob-public-access true

# Get the connection string for the new storage account
$connectionString=$(az storage account show-connection-string --name $storageAccName --key key1 --query connectionString)

# Enable CORS on the storage account
az storage cors add --methods DELETE GET HEAD MERGE OPTIONS POST PUT --origins * --services b --allowed-headers * --max-age 200 --exposed-headers * --connection-string $connectionString

# Create the storage containers
Write-Output "Creating containers for the sample forms."
az storage container create --account-name $storageAccName --name 1040examples --connection-string $connectionString
az storage container create --account-name $storageAccName --name 1099examples --connection-string $connectionString
az storage container create --account-name $storageAccName --name testdoc --connection-string $connectionString

# Upload the sample data
Write-Output "Uploading the sample forms to the storage account."
az storage blob upload-batch -d 1040examples --account-name $storageAccName --connection-string $connectionString -s "trainingdata/1040examples" --pattern *.pdf
az storage blob upload-batch -d 1099examples --account-name $storageAccName --connection-string $connectionString -s "trainingdata/1099examples" --pattern *.pdf
az storage blob upload-batch -d testdoc --account-name $storageAccName --connection-string $connectionString -s "trainingdata/TestDoc" --pattern *.pdf
Write-Output "Uploaded sample data."

# Create the Forms Recognizer resource
Write-Output "Setting up the Document Intelligence resource."
az cognitiveservices account create --kind FormRecognizer --location westus2 --name $docIntelligenceName --resource-group $resourceGroupName --sku F0 --yes