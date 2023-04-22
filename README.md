<h1>This project aim to build a real time microphone conversational chatbot connected with chatGPT</h1>

<div> I build the project on Windows so it might have a few diffrences for linux users since PowerShell is used. But
I belive there is a work around Good luck though :man_shrugging:
        
        
</div> <br>
  
  
 
<div>Requirements:
        <ul>
            <li> Azure Portal Account</li>
            <li> OpenAI Account</li>
            <li> Python</li>
            <li> Microphone</li>
        </ul>
</div>

<br>        
<h3> starting with Azure Portal</h3>

<br>
<br>

![Microsoft_Azure-Logo_resized](https://user-images.githubusercontent.com/60922667/233615952-f25ca77d-bc3e-4379-89db-10a2189bb58b.png)

<br>
<br>


<p> Create an account in the Microsoft Azure Portal: https://azure.microsoft.com/en-us/free/ -->
!!!Note: creating an account will require credit card information but don't worry the services used in this project are FREE </p>
<p> After creating an account head to the Azure Potal main page at the top of the screen and search for Cognitive services </p> 

![Cognitive_Search_updated](https://user-images.githubusercontent.com/60922667/233621297-f020f8af-7bdd-496c-a862-d78499dcc35b.jpg)

<p> Next look for Speech Service </p> 

![Speech_Services_updated](https://user-images.githubusercontent.com/60922667/233622246-7fca7743-4ad4-4101-bf5f-5dd67ef37647.jpg)

<p> hit create </p> 

<div> Fill up the basic requiremnts
<ul>
        <li>Choose a subscription ---> (A subscription should be created by default along with the account if not just create one)</li>
        <li>Create a resource Group </li>
        <li>Choose a region the suites you </li>
        <li>Create an instance name </li>
        <li>Select the free tier (F0) from the Pricing tier options, for more informations just click "View full pricing details" </li>
</ul>
</div>

<p> Leave the default options for network, identity, and tags, or feel free to change them if you know what you are doing <p>
<p> When everything is done jump to (Review + create), it will display all of the configurations you made just simply click on create </p> 
<p> the generating process will only take a few seconds </p> 

<p> Next search for resource groups in the top of the screen then click on it, the resource group that was created earlier should be visible there, and inside of it will be the speech service. </p>

<p> Two things are required from inside the speech service Key and Region </p>



![Key_And_Region_updated](https://user-images.githubusercontent.com/60922667/233783910-3cbc1d4e-a85f-4c3a-bc33-42b0f1318f28.jpg)

<p> Now the azure part is done. Next configure the SPX through powershell using the following command: </p>

```
dotnet tool install --global Microsoft.CognitiveServices.Speech.CLI 
```
<p> SPX should be configured, next save your speech key and region that was aquired from speech service by using the following command </p>

```
spx --% config @key --set SPEECH-KEY
```
```
spx --% config @region --set SPEECH-REGION
```



<p>!!!Note:  Microsoft Visual C++ Redistributable for Visual Studio 2019 and .NET 6 are required. Instructions can be found here https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/spx-basics?tabs=windowsinstall%2Cpowershell</p>

<p>Viola now the speech recognition should b working. To try it type </p> 

```
spx recognize --microphone
``` 
<p>can't see anythig on the screen, try changing the microhone input through windows settings:  Start > Settings > System > Sound, make sure that the right microphone is in use. </p>


<h3> Moving the OpenAI </h3>


![OpenAI](https://user-images.githubusercontent.com/60922667/233785126-79c27190-68d9-4ea7-aefb-2bb9c45c5759.png)

<p>The openai part is really simple we only need to aquire the api key in order to use in our code, create an account on the openai website </p>













