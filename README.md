# RunningChess
A chess game that uses milage as points instead of turns 

To Play the game, one must have a strava account: https://www.strava.com/

As the host, one must follow the steps in this video to get valid keys: 

Video 1 (Getting Credentials to Host game): https://www.youtube.com/watch?v=sgscChKfGyg&list=PLO6KswO64zVvcRyk0G0MAzh5oKMLb6rTW&index=1&ab_channel=franchyze923

Video 2 (Updating key type to activity:read_all : https://www.youtube.com/watch?v=sgscChKfGyg&list=PLO6KswO64zVvcRyk0G0MAzh5oKMLb6rTW&index=1&ab_channel=franchyze923

Compile:
1) Make a strava account
2) Go to settings my api application and fill it out
3) Follow the videos above to get your updated access token and refresh token
4) Download and open the file in a Python IDE
5) Choose a python interpreter (Python 3.9.7 64-bit used during creation)
6) pip install requests and urllib3 (This may already be installed
7) Replace the Uppercase variables in payload with the actual values found on your "my api application" and the two tokens created while following the video
8) Run the program
