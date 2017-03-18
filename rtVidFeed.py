import itertools
import pickle
import json
import requests
import sys
from rt_api.api import Api

# !!!!! NOTE: ON FIRST RUN THIS WILL ASSUME ALL EPISODES ARE NEW AND SPAM YOUR CHANNEL(S) !!!!!!

# Creating API Instance
api = Api()

# Loading settings from file
f = open('vidfeed.settings', 'rb')
channel, username, password, main_feed, first_feed, webhook_avatar, latest_ep, send_main, send_sponsor = pickle.load(f)
f.close()

# Setting the Webhook header
webhook_header = {'content-type': 'application/json'}

# Logging into Rooster Teeth
api.authenticate(username, password)

# Get 15 latest episodes (This should be way more than they'd ever make live at once)
episode_feed = api.episodes(site=channel, count="15")

# Turn Episodes into List
latest_episodes = list(itertools.islice(episode_feed, 15))

for episode in latest_episodes:
	has_set = False

	if episode.id_ == latest_ep:
		print("No new episodes. Exiting")
		sys.exit(1)
		# Ends the script when it reaches the most recently sent episode

	if send_sponsor and episode.is_sponsor_only:
		print("New FIRST-only episode")
		# Send Webhook to FIRST feed
		first_webhook = {
		"avatar_url": "" + webhook_avatar + "",
		"content": "**" + episode.show_name + " - " + episode.title + "**\n:star: FIRST Members Only!\n" + episode.canonical_url + "",
		}
		response = requests.post(first_feed, data=json.dumps(first_webhook), headers=webhook_header)
		has_set = True

	if send_main and not has_set:
		print("New episode")
		# Send Webhook to MAIN feed
		main_webhook = {
		"avatar_url": "" + webhook_avatar + "",
		"content": "**" + episode.show_name + " - " + episode.title + "**\n" + episode.canonical_url + "",
		}
		response = requests.post(main_feed, data=json.dumps(main_webhook), headers=webhook_header)
		has_set = True

# Cache newest episode at runtime
latest_ep = latest_episodes[0].id_

# Save settings
f = open('vidfeed.settings', 'wb')
pickle.dump([channel, username, password, main_feed, first_feed, webhook_avatar, latest_ep, send_main, send_sponsor], f)
f.close()
