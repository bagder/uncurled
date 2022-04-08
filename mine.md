# My experiences

I have participated *deeply* and *properly* in several Open Source projects
and in this section I will describe some of those projects. How I got into the
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

This was the first real Open Source project I conntributed code to regularly.
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

## curl

I needed a simple tool to download currency rates from an HTTP server (See
[Dancer](#dancer) above), and I found **httpget**. On November 11, 1996 Rafael
Sagula had released the first version of that tool named httpget 0.1 and I
found it just days after his release. This was a rudimentary tool that almost
did what I wanted. I fixed a bug or two in it and sent my improvements back to
Rafael over email.

Rafael made a few follow-up releases of the tool before he asked if I wanted
to "take over" maintenance since I had kept on sending improvements his way -
and I did.

In August the following year, while still using httpget to get currencies for
my bot service I found a site that provided more currencies. Since these new
rates were hosted on a GOPHER site I had to add support for another protocol
to the tool, which at the same time made the name wrong. It was no longer just
HTTP it would get. I renamed it to **urlget** a few months later, and by then
it also supported FTP downloads. By then it was portable enough so that it
built and ran on multiple Unix systems as well as Windows, Amiga and more.

When we moved into 1998, the tool had been improved further and could now do
both FTP uploads and HTTP POST and the tool name had again started to feel
wrong and unsuitable. It really did not just "get" URLs anymore. I released
the final urlget version (3.12) on March 14 1998, then renamed the tool to
**curl** and did the first curl release almost a week later with a bumped
version number. On Friday March 20, 1998 I shipped curl 4.0.

In November 1998, I posted an update on the website celebrating "over 300
downloads" of the latest release.

The project remained a command line tool for a while, and after the summar of
2000 we introduced **libcurl** to the world. A library that would bring "curl
powers" to applications that wanted it.

I would continue to work on curl on my spare time for years to come. In 2019,
I joined the company [wolfSSL](https://wolfssl.com) and started offering
commercial curl support and could finally work on curl full-time. Something of
a dream that came true.

In OpenSSF's [criticality score](https://github.com/ossf/criticality_score)
update in early 2021 where they rank how critical Open Source projects are to
the world, they put curl as #86 out of 102,507.

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

The challenge truly piqued our curiosity. With a lot of reverse engineering
and hard work, we figured out how to replace the software in the devices with
one we wrote ourselves. We then took on other similar devices and within a few
years [Rockbox](https://www.rockbox.org) was a fully Open Source mp3 player
firmware replacement that worked on several dozens of different portable music
players from a handful of different brands. Rockbox was a tiny, simple
operating system made to just have a music player application run. Albeit an
application that could run games, including doom (of course), have better
battery live than the factory firmware and support many more music and audio
formats than the original software did.

We had physical annual developer meetups during several years where Rockbox
contributors from all over the world would unite to hack on code and have a
good time over a weekend.

When the smart phones eventually entered and switfly conquered the portable
music world, the concept and use of mp3 players faded away and so did my
personal interest in the Rockbox project. I officially stopped participating
in 2014, but by then I was not doing much. I continued to host and run servers
and infrastructure for the project until late 2021.

## c-ares

At some point during 2003, my friend Bjorn (from Dancer) and I were discussing
back and forth and planning to maybe create our own asynchronous DNS/name
resolver library. We felt that the synchronous APIs provided by
`gethostname()` and `getaddrinfo()` were too limiting in for example curl. We
could really use something that would not block the caller.

While thinking about this and researching what was already out there, I found
the **ares** library written by Greg Hudson. It was an effort that was almost
exactly what we had been looking for. I decided I would not make a new library
but rather join the ares project and help polish that further to perfect it
for curl.

It was soon made clear to me that the original author of this library did not
want the patches I deemed were necessary, including changes to make it more
portable to Windows and more. I felt I had no choice but to fork the project
and instead I created **c-ares**. It would show its heritance but not be the
same. The `c` could be for curl, but it also also made it into an English word
like "cares" which was enough for me.

With c-ares, we could soon offer asynchronous name resolving for curl on a
wide range of platforms, but of course there were other projects and users out
in the world who felt a similar need. c-ares is deployed widely by many.

I have tried to reduce my own personal activities in the c-ares project the
last few years simply because I feel I do not have enough time and energy to
keep it up in this project as well. I still am a maintainer but I am not doing
a lot.

In OpenSSF's [criticality score](https://github.com/ossf/criticality_score)
update in early 2021 where they rank how critical Open Source projects are to
the world, they put c-ares as #2153 out of 102,507.

## libssh2

In late 2006, I wanted to add SCP and SFTP support to curl. I investigated the
library situation for SSH support and I found that there existed two similar
Open Source libraries for this purpose, confusingly similarly named too:
libssh2 and libssh.

As I wanted the SSH library to work a with a non-blocking API to suit curl
proper, I reached out to both the SSH library projects I had found and asked
them about their current support and how they viewed the future and offered to
work on providing such API/functionality myself. I thought the by far most
promising and friendly response came from **libssh2**, so I made my choice.

In November 2006 we started to add support for SCP and SFTP to curl based on
libssh2, and at the same time I started contributing improvements in the
libssh2 project. In particular to make sure the API could be set to and behave
in non-blocking way.

libssh2 was founded by Sara Golemon in December 2004 and she was still the
lead developer when I joined the project but I soon become a co-maintainer and
when Sara changed jobs in 2007 she was blocked to contribute to the project
anymore and I became almost the sole maintainer.

I am still a maintainer of the libssh2 project but I try to keep my activities
to a minimum. Others do the real work there now.

In OpenSSF's [criticality score](https://github.com/ossf/criticality_score)
update in early 2021 where they rank how critical Open Source projects are to
the world, they put libssh2 as #3222 out of 102,507.

## Firefox

In November 2013 I flew over to the US and visited the Mozilla offices in
Mountain view, California for a day full of job interviews. I think I did
seven of them, back to back, over the course of that day.

In most of the interviews, we soon touched the fact that I was the main author
of curl, I knew my way around HTTP and client networking and got into talking
about specific problems or challenges of the day. They knew I knew HTTP,
networking and Open Source as I had already shown that in the public for
years. They mostly needed to also check if I would work socially in a team in
the real world. I got the job.

Working on the Firefox web browser as a full-time job was quite a difference
compared to the small scale projects I had otherwise mostly kept myself busy
in. In this project there were hundreds of developers, it could end up in
thousands of commits per day and there were more than a thousand new bug
tracker entries filed every single day. The speed and the volume of things
were overwhelming.

I worked in the networking team ("Necko") so I got to fiddle with HTTP, DNS,
sockets, cookies etc. Things I knew and liked to fiddle with since before. It
was a perfect job for me. Maybe the biggest downside was C++.

I quit Mozilla in December 2018 without knowing what to do next, but with a
keen interest in trying to see if I could maybe make working on curl full-time
a thing...
