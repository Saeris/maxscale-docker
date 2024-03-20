# MaxScale Docker Sharded Database

This is an example of a sharded database using MariaDB and MaxScale. It uses `docker-compose` to setup all of the various services involved and comes with some sample data and a python script to test the database.

## Running

To start the cluster, run the following commands in the project root:

```bash
docker-compose build
docker-compose up -d
```

It will take a moment for the server to start and be fully available. You can check the status of the database cluster by running the following:

```bash
docker-compose exec maxscale maxctrl list servers
```

A successful result will look something like this:

```bash
┌────────┬─────────┬──────┬─────────────┬─────────────────┬───────────┬─────────────────┐
│ Server │ Address │ Port │ Connections │ State           │ GTID      │ Monitor         │
├────────┼─────────┼──────┼─────────────┼─────────────────┼───────────┼─────────────────┤
│ shard1 │ shard1  │ 3306 │ 0           │ Master, Running │ 0-3001-59 │ MariaDB-Monitor │
├────────┼─────────┼──────┼─────────────┼─────────────────┼───────────┼─────────────────┤
│ shard2 │ shard2  │ 3306 │ 0           │ Running         │ 0-3002-4  │ MariaDB-Monitor │
└────────┴─────────┴──────┴─────────────┴─────────────────┴───────────┴─────────────────┘
```

Befoe you can run the Python script, you will need to seed the database with the included zipcode data in the `sql/` directory. To do this, you can use phpMyAdmin, which will be running on [http://localhost:8080](http://localhost:8080). You can use the same login credentials as the MaxScale cluster is configured with: `maxuser` and `maxpwd` to login to phpMyAdmin. From there, navigate to the Import wizard and upload both `sql/zipcodes_one.sql` and `sql/zipcodes_two.sql` one at a time.

You will then need to run some first-time setup for Python. I recommend using [`uv`](https://astral.sh/blog/uv) for this. The following commands should be all you need running in a Linux dev environment:

Setup the virtual environment:
```bash
uv venv
```

Activate the virtual environment (command varies per host OS):
```bash
source .venv/bin/activate
```

Install required packages:
```bash
uv pip install -r requirements.txt
```

Finally, you can run `app.py`:

```bash
python app.py
```

To shut down the cluster, run the following:

```bash
docker-compose down -v
```
