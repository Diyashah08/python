def main():
    emails = ["alice@gmail.com", "bob@yahoo.com", "carol@gmail.com"]
    allowed=list(filter(get_valid_email,emails))
    allowed_without_domains=list(map(without_domain,allowed))
    print(allowed_without_domains)

def get_valid_email(email):
    if email.endswith("@gmail.com"):
        return email
def without_domain(email):
        return email.split("@")[0]
    
if __name__ == "__main__":
    main()

    