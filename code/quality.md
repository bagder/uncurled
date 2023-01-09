# Code quality

The quality of your project is of course going to be important to users of your
product or service.

A project is however *expected* to start as a baby and have its problems at
first, and nobody will expect that it is perfect to start with. Over time, you
improve and you iterate on design and code. You add tests, you run more tools
and you build automated systems to do it for you.

There is no point in putting in all that energy and try to make everything
perfect from day one.

As the project grows older, it is expected to mature and to evolve into a
solid code base, but as Open Source is forever, there is no fixed timeline for
this. You get to spend as much time on this as you see fit. You might just not
become super popular and conquer the world properly until the code quality is
decent.

## How do you achieve good code quality?

There is no magic silver bullet for this, nor is it really an Open Source
problem. It is an old software engineering challenge and my steps to
accomplish this are:

1. consistent code style (verified by tools)
2. human code reviews before merge
3. tests, tests, tests.
4. CI system that run all tests before merge
5. fuzzing and continuous tests of merged code
6. be responsive on bug reports, add new tests with bugfixes
7. be responsive and friction-less when accepting bugfixes
8. run a bug bounty
9. release often
10. keep at it

## Code coverage

In some circles, measuring and achieving some specific code coverage level is
considered important and I will not disparage that. I think it is awesome if
you manage to write your code and test cases so that you get great code
coverage. It will not mean terribly much and you can still have
many bugs even so, since code coverage cannot measure code path combinations.

In my projects, the code complexity and the portability and conditional
sections of the code etc have always made it extremely hard to generate and
measure code coverage to any meaningful level, so I have rarely done so. I
believe we have still managed to produce fairly good code just based on the
basic principle outlined above.

