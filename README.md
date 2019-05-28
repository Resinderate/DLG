
# DLG

[![Build Status](https://travis-ci.org/Resinderate/DLG.svg?branch=master)](https://travis-ci.org/Resinderate/DLG)

App to which acts as a HTTP Web API with an endpoint to total a given list of numbers.

## Assumptions
- Should `POST` to `/total/`
- Should use `application/json` for body, as opposed to something like query params.
- The contents should just be a list, like `[1, 2, 3]`, as opposed to something like `{"the_list": [1, 2, 3]}`
- The contents are all numeric. Eg, `1`, `1.2` will work. `"1"`, `"one"`, etc will error with a `400`

## Setup
Inside a virtual environment.
```bash
pip install -r requirements.txt
```
To run:
```bash
FLASK_APP="src/dlg.py" flask run
```
## Tests
To run tests:
```bash
pytest
```
CI is set up on travis to run tests against every push. See latest builds: [https://travis-ci.org/Resinderate/DLG](https://travis-ci.org/Resinderate/DLG)

## Demo
Live demo hosted at: http://dlg.mur-phy.com/total/

Try it out with curl:
 ```
curl -X POST \
  http://dlg.mur-phy.com/total/ \
  -H 'Content-Type: application/json' \
  -d '[1, 2, 3]'
 ```

Running on Raspberry Pi at home, using nginx as a reverse proxy, and supervisord to run/keep up the flask process.

## To Do
- When providing invalid input, like `[1, 2, "three"]`, give more info about the problem element.
- Add deploy script, and deploy steps to Travis CI, to deploy code on changes to master.
- Make `scripts/run.sh` a bit more generic to be useful outside of own host environment.
