# deutsche-bahn-cli

Get useful information regarding public transport in Germany (DeutscheBahn) such as train stations, departures and arrivals, routes, parking spots and more straight from the CLI.
<br>
This program is powered by the official [Deutsche Bahn APIs](https://developer.deutschebahn.com/store/apis/list):

- [StaDa API](https://developer.deutschebahn.com/store/apis/info?name=StaDa-Station_Data&version=v2&provider=DBOpenData)
- [TimeTable API](https://developer.deutschebahn.com/store/apis/info?name=Timetables&version=v1&provider=DBOpenData)

<br>

### Installation & Prerequisites
You must have `Python v3` installed on your device.

#### Installation steps

1. Clone the repository
```bash
$ git clone https://github.com/Manu10744/deutsche-bahn-cli.git
```
 
2. Create a `.env` file in the root directory and enter your API Key:
```bash
DB_API_KEY=<your_key>
```   

3. Install the necessary dependencies with `pip`
```bash
$ pip install -r requirements.txt
```

<br>

### Usage Examples
#### Search for a train station
```bash
# Search with a fracture of a name
py main.py --search Münc

# Search with a full name
py main.py --search "München Hbf"

# Search with a wildcard
py main.py --search "München*,Berlin*"
```

<br>
<hr>

### TO-DO's:
- [X] Get API Key
- [X] Setup fundamental structure and configuration
- [X] Implement search for train stations => maybe --find str ?
- [X] Implement search for departures given a train station => maybe --departures xy ?
- [ ] (WIP) Implement search for parking spots => maybe --parking xy ?
- [ ] Implement route information output => maybe --from xy --to z ?

### Possible enhancements 
- [X] Instead of printing lots of results, print some and ask user if he wants to output more results
- [X] Add --verbose argument
- [ ] (WIP) Bash autocomplete
- [ ] Web Dashboard
