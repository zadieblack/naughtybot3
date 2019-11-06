# naughtybot3

This is a combination of two twitter bots. @erotica_ebooks tweets out titles for non-existent self-published erotica ebooks. @bot_lust tweets steamy (and ridiculous) excerpts from those same non-existant books. Both the titles and excerpts are generated from word lists . The tweets are outputted as images for added fanciness. 

This bot was coded in python. It uses the **tweepy** library to access Twitter's API. It uses the **pillow** library to create images.

***WARNING***
*This bot generates explicit adult content! You must be 18+ to use or modify this bot!*

Flaming Lust Bot on Twitter is [@bot_lust](https://twitter.com/bot_lust). Erotica Ebooks is [@erotica_ebooks](https://twitter.com/erotica_ebooks/)

## why combine?
erotica_ebooks and flaming lust bot were orignally separate. They were also multi-threaded so that they could offer a feature that allowed them to tweet back when someone @'d them on twitter. In an effort to continue to maintain the bots on free hosting I have made the decision to combine them and to remove the tweet back feature (which was seldom used). 

I have continued to make improvements on the combined codebase.

However, if you are interested in the multi-threaded reply capabilities of the originals, you might be better off forking one of them. You can find them here:

* https://github.com/zadieblack/flaminglustbot
* https://github.com/zadieblack/erotica_ebooks

## running the bot

The bot uses the python library **tweepy** to access the twitter API. It requires a file called twitterauth.py which is **not** contained in this repo. you must create your own file and include your own twitter authentication codes, obtained from https://apps.twitter.com/.

To run this bot:
```
runbot [-tweet] [-numtweets NUMTWEETS] [-loop] [-test TEST] [-tweettimer TWEETTIMER] 
```
All args optional, but you must include **-tweet** if you want the bot to actually tweet what it generates. run_as_task was designed to run the bot as a task from pythonanywhere.

Standard command line:
```
$ lust_bot -tweet -loop
```
