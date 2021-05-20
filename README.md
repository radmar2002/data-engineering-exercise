# data-engineering-exercise

### Structure:

- script
- api
- sqlfiles

### Task 1 Python:

Run in command line:
`python nest.py nesting_level_1 nesting_level_2 ... nesting_level_n`

Example:
`cat input.json | python nest.py currency country city`

### Task 2 Python:

REST service from the first task deployed here on
Digital Ocean with `drf, supervisor, gunicorm nginx`

Example: POST `http://165.22.22.185/api/v01/nest/`

- REST call with Postman/Insomia or any other client
- Nesting levels should be passed in header: `nestlevels: country city currency`
- Basic Auth: user/pass: `marius / *** `
- Body can have the similar input.json

```javascript
fetch("http://localhost:8000/api/v01/nest/", {
  method: "POST",
  headers: {
    "content-type": "application/json",
    nestlevels: "country city currency",
    authorization: "Basic bWFyaXVzOmdyaWdvcmVzY3U=",
  },
  body: [
    {
      country: "US",
      city: "Boston",
      currency: "USD",
      amount: 100,
    },
    {
      country: "FR",
      city: "Paris",
      currency: "EUR",
      amount: 20,
    },
    {
      country: "FR",
      city: "Lyon",
      currency: "EUR",
      amount: 11.4,
    },
    {
      country: "ES",
      city: "Madrid",
      currency: "EUR",
      amount: 8.9,
    },
    {
      country: "UK",
      city: "London",
      currency: "GBP",
      amount: 12.2,
    },
    {
      country: "UK",
      city: "London",
      currency: "FBP",
      amount: 10.9,
    },
  ],
})
  .then((response) => {
    console.log(response);
  })
  .catch((err) => {
    console.error(err);
  });
```

![test_call](./test_call.png)

- localhost API point: `http://localhost:8000/api/v01/nest/`

### Task 3 SQL:

- SQL scripts are included in folder: `data-engineering-exercise/sqlfiles/`
