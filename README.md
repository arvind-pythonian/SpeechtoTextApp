### Speech Transcription using Flask Web Application ###
Speech Recognition is an important feature in several applications used such as home automation, artificial intelligence, etc.  
This aims on how to make use of the SpeechRecognition library of Python which can be easily integrated with flask to perform these functionalities in browser.

### install mongodb ###
Download and install latest version of mongodb server from it's official website.

### Architecture ###
https://1drv.ms/p/s!AmD756sp9GbsjSok1QhKycubiGIZ?e=0x1M4U

### install depndencies ###
Linux:
$ sudo pip3 install -r requirements.txt
Windows:
pip install -r requirements.txt
Running the Application:
Linux:
$ python3 voiceRecorder.py run
Windows:
python voiceRecorder.py run
 Note: The Application is built in windows environment


### Viewing the app ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/

1. Select start listening
2. then select start and speak
3. click stop to view transcription

Technologies Used:
1. Framework : Flask
2. Languages: Python, HTML, Javascript, Jquery, Bootstrap
3. Database: MongoDB


### You can view the transcriptions through MongoDB GUI Client.
The Application is hosted on local machine. ###