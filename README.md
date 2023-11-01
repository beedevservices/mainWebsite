# mainWebsite

## Core App
### Models
- Services
    - title
    - id
    - package
    - price
    - time-frame
    - info lines

## Customer App
### Models
- Customer
    - firstName
    - lastName
    - email
    - password
    - companyName
- CustomerProfile
    - address01
    - address02
    - city
    - state
    - zip
    - phone
    - business type
- Reviews
    - customer_id
    - order_id

## Order App
### Models
- OrderRequest
    - service_id
    - customer_id
    - requestDate
    - description
    - bestContact
- Contract
    - orderRequest_id
    - customer_id
    - paymentTerms
    - startDate
    - endDate
    - accepted
- Order
    - contract_id
    - customer_id
    - status
- Invoice
    - contract_id
    - customer_id
    - date
    - paymentRequest


## Admin App
### Models
- Employee
    - firstName
    - lastName
    - email
    - password
    - employeeid
- EmployeeProfile
    - address01
    - address02
    - city
    - state
    - zip
    - phone
    - workEmail
    - hireDate
    - pay_id
- EmployeeSkills
    - language
    - framework
- Pay
    - employee_id
    - rate
    - nextEval
- Jobs
    - employee_id
    - order_id
    - startDate
    - endDate