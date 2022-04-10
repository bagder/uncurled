# Release management

Releases work best when you can do as much of it as possible in an automated
way. Then you can also do things like automatic nightly archives and you can
verify in CI jobs etc that the scripts work.

I have personally done several hundred releases of my Open Source projects
over the years, and my single best advice is: use a checklist. It took me a
while to learn this hard lesson myself and I do not how many releases I have
screwed up in my life simply because I forgot some little detail along the
way. I have learned that if I have every tiny little detail in the release
process documented, I can not only make sure that I can follow it and do an
identical release the next time, I can also at some point in a much easier way
hand over that duty to someone else, with great confidence that it will work.

Remember to update the checklist when you change the release procedure.

I am a firm believer in release early, release often and I think it has paid
off many times over the years. More releases is better than fewer. Remember:
[Only releases get tested](../code/releases.md).
