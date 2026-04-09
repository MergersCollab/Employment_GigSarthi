import json
import requests
from bs4 import BeautifulSoup
import re

def scrape_jobs():
    url = "https://www.freelancer.com/jobs/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        jobs = []
        job_cards = soup.find_all('div', class_='JobSearchCard-item')
        
        for idx, card in enumerate(job_cards):
            title_tag = card.find('a', class_='JobSearchCard-primary-heading-link')
            title = title_tag.text.strip() if title_tag else "Unknown"
            
            desc_tag = card.find('p', class_='JobSearchCard-primary-description')
            desc = desc_tag.text.strip() if desc_tag else "No description"
            
            price_tag = card.find('div', class_='JobSearchCard-secondary-price')
            price_text = price_tag.text.strip() if price_tag else "N/A"
            # Clean price string
            price = re.sub(r'\s+', ' ', price_text).replace('Avg Bid', '').strip()
            
            # Simple skills extraction
            skills = []
            skill_tags = card.find_all('a', class_='JobSearchCard-primary-tagsLink')
            for skill in skill_tags:
                skills.append(skill.text.strip())
            
            jobs.append({
                "id": f"job-{idx+1}",
                "title": title,
                "description": desc,
                "price": price,
                "skills": skills
            })
            
        return {
            "status": "success",
            "message": f"Successfully scraped {len(jobs)} gig listings.",
            "data": jobs
        }
        
    except Exception as e:
        # Fallback dummy data in case of error
        dummy_jobs = [
            {"id": "job-1", "title": "React Developer Needed", "description": "Need a React dev for fullstack app.", "price": "$15 - $25 / hr", "skills": ["React.js", "Javascript"]},
            {"id": "job-2", "title": "Python Data Scraper", "description": "Scrape e-commerce sites.", "price": "$100", "skills": ["Python", "Web Scraping", "BeautifulSoup"]},
            {"id": "job-3", "title": "Logo Design", "description": "Create a modern logo for a tech startup.", "price": "$50", "skills": ["Graphic Design", "Logo Design"]},
            {"id": "job-4", "title": "SEO Expert", "description": "Improve ranking for my website", "price": "$20 / hr", "skills": ["SEO", "Marketing", "Link Building"]}
        ]
        return {
            "status": "fallback",
            "message": "Scraping failed, using fallback structured data. Error: " + str(e),
            "data": dummy_jobs
        }

if __name__ == "__main__":
    result = scrape_jobs()
    print(json.dumps(result))
