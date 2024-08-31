# DPS_Challenge
Repository for the DPS Challenge

**CHALLENGE DETAILS**
Challenge is intended for **Artificial Intelligence Engineer** applicant.

## Mission 1: Create an AI Model

**Description:** Download the “Monatszahlen Verkehrsunfälle” Dataset from the München Open Data Portal. [Link to download the Dataset](https://www.opengov-muenchen.de/dataset/5e73a82b-7cfb-40cc-9b30-45fe5a3fa24e/resource/40094bd6-f82d-4979-949b-26c8dc00b9a7/download/210619monatszahlenjuni2021monatszahlen2106verkehrsunfaelle.csv)

Here you see the number of accidents for specific categories per month. Important are the first 5 columns:
- Category
- Accident-type (insgesamt means total for all subcategories)
- Year
- Month
- Value

Your **goal** would be to visualise historically the number of accidents per category (column1). The dataset currently contains values until the end of 2020. Create an application that forecasts the values for:
- Category: 'Alkoholunfälle'
- Type: 'insgesamt
- Year: '2021'
- Month: '01'

## Mission 2: Publish your source code & Deploy
**Description:** Publish your source code in a github repository. It should both contain the code how you made it and the visualisation itself (as an image). We’d like to see the steps how you arrived at the solution, so please make sure to commit every step you did and not just the final application in 1 or 2 commits.

The next step is to deploy the model. You would need to create an endpoint that returns your predictions. Make sure that your endpoint accepts a POST request with a JSON body like this:
 
{
"year":2020,
"month":10
}

And it should return your applications prediction in the following format:
 
{
"prediction":value
}

The model can be deployed to a cloud service. You can use (aws, google cloud, heroku or whatever you prefer, they usually all provide a freetier).

## Mission 3: Send us the URL of your work
