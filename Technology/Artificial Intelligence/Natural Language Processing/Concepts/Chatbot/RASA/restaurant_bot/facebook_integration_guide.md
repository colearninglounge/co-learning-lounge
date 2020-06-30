**RASA FACEBOOK INTEGRATION**

Once you have created your bot using rasa and tested it, you would be eagerly waiting to share it with the world. This task of sharing the bot with the rest of the world can be easily accomplished by integrating the bot to an online platform. 
There are various platforms to which RASA integration is supported, such as:
- Facebook Messenger
- Slack
- Telegram
- To your own website

Here you will see how to integrate your RASA Bot with Facebook Messenger.

To integrate the bot with Facebook messenger, the file you will be needing to work with is credentials.yml of your project directory.

In this file, you need to update the facebook integration requirements which is already mentioned in comment form. There are 3 requirements to it:
- Verify
- Secret
- page-access-token

**Step-1**: Verify: In the verify section, you can put the name of the bot.
<p align="center">
  <img width="700" height="100" src="fb images/verify.png" alt="Verify script">
</p>

**Step-2**: Now you have to get a secret and page-access-token. For this, you have to visit facebook developers website.

**Step-3:** Here, in the top menu, you have an option for My Apps. Click on My Apps, and then click on Create App.
This will land you into your facebook for developers account. Here, search for Messenger, and click on set up.
<p align="center">
  <img width="600" height="250" src="fb images/fb_developer.png" alt="Facebook Developer Account">
</p>

**Step-4**: You have landed in your bot’s settings page. Here, scroll down to the Access Token menu.
To generate access token, you firstly need to link the bot to your facebook page. So, here you get two options for it, either to create a new page or to link with an existing page. You can choose accordingly here.

**Step-5**: Once the page is linked successfully to your bot, you will get a list showing your page and an option to Generate Token. Click on Generate Token, copy the token and paste it against page-access-token in the credentials.yml file in your chatbot directory.
<p align="center">
  <img width="600" height="250" src="fb images/Token_generated.jpg" alt="Token Generated">
</p>

**Step-6**: Now you are left with the Secret. To get this, go to settings in the left menu, and in drag-down select Basic. There, you will find App Secret, click on show. It will ask for your password. Once the password is entered, you will get the code that you have to paste against Secret in credentials.yml file.
<p align="center">
  <img width="600" height="300" src="fb images/app_secret.jpg" alt="App Secret">
</p>

**Step-7**: As a last and another mandatory step, you should also mention callback url. For this, go to Messenger and then settings. On scrolling you will see a Webhooks tab. Click on add a callback url. In this you have to mention verify (from credentials.yml file) and a callback url.
A callback url looks like this:

_http://localhost:5005/webhooks/facebook/webhook_
<p align="center">
  <img width="600" height="250" src="fb images/callback_url.jpg" alt="Callback url">
</p>

There are two ways to mention a callback url. 
If you have your own website, use that url
If not having your own website, you can use ngrok to get a shareable url. In the terminal simply write _./ngrok http 5005_. Once executed, copy the https link and use it in callback url. 
<p align="center">
  <img width="600" height="200" src="fb images/ngrok.jpg" alt="ngrok">
</p>

Before you click on verify and save, open terminal and execute the command ‘rasa run’. Once the command is executed, click on verify and save. 

**Step-8**: Now in Add Subscription and select messaging and messaging_postback. And you are all set.

**Search for your bot in messenger, and start your conversation with it. Make sure to run action server terminal.** 

