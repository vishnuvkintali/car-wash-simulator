# Car Wash Queue Simulator

A program I built to simulate a car wash and figure out how busy it gets, how long people wait, and how many wash bays a shop really needs. It is inspired by my brother's business, Needham Auto Cleaning.

This is an Industrial Engineering project. Industrial Engineering is about making systems (like a car wash, a factory, or a hospital) run better. A car wash is a great example because it is a line (a "queue") of customers waiting for a service.

## What it does

You type in some settings and the program pretends to run a full day, minute by minute, then tells you what happened. It can also run the day many times in a row and average the results.

You can set:
- How often cars arrive (on average)
- How long a wash takes (on average)
- How many wash bays the shop has
- How long the shift is (in minutes)
- How many days to simulate

It reports:
- Average cars washed per day
- The worst pileup (longest line) it ever saw
- The average time a customer waited in line

## How to run it

You need Python installed. Then in a terminal:

```
python carwash_sim.py
```

Answer the questions it asks. If you type something that is not a number, it will ask you again instead of crashing.

## The big thing I discovered

The most surprising part was how much **randomness** changed everything.

When cars arrived on a perfect schedule (exactly every 4 minutes) with 2 bays, nobody waited at all. The line never got longer than 1 car.

But when I made the cars arrive randomly (still one every 4 minutes on average, just not perfectly spaced), the line suddenly piled up to 7 or 8 cars and people started waiting a few minutes, even though nothing about the averages changed.

That taught me a real Industrial Engineering lesson: **variability is the enemy.** Randomness creates waiting lines all by itself, even when a shop has enough capacity on average. This is why a bank with "enough" tellers still has a line. It is also why a smart shop keeps a little spare capacity instead of running at 100 percent.

## Other findings

- With cars arriving every 4 minutes but each wash taking 6 minutes, **one bay cannot keep up.** The line grows to over 20 cars and the average wait hits 40 minutes.
- Adding a **second bay** fixes it almost completely. Cars washed per day jumps from about 39 to about 59, and the wait nearly disappears.
- There are three ways to fix a bottleneck: wash faster, get fewer cars, or add more capacity (more bays). Adding a bay was the easiest big win here.

## Why running it many times matters

Once I added randomness, running the simulation just once could not be trusted, because one run might get lucky or unlucky. So the program runs the day many times (like 100 times) and averages the results. Engineers call this a Monte Carlo simulation. It gives an answer you can actually rely on.

## What I learned while building this

- Loops (using a loop as a clock that counts minutes)
- Lists (to track many wash bays at once)
- Functions (to package the simulation and reuse it)
- Libraries (using Python's random library)
- Handling bad input so the program does not crash
- Monte Carlo simulation (running many times and averaging)
