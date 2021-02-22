# Multar

    Multar is a simple theatre seat booking app for a new theatre in town. Multar is supposed to be used by users in the theatre to gauge and manage occupancy. The theatre is a new Arena theatre for live performances and does not assign fixed seating number assignments to its patrons. Project consists of 3 API endpoints as mentioned below:

### Occupy Seat

- [Endpoint URL - /occupy/ ] The Endpoint will be given the person's name and ticket ID as input and outputs the seat number which will be occupied. If the seating is full, the appropriate error message is returned. This endpoint is a POST request and can be run as:

```json
{
	"ticket_id": "ticket_id",
	"person_name": "Name"
}
```

### Vacate Seat

- Vacate seat - [Endpoint URL - /vacate/ ]: This endpoint takes the seat number which the person will be vacating and frees that slot up to be used by other people. Vacate seat at first feels to be a DELETE request but it is acutally a POST request because this endpoint istead of deleting anything is updating the is_available (seat) back to "True".

```json
{
	"seat_id": "seat_num"
}
```

or 

```json
{
	"seat_id": 1
}
```

### Get info

- Get Person/Seat information - [Endpoint URL - /get_info/\<NAME or SEATNUM or TICKETID> ]: This endpoint can take either the seat number or person’s name or ticket ID for the input and returns the person’s name, ticket ID, and slot number.

As mentioned this endpoint can be called with a url parameter after /get_info

1. `/get_info/Name/`
2. `/get_info/seat_num/`
3. `/get_info/ticket_id/`

## Installation

1. Settin up the environment

- Using Python virtual env

```console
	$ cd Multar
```
```console
	$ python3 -m venv venv
```
```console
	$ source venv/bin/activate
```
```console
	$ pip3 insall requirements.txt
```

- Using Pipenv

```console
	$ cd Multar
```
```console
	$ pipenv shell
	$ pipenv install requirements.txt
```

2. Move to ticketapi project

```console
	$ cd ticketapi
```

3. Run Migrations

```console
	$ python3 manage.py migrate
```

4. Populate seats data

Set the value of `MAX_OCCUPANCY` in the `settings.py` and populate the seats in the database. For populating the seats in the database a special management command is implemented in the project which takes the `MAX_OCCUPANCY` variable from `settings.py` and creates those number of seats in the database. By default it is set to 100.

```console
	$ python3 manage.py seed
```

5. Run Server

```console
	$ python3 manage.py runserver
```
