# Responsible disclosure

Responsible disclosure is the process where you as a maintainer receives a
report about a security problem and work on a fix **privately** until you have
a fix and then disclose the problem to the world coordinated with the fix.

A responsible disclose can also often involve pre-notifying distributors or
vendors that ship your product so that they can be prepared and offer fixed
versions to users on the very day you make the security problem known to
everyone.

I am a strong proponent of the responsible disclosure approach because of how
it tries to keep innocent users of the product safe. As soon as the security
flaw becomes known, we can be sure that malicious actors will try to take
advantage of it for nefarious purposes.

This said, the keeping things private for the sake of the users' safety must
not be abused or taken lightly. It should only ever be used for actual
security problems and not for any other kind of bugs. It is also important
that the problem still gets fixed and gets published within a reasonable time
even when handled in private. Because a security problem can of course still
be exploited and hurt users even before you have announced it to the world.

Critics of this model tend to favor shipping the bugfix sooner rather than
later in order to help minimize the time window for which bad guys can abuse
the issue. That allows users to patch their systems sooner, but might also
leave users who cannot patch their own systems (for whatever reason)
vulnerable for a now public flaw for a longer period of time.
