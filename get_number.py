import re
import requests
import socket
from bs4 import BeautifulSoup


def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return "Unable to resolve the domain."

def get_webpage_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content

    except Exception as e:
        print(f"An error occurred while fetching webpage content: {str(e)}")
        return None

def find_phone_number(html_content):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        phone_element = soup.find(class_='phone-number')

        if phone_element:
            phone_number = phone_element.get_text(strip=True)
            phone_pattern = r'\b\d{1} \(\d{3}\) \d{3}-\d{2}-\d{2}\b'
            match = re.search(phone_pattern, phone_number)

            if match:
                return match.group()
            else:
                return "Phone number not found or invalid format."
            
        else:
            return "Phone number element not found on the webpage."
        
    except Exception as e:
        print(f"An error occurred while parsing HTML content: {str(e)}")
        return None


url = "https://sstmk.ru"
domain = "sstmk.ru"

ip_address = get_ip_address(domain)
print(f"IP адрес сайта {domain}: {ip_address}")

html_content = get_webpage_content(url)
phone_number = find_phone_number(html_content)
print(f"Телефон на главной странице {url}: {phone_number}")
