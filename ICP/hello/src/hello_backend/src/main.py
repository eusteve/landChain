from kybra import query

@query
def greet(name: str) -> str:
    return f"Hello, {name}!"

#land registration 
def register_land(location, area):
    tx_hash = LandRegistry.functions.registerLand(location, area).transact({
        'from': w3.eth.accounts[0], 
        'gas': 2000000  # Example: Set gas limit
    })
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)  # transactions to be handled here
    return tx_receipt


# Define a function to get land details
def get_land_details(land_id):
    land_details = LandRegistry.functions.getLandDetails(land_id).call()
    return land_details


# Define class for land parcels
class LandParcel:
    def __init__(self, parcel_id: str, owner_id: str, area: int, location: str, price: int, description: str):
        self.id = parcel_id
        self.ownerId = owner_id
        self.area = area
        self.location = location
        self.price = price
        self.description = description

# Define class for owners
class Owner:
    def __init__(self, owner_id: str, name: str, email: str):
        self.id = owner_id
        self.name = name
        self.email = email

# Function to register a new land parcel
def register_land_parcel(parcel: LandParcel) -> LandParcel:
    # Perform validation and registration logic here
    print(f"Land parcel registered: {parcel.location}")
    return parcel

# Function to transfer ownership of a land parcel
def transfer_ownership(parcel_id: str, new_owner_id: str) -> None:
    # Perform ownership transfer logic here
    print(f"Ownership of parcel {parcel_id} transferred to {new_owner_id}")


# Create a new land parcel
new_parcel = LandParcel(
    parcel_id='1',
    owner_id='owner1',
    area=1000,
    location='123 Main St',
    price=100000,
    description='Beautiful land parcel with scenic views'
)

# Registers the parcel of land 
registered_parcel = register_land_parcel(new_parcel)

#registers a new owner
new_owner_id = 'newOwner1'
transfer_ownership(registered_parcel.id, new_owner_id)
