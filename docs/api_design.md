# MediFind API Design

## Search Medicine

GET /api/search?medicine=paracetamol

Response:

{
"medicine": "Paracetamol",
"results": [
{
"pharmacy": "ABC Medicals",
"distance": "1.2 km",
"stock": 50
}
]
}



## Get Pharmacy Details

GET /api/pharmacy/{id}



## Add Medicine

POST /api/medicine



## Update Inventory

POST /api/inventory



## Pharmacy Login

POST /api/pharmacy/login
