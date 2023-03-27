# curl

I needed a simple tool to download currency rates from an HTTP server (See
[Dancer](dancer.md) above), and I found **httpget**. On November 11, 1996
Rafael Sagula had released the first version of that tool named httpget 0.1
and I found it just days after his release. This was a rudimentary tool that
almost did what I wanted. I fixed a bug or two in it and sent my improvements
back to Rafael over email.

Rafael made a few follow-up releases of the tool before he asked if I wanted
to "take over" maintenance since I had kept on sending improvements his way –
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

It was only a toy project and of course it was Open Source. I admired and
thought Open Source authors were cool and I wanted to be part of that group as
well. I wanted curl to run everywhere and I knew that I would not be able to
make it a universal tool on my own, nor would I alone be able to fix all bugs
and add all potential new features. It had to be Open Source to go places.

In November 1998, I posted an update on the website celebrating "over 300
downloads" of the latest release.

The project remained a command line tool for a while, and after the summer of
2000 we introduced **libcurl** to the world. A library that would bring "curl
powers" to applications that wanted it.

I would continue to work on curl on my spare time for years to come. In 2019,
I joined the company [wolfSSL](https://wolfssl.com) and started offering
commercial curl support and could finally work on curl full-time. Something of
a dream that came true.

In OpenSSF's [criticality score](https://github.com/ossf/criticality_score)
update in early 2021 where they rank how critical Open Source projects are to
the world, they put curl as #86 out of 102,507.
