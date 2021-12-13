# Google cloud
## Starting a new project
To star a new project in google cloud we can go to the:
[Firebase console](https://console.firebase.google.com) or
create it from [Google cloud platform console](https://console.cloud.google.com)

## Creating a virtual environment
Execute the following  command
```
python -m venv venv
```
Then to activate the virtual environment we go the the folder venv and type:
```
cd venv
Scripts\activate venv
```
In order to add new packages we create a file called requirements.txt and execute:
```
pip install -r requirements.txt
```
##Deploying the function
First, set the project ID with the following command

```
gcloud config set project [YOUR PROJECT ID]
```
Then we deploy our function with this command

```
gcloud functions deploy [FUNCTION NAME] --runtime python37 --trigger-http
```
