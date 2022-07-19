# PARSER | CSV TO SQLITE DB


## Files:
* [`Task`](files/tasks.txt) - Task sheet
* [`server.csv`](files/server.csv) - Server data file
* [`client.csv`](files/client.csv) - Players data file
* [`cheaters.db`](files/cheaters.db) - Data about cheaters is stored here
* [`main.db`](files/main.db) - Main database. Data is written here

## Setup:
> ```shell
> # SSH
> git clone git@github.com:xristxgod/CSV-PARSER.git
> # HTTPS
> git clone https://github.com/xristxgod/CSV-PARSER.git
> ```

## Settings in .env file:
> `MAIN_DB_PATH` - The path to the main database. By default: `../files/main.db`
>
> `CHEATERS_DB_PATH` - The path to the database with cheaters. By default: `../files/cheaters.db`
> 
> `CLIENT_FILE` - The path to the file with information about players. By default: `../files/client.csv`
> 
> `SERVER_FILE` - The path to the file with information about server. By default: `../files/server.csv`

## How to run:
> ```shell
> # Install lib 
> pip install -r requirements.txt
> # Run
> python ./main.py
> ```

-------
<details><summary>Request to create a table in the database: main.db</summary>

```sql
CREATE TABLE IF NOT EXISTS general_model (
	id int PRIMARY KEY,
  	timestamp int,
  	player_id INT,
  	event_id int,
  	error_id char,
  	json_server JSON,
  	json_client JSON,
);
```

</details>

<details><summary>Request for data about cheaters in the bath:</summary>

```sql
SELECT player_id 
FROM cheaters
WHERE ban_time > 'year-month-day hours:minutes:seconds'
Example: WHERE ban_time > '2021-12-12 00:00:00'
```

</details>

------

### Screenshot of the work:
![image](https://user-images.githubusercontent.com/84931791/179762350-7bd10c2c-949f-42af-a1a9-b495b165615b.png)

