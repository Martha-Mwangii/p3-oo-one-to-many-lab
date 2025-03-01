class Pet:
    # Class variable storing valid pet types
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    # All instances of Pet will be stored here
    all = []
    
    def __init__(self, name, pet_type, owner=None):
        # Validate the pet_type is one of the allowed types
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        
        # Initialize the instance
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        
        # Add the pet to the all list
        Pet.all.append(self)
        
        # If there's an owner, add the pet to the owner's pets list
        if owner:
            owner.add_pet(self)
    
class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []
    
    def pets(self):
        # Returns the list of pets owned by the owner
        return self.pets_list
    
    def add_pet(self, pet):
        # Ensure pet is an instance of the Pet class
        if not isinstance(pet, Pet):
            raise Exception(f"Expected a Pet, got {type(pet)}")
        
        # Add the pet to the owner's pets list and set the owner of the pet
        self.pets_list.append(pet)
        pet.owner = self
    
    def get_sorted_pets(self):
        # Returns the owner's pets sorted by name
        return sorted(self.pets_list, key=lambda pet: pet.name)

