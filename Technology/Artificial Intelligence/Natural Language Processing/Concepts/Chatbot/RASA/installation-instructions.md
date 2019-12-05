# Step 1: Setup and Installation

<div style="border-style: solid; border-color: black; text-align: center; background-color: lightgreen; padding: 5px;">

Step 1:	 Download and install Anaconda Navigator: https://docs.anaconda.com/anaconda/install/

Step 2:	 - Windows user can open Anaconda Prompt (as an Administrator) from the start menu
	 - Linux user can open terminal in sudo mode

Step 3:   Install Virtual Environment, Follow sub-steps Below (Type the following commands step by step in the terminal)-
	  * Check the version of anaconda (latest version should be installed)<br>
	    `conda -V`
         
          * Update the Anaconda Navigator
            `conda update conda`
       
          * Create the virtual Environment
            `conda create -n your_environment_name python=3.7.5 anaconda`
            (replace your_environment_name with any name you want to give to your virtual environment)
            (press y to proceed whenever it will be asked for confirmation)
         
          * Activate your virtual Environment
            `conda activate your_environment_name`
            (replace your_environment_name with the virtual environment name that you have given earlier)

Step 4:   Install Microsoft Visual C++ Build tools: https://go.microsoft.com/fwlink/?LinkId=691126
	  > Note: Linux and Mac operating users can skip this step.

Step 5   Install Rasa Framework and its dependencies by running the following commands in the virtual environment Command Prompt Shell<br>
         `pip install --upgrade rasa-x==0.20.2 --extra-index-url https://pypi.rasa.com/simple`  <br>
	 `pip install rasa[spacy]` <br>
	 `python -m spacy download en_core_web_md`  <br> 
	 `python -m spacy link en_core_web_md en` <br>

          If you have performed everything correctly the try running the following command<br>
          `rasa`

If it doesn’t give any error then Congratulations you have successfully completed the installation and you are ready to build your chatbot.

Step 6:	Getting a Bing Maps Key<br>
        Navigate [here](https://docs.microsoft.com/en-us/bingmaps/getting-started/bing-maps-dev-center-help/getting-a-bing-maps-key) and then click on ‘Bing Maps Key’ hyperlink. 
	After we have signed up (if we do not have an account on Microsoft) and provided our basic information, we can create a key. 
        Bing Maps API provides a ‘basic’ key, by default (i.e. it can be specified directly in the request header, no need of OAuth complexity).
        After the key has been created we can see/ copy it by clicking on ‘My Account’ -> ‘My Keys’.

Step 7:	Create Zomato API<br>
        We will need an API key from Zomato, so navigate to [Zomato](https://developers.zomato.com/api) and ‘request an API key’.
        On being prompted, we may either sign up on Zomato or ‘Continue with Google’. After we have completed the sign up, we should receive the API key

> Update both the keys in [actions.py](./actions.py) file.
