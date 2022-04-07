# My experiences

I have participated *deeply* and "properly" in several Open Source projects
and in this section I will describe each of those project. How I got into the
projects, some of the specifics of the projects, my position in the project
and perhaps something I learned from that particular one.

This is not meant to be an exhaustive or complete list.

## Dancer

Soon after I started a new software developer job in the autumn of 1993, I
discovered IRC, Internet Relay Chat. I immediately joined channels (that is
what "chat rooms" are called in IRC speak), socialized online and made friends
online with people from around the world.

On IRC, I soon discovered that not all clients were actual users. Some of them
were automated programmed robot clients, called bots. All channels I
frequented had at least one. One day an IRC friend of mine from Denmark,
Bjorn, showed me his embryo of what would become his own Open Source bot. I
immediately joined the mission of writing a bot. For the fun, for the
education and to be able to make our bot do everything we would like a bot do
in the channels we frequented. We called it Dancer from the fact that it
served in a Danish channel at first. Dane Serv become Dancer.

I refreshed a programming language I had written already before that I called
FPL (Frexx Programming Language) and made the bot programmable in this
language. This piece of code might be the oldest code I have ever released as
Open Source, tracing back to maybe even before 1990.

We worked on and developed Dancer intensively for several years. In the late
1996, it struck me I should of course extend it so that it could exchange
currency rates for us on command. How much is 100 SEK (Swedish crowns) in USD
today? That was easy, but in order for the currency rates to be exact, I
needed to download fresh rates from somewhere daily. I found an HTTP server
that hosted rates, so I just needed a tool that could run on a schedule and
download those updated numbers...

## Rockbox

In the beginning of the twenty-first century, before the smart phones, a new
consumer electronics device started to show up in some households. The
portable mp3 players. Digital music in your pockets for real. To many, the
Apple ipod was the first device that showed the potential but already before
that model, other manufacturers and brands had already released some devices.

One of the first mp3 players on the market was the "Archos Player" with its
massive 6 GB harddrive. My brother Björn and our common friend Linus purchased
these devices, only to soon realize that while the device was nice, the
software were lacking several features you would think such a device should be
able to provide. How hard would it be to write our own replacement?

With a lot of reverse engineering and hard work, we managed to figure out how
to replace the software in the device with one we wrote ourselves. We then
took on other similar devices and within a few years
[Rockbox](https://www.rockbox.org) was a fully Open Source mp3 player firmware
replacement that worked on several dozen music players from a handful of
different brands. Rockbox was a tiny simple operating system made to just have
a music player application run. Albeit an application that could run games,
including doom (of course), have better battry live and support many more
music and audio formats than any of the original firmwares did.

We had physical annual developer meetups during several years where Rockbox
contributors from all over the world would unite to hack on code and have a
good time over a weekend.

When the smart phones eventually entered and switfly conquered the portable
music world, the concept and use of mp3 players faded away and so did my
personal interest in the Rockbox project. I officially stopped participating
in 2014, but by then I was not doing much. I continued to host and run servers
and infrastructure for the project until late 2021.

## c-ares

## libssh2

## Firefox

## curl
