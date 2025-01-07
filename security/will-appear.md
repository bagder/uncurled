# Security problems will appear

Security is hard and flaws easily creep in. Be humble and prepared to act when
(not if) such problems are reported. Also, be prepared that changes you
thought nobody cared about or used will get some serious attention and get
flamed badly once a security flaw is pointed out and gets handled by the
public. This is not saying that you cannot have processes and develop code to
be more secure than others. You can and you should.

We judge projects based on how they handle their security problems, not by
their existence.

We *never* compare projects by counting published past security
vulnerabilities. It does not work. A project having reported more issues might
have had more scrutiny or just set the bar lower than the project with fewer.

## "Your project is insecure"

Even when you do everything by the book and follow every best practice to the
point on how to handle security problems; you fix the problems, you register
CVEs and you disclose them responsibly with all details documented, you can be
sure that parts of your audience will react badly.

They will think that because you published a security vulnerability, your
project has a bigger problem of insecurity. As if not all actively developed
projects get these problems, either open or proprietary.

## Learn

Every security incident is a chance to learn. Mistakes are for learning. Why
did this error slip through and cause this problem? What code pattern can we
detect or prohibit to prevent this or similar mistakes to happen again?

This is hard. In my experience, most security problems feel like one-offs and
rare circumstances that happened because of strange changes and your own
stupidity. Seeing patterns and adjusting ways of working to prevent future
flaws is difficult work but should always be attempted, to make the most out
of every CVE.
