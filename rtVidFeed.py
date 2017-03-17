# Requires rt_api by NickMolloy to be installed
# https://github.com/NickMolloy/rt_api
# ~/pip install rt_api
import itertools
import pickle
import json
import requests
import sys
from rt_api.api import Api

# !!!!! NOTE: ON FIRST RUN THIS WILL SPAM YOUR CHANNEL(S) WITH ALL 25 NEW EPISODES !!!!!!

# Creating API Instance
api = Api()

# Loading settings from file
f = open('vidfeed.settings', 'rb')
channel, username, password, main_feed, first_feed, webhook_avatar, latest_ep = pickle.load(f)
f.close()

# Setting the Webhook header
webhook_header = {'content-type': 'application/json'}

# Logging into Rooster Teeth
api.authenticate(username, password)

# Get 25 latest episodes
episode_feed = api.episodes(site=channel, count="25")

# Turn Episodes into List
latest_episodes = list(itertools.islice(episode_feed, 25))

for episode in latest_episodes:
	has_set = 0

	if episode.id_ == latest_ep:
		print("No new episodes. Exiting")
		sys.exit(1)
		# Ends the script if no new videos have been posted

	if episode.is_sponsor_only:
		print("New FIRST-only episode")
		# Send Webhook to FIRST feed
		first_webhook = {
		"avatar_url": "" + webhook_avatar + "",
		"content": "**" + episode.title + "**\n:star: FIRST Members Only!\n" + episode.canonical_url +"",
		}
		response = requests.post(first_feed, data=json.dumps(first_webhook), headers=webhook_header)
		has_set = 1

	if has_set == 0:
		print("New episode")
		# Send Webhook to MAIN feed
		main_webhook = {
		"avatar_url": "" + webhook_avatar + "",
		"content": "**" + episode.title + "**\n" + episode.canonical_url +"",
		}
		response = requests.post(main_feed, data=json.dumps(main_webhook), headers=webhook_header)
		has_set = 1

# Cache newest episode at runtime
latest_ep = latest_episodes[0].id_

# Save settings
f = open('vidfeed.settings', 'wb')
pickle.dump([channel, username, password, main_feed, first_feed, webhook_avatar, latest_ep], f)
f.close()
