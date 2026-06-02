# MediFind Database Design

## Users

Stores information about people using the application.

| Column        | Type         | Description            |
| ------------- | ------------ | ---------------------- |
| user_id       | Integer (PK) | Unique user identifier |
| name          | String       | User's full name       |
| email         | String       | User email             |
| password_hash | String       | Encrypted password     |
| created_at    | Timestamp    | Account creation time  |

---

## Pharmacies

Stores pharmacy information.

| Column          | Type         | Description                |
| --------------- | ------------ | -------------------------- |
| pharmacy_id     | Integer (PK) | Unique pharmacy identifier |
| name            | String       | Pharmacy name              |
| address         | String       | Full address               |
| latitude        | Float        | Location latitude          |
| longitude       | Float        | Location longitude         |
| contact_number  | String       | Pharmacy contact           |
| operating_hours | String       | Opening hours              |
| is_verified     | Boolean      | Verification status        |

---

## Medicines

Stores medicine information.

| Column       | Type         | Description                |
| ------------ | ------------ | -------------------------- |
| medicine_id  | Integer (PK) | Unique medicine identifier |
| name         | String       | Medicine name              |
| generic_name | String       | Generic medicine name      |
| manufacturer | String       | Manufacturer               |
| dosage       | String       | Example: 625mg             |
| form         | String       | Tablet, Syrup, Injection   |

---

## Inventory

Links pharmacies and medicines.

| Column         | Type         | Description        |
| -------------- | ------------ | ------------------ |
| inventory_id   | Integer (PK) | Inventory record   |
| pharmacy_id    | Integer (FK) | Pharmacy reference |
| medicine_id    | Integer (FK) | Medicine reference |
| stock_quantity | Integer      | Quantity available |
| price          | Decimal      | Selling price      |
| last_updated   | Timestamp    | Last stock update  |

---

## Relationship Diagram

Users
|
| Searches
|
Medicines
|
| Available In
|
Inventory
|
| Belongs To
|
Pharmacies
