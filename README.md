#rtVidFeed
Rooster Teeth videos to Discord Webhooks via python
------

Made for the Rooster Teeth/Let's Play family of Discord Servers, but feel free to use and modify it for anything.  
*I barely know python, so this is probably hacked together just barely enough to function...*

Come join us on Discord:  
[Rooster Teeth Community](https://https//discord.gg/roosterteeth)  
[FunHaus Community](https://discord.gg/ecWNNZx)  
[Achievement Hunter Community](https://discord.gg/P8cJ9vC)  
[Cow Chop Community](https://discord.gg/cowchop)  
[Kinda Funny](https://discord.gg/kindafunny)  
[The Creatures Community](https://discord.gg/d5YjjdP)  
[Game Attack/ScrewAttack G1](https://discord.gg/F8fncjr)  
[RTX 2017](https://discord.gg/0oqF8OqUW3gQDZD2)  
[Community Bite](https://discord.gg/zQstVc9)  
[/r/RWBY](https://discord.gg/rwby)  
[Red vs. Blue](https://discord.gg/TkeEJ9D)

Huge shoutout to Nick Molloy for making the API interface. It's hard to believe that a company as large as Rooster Teeth doesn't have a documented API or public feeds available for their content, and his python script does the job perfectly.

---
####Setup:
+ First you'll need to make sure you have [rt_api](https://github.com/NickMolloy/rt_api) by [Nick Molloy](https://github.com/NickMolloy) installed. In Terminal run:  
`pip install rt_api`
+ Next, open up **vidfeed.settings**
  * Replace `<Website>` on **line 2** with the name of the site you want to pull videos from. Available options:
     * `RoosterTeeth`
     * `AchievementHunter`
     * `FunHaus`
     * `ScrewAttack`
     * `GameAttack`
     * `TheKnow`
     * `CowChop`
     * Blank - This will feed you videos from **ALL** the above sites
   * Replace `<Username>` and `<Password>` **on lines 4 and 6** with the username/password of an account on [RoosterTeeth.com](http://roosterteeth.com/) that has a FIRST Subscription (This is necessary to retrieve links to FIRST-exclusive content. **If you filter out FIRST content, you don't need to provide these.**)
   * Replace `<Main Feed Channel Webhook URL>` **on line 8** with the Webhook URL that Discord gives you *in the channel you want all non-FIRST videos to be linked in*
   * Replace `<FIRST Feed Channel Webhook URL>` **on line 10** with the Webhook URL that Discord gives you *in the channel you want all FIRST-exclusive videos to be linked in*
   * Replace `<Webhook Avatar URL>` **on line 12** with the URL of the image you want to be the avatar of the bot when it posts in your Discord channels
   * If you want to filter out __non-FIRST__ content, change **line 15** to be `aI00`
   * If you want to filter out __FIRST Exclusive__ content, change **line 16** to be `aI00`
   * After all this, your vidfeed.settings should look something like this:  
     ```(lp0
     S'RoosterTeeth'
     p1
     aS'firstSubscriber'
     p2
     aS'ispasswordastrongpassword'
     p3
     aS'https://discordapp.com/api/webhooks/lots of random numbers and letters'
     p4
     aS'https://discordapp.com/api/webhooks/lots of random numbers and letters'
     p5
     aS'http://placekitten.com.s3.amazonaws.com/homepage-samples/200/286.jpg'
     p6
     aI0
     aI01
     aI01
     a.```

+ After that, you just have to set up a cron job (or other persistent timer) to keep running the script
