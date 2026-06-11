def build_client_profile():
    print('=== CLIENT INFORMATION FORM ===')
    name = input('Enter full name: ')
    phone = input('Enter phone number: ')
    email = input('Enter email address: ')
    nationality = input('Enter nationality: ')
    client_data = {
        'name': name,
        'phone': phone,
        'email': email,
        'nationality': nationality
    }
    return client_data
