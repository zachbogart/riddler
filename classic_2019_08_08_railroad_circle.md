## Circular Railroad

https://fivethirtyeight.com/features/how-many-cars-are-on-this-circular-train/

From Ben Tupper, ‘round and ‘round the railroad:

You find yourself in a train made up of some unknown number of connected train cars that join to form a circle. It’s the ouroboros of transportation. Don’t think too hard about its practical uses.

From the car you’re in, you can walk to a car on either side — and because the train is a circle, if you walk far enough eventually you’ll wind up back where you started. Each car has a single light that you can turn on and off. Each light in the train is initially set on or off at random.

What is the most efficient method for figuring out how many cars are in the train?

(Assume that you can’t mark or otherwise deface a train car, and that each car’s light is only visible from within that car. The doors automatically close behind you, too. There are only two actions you can take: turning on or off a light and walking between cars.)

## Solution

We need a way to count the cars using only the lights. Let the length be defined by *l* Our method is as follows:

1. Walking in one direction, turn on the lights for *x* steps.
2. Turn around and turn off the lights for *x* steps.

We will end up back where we started.  If *x* ends up being less than *l*, we will always see lights on as we walk back. But, if *x* is greater than the length of the train, when we walk back we will walk into a car that is dark before we have gotten back to where we started. This overshoot means whe already have been in this car and walked the length of the train, meaning how many lights be turned off on the way back is the length of the train.

I'm not sure the best way to determine *x*, though. We could start at 2 I spose and then keep adding one till we hit it. Or we could double our step count every time a search fails. Would like to see what people do about choosing the *x* efficiently.