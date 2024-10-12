import re
import requests
import argparse

class CRTFinder:
    def __init__(self):
        self.seen_subdomains = set()

    @staticmethod
    def is_valid_domain(domain):
        """Check if the provided domain is valid."""
        domain = domain.lstrip('www.')
        pattern = r'^[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.([a-zA-Z]{2,}|xn--[a-zA-Z0-9]+)$'
        return re.match(pattern, domain) is not None

    @staticmethod
    def clean_subdomain(subdomain):
        """Clean subdomains by removing unwanted prefixes and normalizing."""
        return subdomain.replace('*.', '').replace('www.', '').lower()

    def fetch_subdomains(self, domain):
        """Fetch subdomains from crt.sh for a given domain."""
        response = requests.get(f"https://crt.sh/?q=%25.{domain}&output=json")
        if response.status_code != 200:
            print(f"Failed to retrieve data for {domain}")
            return set()

        subdomains = {
            self.clean_subdomain(subdomain)
            for entry in response.json()
            for subdomain in entry['name_value'].splitlines()
        }
        return subdomains

    def process_domains(self, domains):
        """Process the list of domains and collect their subdomains."""
        for domain in domains:
            if self.is_valid_domain(domain):
                subdomains = self.fetch_subdomains(domain)
                self.seen_subdomains.update(subdomains)
            else:
                print(f'Invalid domain: "{domain}".')

    def display_subdomains(self):
        """Display unique subdomains found."""
        if self.seen_subdomains:
            print("Unique Subdomains:")
            for subdomain in sorted(self.seen_subdomains):
                print(subdomain)
        else:
            print("No subdomains found.")

    def run(self):
        """Run the script based on command-line arguments."""
        parser = argparse.ArgumentParser(description="Retrieve subdomains from a domain.")
        parser.add_argument("-d", "--domain", help="Specify a domain to retrieve subdomains")
        parser.add_argument("-f", "--file", help="Specify a file containing a list of domains")
        args = parser.parse_args()

        if args.domain:
            self.process_domains([args.domain])
        elif args.file:
            try:
                with open(args.file, 'r') as file:
                    domains = [line.strip() for line in file.readlines()]
                    self.process_domains(domains)
            except FileNotFoundError:
                print("File not found or not valid.")
                return
        else:
            parser.print_help()

        self.display_subdomains()

if __name__ == "__main__":
    crt_finder = CRTFinder()
    crt_finder.run()
