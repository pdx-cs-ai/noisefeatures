# noisefeatures: show off noise feature problems
Bart Massey

This repo contains:

* Code for generating randomized instances with correlated
  and noise features

* Code for checking the generator output

* Code for some ML classifiers, taken from the `psam` Python
  implementations at https://github.com/pdx-cs-ai

* Some sample generated instances

## Demo

The effect can be demonstrated with different learners.

### KNN

Run

    python3 knn.py unmess.csv 10 11
    
to show that with two features each with 70% correlation you
get accuracy of about 70%. Then run

    python3 knn.py mess.csv 10 11

to show that with two 70%-correlated features and 500 random
features you get an accuracy of about 50%. The "good"
features are being swamped by the bad ones.

### ID3

Run

    python3 nbayes.py unmess.csv 10
    python3 nbayes.py mess.csv 10

to see the effect.  Note that the second run is much
slower, since 502 features must be processed for each
instance.

### ID3 (Decision Tree)

Run

    python3 id3.py unmess.csv 10 0 0
    python3 id3.py mess.csv 10 0 0

The slowdown is still present, but even with all the noise
features ID3 is partly figuring it out.

Those last two parameters control tree pruning. With them at
defaults even the clean instances are classified randomly:

    python3 id3.py unmess.csv 10

With the pruning set to be "modest" the noisy instances are
classified accurately.

    python3 id3.py mess.csv 0.1 0

We know this is a real result due to the way we constructed
the data. Decision trees are cool.
