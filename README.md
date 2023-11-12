# randbayes: show off noise feature problems
Bart Massey

This repo contains:

* Code for generating randomized instances with correlated
  and noise features

* Code for checking the generator output

* Code for a Naïve Bayes classifier for the instances. The
  classifier uses log-likelihood comparisons with
  *m-*estimation and performs *n-*way cross-validation.
  This code is taken unchanged from
  <https://github.com/pdx-cs-ai/psambayes>

* Some sample generated instances

## Running

Easiest is to just run

    python3 nbayes.py unmess.csv 10
    
to show that with two features each with 70% correlation you
get accuracy of about 70%. Then run

    python3 nbayes.py mess.csv 10

to show that with two 70%-correlated features and 500 random
features you get an accuracy of about 50%. The "good"
features are being swamped by the bad ones. Also note that
this second run is much slower, since 502 features must be
processed for each instance.
