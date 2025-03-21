# raspify
Raspify, the open-source Rapsberry Pi Spotify controller.
## Install guide
**! IN ORDER TO BE ABLE TO USE THIS PROJECT, YOU MUST HAVE SPOTIFY PREMIUM !**

In order to be able to use this project, you must install some libraries by running this code in your console:
```pip install spotipy```
```pip install pygame```
```pip install os```
```pip install dotenv```
```pip install io```
```pip install requests```
Alternatively, you can use ```pip3 install``` if you have installed Python 3.4 or above.

Create a folder named "raspify" and copy the code in it.
Change the item values of `client_id` and `client_secret` from the file `.env`.
Done!
## Personalization Guide
If you want to change my beautiful artwork, you can change the files titled
`previous.png` `pause.png` `next.png`
If you want to change the fons, you can either add a new font file with the same name or add your font file and change the names of the fonts on lines 30 and 31 to your font name.
## Credits
Thanks to [pygame](pygame.org) and [spotipy](https://spotipy.readthedocs.io/en/2.25.1/) for making this project possible. Also, check out [Spotify](https://open.spotify.com).
