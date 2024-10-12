# CRTFinder

**CRTFinder** is a simple tool to retrieve a list of subdomains for a given domain using data from [crt.sh](https://crt.sh/), a website that provides public SSL certificate information. The tool automatically removes duplicate subdomains and ensures that only valid subdomains are displayed.

## Features

- Fetch subdomains from a specified domain.
- Supports single domain input or a list of domains from a file.
- Automatically removes duplicate subdomains.
- Cleans subdomains by removing `www.` prefixes and wildcard `*`.
- Filters out invalid domain inputs.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/mnovel/CRTFinder.git
   cd CRTFinder
   ```

2. **Install dependencies**:

   CRTFinder uses the `requests` module, make sure it is installed. If not, run the following command:

   ```bash
   pip install requests
   ```

3. **Run the script**:

   CRTFinder can be executed from the command line. Use Python 3.x to run it.

   ```bash
   python CRTFinder.py -d example.com
   ```

## Usage

There are two ways to use **CRTFinder**:

1. **Fetch subdomains for a single domain**:

   Use the `-d` or `--domain` option to specify the domain you want to retrieve subdomains for.

   ```bash
   python CRTFinder.py -d example.com
   ```

2. **Fetch subdomains from a file with multiple domains**:

   You can provide a file containing a list of domains using the `-f` or `--file` option.

   Each line in the file should contain one domain:

   ```text
   example.com
   example.org
   test.com
   ```

   Then, run:

   ```bash
   python CRTFinder.py -f domainlist.txt
   ```

## Output

Once executed, the tool will display the unique subdomains found. Here's an example of the output:

```bash
Unique Subdomains:
api.example.com
mail.example.com
www.example.com
```

## Options

- `-d` or `--domain`: Specify a domain to retrieve subdomains for.
- `-f` or `--file`: Specify a file containing a list of domains to retrieve subdomains from.
- `-h` or `--help`: Display a help message and list available options.

## Example Usage

### Example 1: Fetch subdomains for a single domain

```bash
python CRTFinder.py -d example.com
```

### Example 2: Fetch subdomains from a file with multiple domains

```bash
python CRTFinder.py -f domainlist.txt
```

## License

This project is licensed under the [MIT License](LICENSE).
