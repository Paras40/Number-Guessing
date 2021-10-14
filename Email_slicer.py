email = input("Write your email here : ").strip()

#index is a in-built function
username = email[:email.index("@")]
domain = email[email.index("@")+1:]

print(f"Your username is {username} and domain is {domain}")
