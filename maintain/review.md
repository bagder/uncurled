# Patch reviewing

One of the most important tasks in a project for a maintainer is to review
proposed changes and improvements.

A project should have **all** its changes peer reviewed by someone before they
are merged to reduce the risk of bad things getting merged. A project should
also have other means and checks in order to detect bad code for when the
review fail to detect mistakes: like tests and code scanners.

Reviews not only work to detect flaws, they also serve as a way for the more
experienced developers to provide feedback and help contributors how to
improve their contribution and guide them to make a better next attempt. It is
also how a maintainer can object to a suggested feature completely if it does
not comply with the project's general goal and direction.

My advice is to use as many tools, scripts and robots as possible to verify
and warn about code style and "source formalities", since I have learned that
users in general accept nit-picking by tools much more than they do when those
remarks come from fellow humans. And as a reviewer, remarking on spacing,
indent levels and brace positions is mind-numbing work we rather not do.

In many smaller and undermanned projects, reviews will frequently be performed
by the same maintainer that authored the change. This is not ideal, but will
be done if there are not enough reviewers around in the name of driving
development forward.
