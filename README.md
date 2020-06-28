# Reddit Autoreplier

Small Reddit bot script that replies to comments using key phrases. Built using [PRAW](https://github.com/praw-dev/praw), requires Python 3.7+.

## Generating Credentials

1. Login into https://www.reddit.com/prefs/apps using a preexisting Reddit account. Mature accounts are less-likely to be rate-limited by Reddit's API.

2. Select create app. Select the "script" option. Enter a name and a redirect url _(can be anything, but usually is the url to your Reddit account)_.

3. Copy the generated client secret and client id _(located below application's name)_ into `praw.ini`.

4. Then, run:

```bash
python3 main.py
```

5. The bot will search and reply for posts in [testingground4bots](https://reddit.com/r/testingground4bots). This is a subreddit designed for testing bots with little consequence.

## Configuration

In `main.py`, the following are set as defaults and can be configured:

```python
TARGET_SUBREDDIT = "testingground4bots"
MAX_LENGTH = 20
SEARCH_PHRASE = "!dropthemic"
DELETE_PHRASE = "delete pls"
REPLY_PHRASE = '''#🎤 Drop.

***

^(I'm a bot. Reply with **delete pls** to remove.)
'''
```

`REPLY_PHRASE` follows Reddit's formatting conventions, including line breaks. Python's multi-line strings are recommended here.

`TARGET_SUBREDDIT` can be changed to the desired subreddit after configuring and testing the script. ALWAYS confirm with the subreddit's moderators before changing the bot's target. Testing new search and delete phrases is safest in the [testingground4bots](https://reddit.com/r/testingground4bots) subreddit.

## TODO

- [ ] Handle rate-limiting errors more gracefully
- [ ] Refactor script to be asynchronous
- [ ] Move config vars in main.py to praw.ini (and/or, switch to TOML/JSON)
