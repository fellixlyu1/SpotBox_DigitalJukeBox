# SpotBox_DigitalJukeBox
SpotBox is a digital jukebox web app that connects with your Spotify account for you and other users to add songs to the current playlist!

To begin, you'll need a Spotify account, a Spotify developer account, and a safe Wi-Fi connection. To create a developer account, go to: developer.spotify.com. Once you've created your Developer account, go to the "Dashboard" and click the "Create App" button. Once you've created your app, go to the settings and copy the "Client ID" and the "Client Secret" at the top.

<img width="1280" alt="Screen Shot 2023-08-29 at 10 58 24 AM" src="https://github.com/fellixlyu1/SpotBox_DigitalJukeBox/assets/116593040/27fe4beb-e25e-4afb-9101-d3d34e469e57">

Scroll down and you'll find a section for "Redirect URI". You can use your localhost to callback the program. By this point, you have your Spotify account username, Client ID, Client Secret, and the redirect URI. Create a .env file and fill out the information in the following format:
USERNAME=(your username here)
CLIENT_ID=(your client id here)
CLIENT_SECRET=(your client secret here)
REDIRECT_URI=(your redirect uri here)

<img width="1280" alt="Screen Shot 2023-08-29 at 11 01 28 AM" src="https://github.com/fellixlyu1/SpotBox_DigitalJukeBox/assets/116593040/05aba58f-1078-455b-9b52-a41af5abd40f">

Once you've finished the following instructions, you may run the program and click on the link in the terminal with your IP address and the web app will appear!
