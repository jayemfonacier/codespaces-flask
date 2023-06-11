import requests, random, string

def generate_random_email():
    # Generate a random username
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    
    # Generate a random domain
    domain = random.choice(["gmail.com", "yahoo.com", "hotmail.com"])

    # Combine the username and domain to create the email address
    email = f"{username}@{domain}"

    return username, email

# Generate a random email address
random_email = generate_random_email()

url = 'http://127.0.0.1:5000/items'
# JSON data for the new item
new_item = {
    "username": generate_random_email()[0],
    "email": generate_random_email()[1],
    "phone_number": random.randrange(10**9, 10**10),
    "age": random.randrange(10, 100),
    "sex": random.choice(["Male", "Female"])
}

# Send POST request to create the new item
response = requests.post(url, json=new_item)

# Print the response
print(response.status_code)  # Status code (e.g., 201 for success)
print(response.json())
