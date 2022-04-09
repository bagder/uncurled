# Dancer

Soon after I started a new software developer job in the autumn of 1993, I
discovered IRC, Internet Relay Chat. I immediately joined channels (that is
what "chat rooms" are called in IRC speak), socialized online and made friends
online with people from around the world.

On IRC, I soon discovered that not all clients were actual users. Some of them
were automated programmed robot clients, called bots. All channels I
frequented had at least one. One day an IRC friend of mine from Denmark,
Bjørn, showed me his embryo of what would become his own Open Source bot. I
immediately joined the mission of writing a bot. For the fun, for the
education and to be able to make our bot do everything we would like a bot do
in the channels we frequented. We called it Dancer from the fact that it
served in a Danish channel at first. Dane Serv become Dancer.

This was the first real Open Source project I contributed code to regularly.
It was also my first real TCP/IP client adventure and I learned to read RFCs
to figure out protocol details.

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
