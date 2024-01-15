import os
import requests


PROXYCURL_API_KEY = os.environ.get("PROXYCURL_API_KEY")

DUMMY_JSON = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"

def scrape_linkedin_profile(url: str):
    # NOTA the docstring will be used by Langchain Agents
    """scrape information from LinkedIn Profiles,
    Manuall scrape the information from the LinkedIn profile.
    """
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    headers = {"Authorization": f"Authorization: Bearer ${PROXYCURL_API_KEY}"}

    # response = requests.get(url=api_endpoint, params={"url": url}, headers=headers)

    response = requests.get(url=DUMMY_JSON)

    data = response.json()

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", None) and k not in ("people_also_viewed", "certifications")
    }

    if data.get("groups"): 
        for group in data.get("groups"):
            group.pop("profile_pic_url")
    
    return data  
    

