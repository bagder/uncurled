# c-ares

At some point during 2003, my friend Bjørn (from Dancer) and I were discussing
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
and instead I created **c-ares**. It would show its roots but not be the
same. The `c` could be for curl, but it also made it into an English word like
"cares" which was enough for me.

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

