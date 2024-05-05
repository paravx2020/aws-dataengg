from faker import Faker
fake = Faker()
message = {
    'name': fake.name(),
    'address': fake.address(),
    'phone': fake.phone()
}
print(message)