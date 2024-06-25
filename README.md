<h1>SpotBox: The Spotify Jukebox</h1>
<p>SpotBox is a digital jukebox web app that connects with your Spotify account for you and other users to add songs to the current playlist!</p>

<h3><strong>Spotify Your Life's Most Precious Moments</strong></h3>

<p>Imagine if you can play the song you and your partner met in the restaurant you had your first date! Remember the song you and your partner heard in that romantic setting? Use SpotBox to add that song into the queue.</p>

![pexels-photo-8091344](https://github.com/fellixlyu1/SpotBox_DigitalJukeBox/assets/116593040/0d82251c-5299-44bb-b44a-02a827f777d7)

<h3><strong>Share your music from anywhere!</strong></h3>

<p>Allow friends and family to add songs to the queue during car rides or your life's greatest events!</p>

![pexels-photo-5329290](https://github.com/fellixlyu1/SpotBox_DigitalJukeBox/assets/116593040/7ffb36cd-02c6-40e4-ab42-50b95e612859)

<h2><strong>Setting Up Your Spotify Developer Account</strong></h2>

<p>To begin, you'll need a Spotify account, a Spotify developer account, and a safe Wi-Fi connection. To create a developer account, go to: developer.spotify.com. Once you've created your Developer account, go to the "Dashboard" and click the "Create App" button. Once you've created your app, go to the settings and copy the "Client ID" and the "Client Secret" at the top.</p>

![Screenshot 2024-06-24 11 29 10 AM](https://github.com/fellixlyu1/SpotBox_DigitalJukeBox/assets/116593040/83c52db4-0761-4edb-86bc-5d813577d876)


![Screenshot 2024-06-24 11 29 43 AM](https://github.com/fellixlyu1/SpotBox_DigitalJukeBox/assets/116593040/dfc2bb7c-064f-4c41-87b9-d328e31c7a03)
<p></p>

<h3><strong>Find The Client ID and Client Secret</strong></h3>

<p>Scroll down and you'll find a section for "Redirect URI". You can use your localhost to callback the program. By this point, you have your Spotify account username, Client ID, Client Secret, and the redirect URI. 

![Screenshot 2024-06-24 11 34 28 AM](https://github.com/fellixlyu1/SpotBox_DigitalJukeBox/assets/116593040/e01a91ad-0dc1-4629-8008-1258df9b5f13)

Create a .env file and fill out the information in the following format:</p>
<p>USERNAME=(your username here)</p>
<p>CLIENT_ID=(your client id here)</p>
<p>CLIENT_SECRET=(your client secret here)</p>
<p>REDIRECT_URI=(your redirect uri here)</p>

![Screenshot 2024-06-24 2 50 30 PM](https://github.com/fellixlyu1/SpotBox_DigitalJukeBox/assets/116593040/008c79d4-6716-4cb7-b744-e4e7834d9a21)

<p>Once you've finished the following instructions, you may run the program and click on the link in the terminal with your IP address and the web app will appear!</p>

<h2><strong>Dependencies Required for SpotBox</strong></h2>

<p>There are certain dependencies you as a developer or a tester will have to consider installing. In the terminal of your IDE, you'll need to install: </p>
<ul>- pip</ul>
<ul>- flask</ul>
<ul>- gunicorn</ul>

<h2><strong>Test It Out!</strong></h2>

<p>Before you even run the program and start adding songs, you'll need to use Spotify and play either one of your playlists or any song of choice. Once that is done, your SpotBox app should start working</p>

<h4><strong>Checking Out the Current Track</strong></h4>

![Screenshot 2024-06-24 2 59 51 PM](https://github.com/fellixlyu1/SpotBox_DigitalJukeBox/assets/116593040/dfe84e5a-2df0-4b6f-b36c-50b388852f91)

![Screenshot 2024-06-24 3 00 14 PM](https://github.com/fellixlyu1/SpotBox_DigitalJukeBox/assets/116593040/130143c2-9fe2-46de-9c1a-535ef6db2a7d)

![Screenshot_20240624-150051_Spotify](https://github.com/fellixlyu1/SpotBox_DigitalJukeBox/assets/116593040/7d35776c-3f2b-4206-9df5-ed868b92cdb8)

<h4><strong>Adding a Track to the Queue</strong></h4>

![Screenshot 2024-06-24 3 00 27 PM](https://github.com/fellixlyu1/SpotBox_DigitalJukeBox/assets/116593040/6773cd58-fcb5-49ab-a4c3-4df7e1f75294)

![Screenshot 2024-06-24 3 00 33 PM](https://github.com/fellixlyu1/SpotBox_DigitalJukeBox/assets/116593040/5ae58af1-a565-4b4b-8903-e6bf17568ff6)

![Screenshot_20240624-150103_Spotify](https://github.com/fellixlyu1/SpotBox_DigitalJukeBox/assets/116593040/c65b8627-b6bc-420c-974f-c6f15a9afb4c)

