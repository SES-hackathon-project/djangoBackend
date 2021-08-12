# ENDPOINTS

## create a new hangout: 
- POST request to http://localhost:8000/create_hangout with the json data body in the
format:
```
{
    "budget_type": {int},
    "zipcode": {int},
    "group_size": {int},
    "number_submitted": {int}
}
```

will return back: 
```
{
    "group_id":{random unique 6-digit int passcode}
    "budget_type": {int},
    "zipcode": {int},
    "group_size": {int},
    "number_submitted": {int}
}
```

## request hangout data 
- GET request to http://localhost:8000/hangout/{group_id}
- IMPORTANT: there has to be a preexisting hangout with the group_id specified

## submit budget
- POST request to http://localhost:8000/submit_budget/{group_id} with the json data body 
in the format: 
```
  "group_id": {int}, 
  "budget_amount":{int}
```
- IMPORTANT:there has to be a preexisting hangout with the group_id specified
- this method also increases the hangout object's number_submitted field by 1


