email=input("What is your email address ?")
username=email[:email.index("@")].strip()
domain_name=email[(email.index("@")+1):].strip()
print("Your username is: {} and domain name is {}".format(username,domain_name))
print("Your username is: "+username+" and domain name is "+domain_name)

