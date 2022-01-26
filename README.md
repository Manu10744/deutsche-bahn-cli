# deutsche-bahn-cli

Get useful information regarding public transport in Germany (DeutscheBahn) such as train stations, departures, routes, parking spots and more straight from the CLI.
<br>
This program is powered by the official [Deutsche Bahn APIs](https://data.deutschebahn.com/dataset.groups.apis.html).
<br>

### Installation & Prerequisites
You must have `Python v3` installed on your device.

#### Installation steps
1. Enter your API Key in the `.env` file
```bash
DB_API_KEY=<your_key>
```   
2. Install the necessary dependencies with `pip`
```bash
$ pip install -r requirements.txt
```

<br>

### Usage
```bash
TODO
```

<br>
<hr>

### TO-DO's:
- [ ] Get API Key
- [ ] Setup fundamental structure and configuration
- [ ] Implement search for train stations => maybe --find str ?
- [ ] Implement search for departures given a train station => maybe --departures xy ?
- [ ] Implement search for parking spots => maybe --parking xy ?
- [ ] Implement route information output => maybe --from xy --to z ?

### Possible enhancements 
- [ ] Bash autocomplete
- [ ] Web Dashboard
