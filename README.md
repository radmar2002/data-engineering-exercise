# data-engineering-exercise

data-engineering-exercise

### T1:

Given an input as json array (each element is a flat dictionary) write a program that will parse this json, and return a nested dictionary of dictionaries of arrays, with keys specified in command line arguments and the leaf values as arrays of flat dictionaries matching appropriate groups
`python nest.py nesting_level_1 nesting_level_2 ... nesting_level_n`

Example:
`cat input.json | python nest.py currency country city`

### T2:

REST service from the first task

- localhost API point: `http://localhost:8000/api/v01/nest/`
- user/pass: `marius / *** `

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
