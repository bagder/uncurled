# Project

(noun) *"An individual or collaborative enterprise that is carefully planned
to achieve a particular aim."*

## It is never finished

This is hardly any surprise to anyone, but projects in general tend to never
really get finished and I imagine that Open Source projects in particular
never do as long as there is a certain amount of users. There are always bug
fixes to be made and people will always want to add more tweaks or features
and then we get more bugs and repeat.

Projects typically finish when there are no more users (willing to work on it).

For individual authors and maintainers, the work on a project can of course
end when they decide to just stop participating in that project.

## Over time, you will spend most time on maintenance and support

I do most of my work in the curl project answering email, trying to reproduce
and understand people's bug reports, clarifying documentation or blogging
about a related subject. Only a small fraction of my curl time is actual
development time.

## Documentation is never good enough

If there is too little documentation or badly phrased, people will not find the
answer there.

If there is too much written on a subject people will not find the answer since
there is too much written and they are only looking for the answer to their
tiny, tiny question.

If there is a FAQ, the exact question the user is looking for is not answered
there.

Heck, even if the documentation is perfect (in your mind), lots of people will
just mail and ask anyway since they believe that is a faster way to get the
accurate answer. Or they do not believe the documentation. Or they for some
reason decide that the perfect online documentation must be out-of-date...

## If not alive, it is dead

An Open Source project that does not update its web site or other resources
within a given time period will appear dead. A project that appears dead are
not updated for reason: because people in the project do not care enough. If
people do not care enough to keep things up-to-date, the project is dead. Yes
sure there are exceptions, but not many... We all look at other projects like
this, we better realize that others look at our projects the same way!

## The world is full of projects

Do not expect contributors and team members to flock around your awesome
idea. In fact, if you just deliver decently good stuff, chances are you may
remain relatively alone in the project... Work to aid people to get into the
project and ease every step, but do not expect them to come.

## Old versions never really die

Suddenly a user will appear out of the blue and report problems or have a
question and it gets revealed that said user has a version of your software
installed that you thought were long forgotten and extinct.

Open source versions once released find their ways to some places that just
then obviously never again upgrade. But surely, if it works why fix it?

The downside for these users is of course that they then have not gotten any
of the security upgrades you have been shipping the last decade.

Often, very slow-moving (or stuck) Linux distributions are blamed for
this. "I am forced to use Linux Y with version Z so I have to use your software
version X".

## Doing a solid and good API is hard

API lessons:

Do not do open ended things like "non-zero to enable", use explicit numbers
instead: "1 to enable, 0 to disable" to leave room for future extensions and
additions.

Using vararg style setopt() functions in C is not the optimal way to receive
values if you use non-ints and want to work nicely on >32bit platforms.

Do not ever return data that needs free(). You must provide a free function to
use since various systems may use different memory models between the app and
the library.

## Keep. On. Improving.

Q: "How does one stay consistent for so long? I bet you had a lot of great
opportunities and new shiny technology you wanted to play around.

Do you have any personal guidelines that help you staying that long on a
project?"

## Clean up your backyard

## Supervise and help out your "neighbors"

## Open standards are your friends

## The project is we, not "I" nor "you"

## Contributor License Agreements (CLAs)
