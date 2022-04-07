# Security

Security is important, and because security is important to people and users,
you need to pay attention as well and make it a priority in your project.

A project should be judged based on how it acts on security problem much more
than the mere fact that the problems appeared the first place. Even the best
run projects will have occasional hiccups, but projects that do not take care
of and handle their security vulnerabilities in a proper and responsible way
will loose users' trust. And without trust, what are your project?

## Security problems will appear

Security is hard and flaws easily creep in. Be humble and prepared to act when
(not if) such problems are reported. Also, be prepared that changes you
thought nobody cared about or used will get some serious attention and get
flamed badly once a security flaw is pointed out and gets handled by the
public. This is not saying that you cannot have processes and develop code to
be more secure than others. You can and you should.

## Review, test, scan, verify

Use manual review, add as many tests as you can, run tools on the source code
and use tools that verify things at runtime (including fuzzing). Do all the
things that can be done to make sure your project has no obvious flaws.

## Bug Bounty

If possibly, consider offering a bug bounty for your project. They usually
work so that security researchers who find and report security vulnerabilities
in your project are rewarded. Preferably with real money.

By offering money to researchers, you will "buy their eyeball time" for a
little while. Many of of those will otherwise simply move on and rather spend
their limited time and energy on other projects that *do* offer rewards.

## the Bug Bounty Paradox

By offering monetary rewards for *finding* security problems, you migth find
yourself in a situation where you pay for the finding but all the developers
who are left to fix the problems are unpaid volunteers. You must be aware of
and acknowledge this imbalance, as it may alienate contributors. Maybe you can
find a way to combat it?

Still, in my experience from having worked with well over a hundred security
flaws detected in my own Open Source projects, finding the problem is usually
the tough part. Once the problem has been identified and brought into the
light of day, actually fixing it is nine out of ten times a rather straight
forward action.
