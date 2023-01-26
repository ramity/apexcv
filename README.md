<h1 align="center">
ApexCV
</h1>

![image](https://i.imgur.com/XZMg8is.jpg)

# Project currently paused.

Excuses include:

> - I'm working on other commerical projects.
> - There's a lack of 1080p source video due to youtube's cat and mouse game for downloaders.
> - There's a lack of video being labeled by version (see Escape from Tarkov in-raid HUD for example).
> - The project needs a rethink and rewrite. I've learned a lot since I started this project doing other work.
> - I'm exploring tesseract-ocr and primitive template matching for other games.

## Want me to work some more on this project?

Create a git issue with label "help wanted", explain your use case for this software, why you're interested in the project, or just say hi.

## Goal:

Create a CV framework that extends beyond apex that allows for configurable conversion of video footage to statistics over time.

## Use cases:

One could use the produced statistics to provide additional context to viewers, sort videos by stats (count or rate), measure progression of stats across videos like measuring improvement, enable quick navigation to key highlights, etc.

# Setup/Contrib

-   remove all previous images/containers
-   clone this repo
-   `cd` into the cloned repo
-   `docker-compose up -d`
-   To exec into the container:
    -   Windows:
        -   `winpty docker exec -it apexcv_python bash`
    -   Linux/Unix/Mac
        -   `docker exec -it apexcv_python bash`
