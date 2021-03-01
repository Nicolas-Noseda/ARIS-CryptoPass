class WebsitePasswordModel:

    website = ""
    password = ""
    username = ""

    def __init__(self, website_password):
        website_password_split = website_password.split("!?&")
        self.website = website_password_split[0].split("=!=")[1]
        self.username = website_password_split[1].split("=!=")[1]
        self.password = website_password_split[2].split("=!=")[1]