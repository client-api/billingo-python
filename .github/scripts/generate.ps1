
# Clean up

$generatedFilesPath = "./.openapi-generator/FILES"

if (Test-Path -Path $generatedFilesPath) {
    $generatedFiles = Get-Content -Path $generatedFilesPath

    foreach ($generatedFile in $generatedFiles) {
                $generatedFile = $generatedFile.Trim()

        if ($generatedFile -in '.gitignore', '.openapi-generator-ignore', 'README.md', '.github') {
            continue
        }

        if (Test-Path -Path $generatedFile) {
            Remove-Item -Path $generatedFile -Force
        }
    }
}

# Download generator

if (-Not (Test-Path -Path "./.openapi-generator/openapi-generator-cli.jar")) {
    $xmlString = Invoke-WebRequest -Uri "https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/maven-metadata.xml" -UseBasicParsing

    if (-Not $xmlString) {
        Write-Host "Unable to fetch XML metadata."
        exit
    }

    $xml = [xml]$xmlString.Content
    $latestVersion = $xml.metadata.versioning.latest
    $latestVersionUrl = "https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/$latestVersion/openapi-generator-cli-$latestVersion.jar"

    Invoke-WebRequest -Uri $latestVersionUrl -OutFile "./.openapi-generator/openapi-generator-cli.jar"
}

# Check Java

$output = & java -version 2>&1
if ($output -match "java version" -or $output -match "openjdk version") {
    Write-Host "Java version: $output"
} else {
    Write-Host "Java is not found."
    exit 1
}

# Check Generator Version

$output = & java -jar .\.openapi-generator\openapi-generator-cli.jar version 2>&1
if ($output -match "$latestVersion") {
    Write-Host "OpenAPI Generator version: $output"
} else {
    Write-Host "Unable to verify OpenAPI Generator version"
    exit 1
}

# Generate

java -jar ./.openapi-generator/openapi-generator-cli.jar generate `
    --input-spec "./.github/specs/openapi.yml" `
    --generator-name "python" `
    --output ./ `
    --enable-post-process-file `
    --git-host "github.com" `
    --git-repo-id "billingo-python" `
    --git-user-id "client-api" `
    --package-name "clientapi_billingo" `
    --additional-properties "packageName=clientapi_billingo,packageUrl=https://github.com/client-api/billingo-python,packageVersion=2.1.0,projectName=clientapi-billingo"

if ($LASTEXITCODE -eq 0) {
    Write-Host "Done"
} else {
    Write-Host "Failed"
}