import requests
import json
import re
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import time
import random

class YouTubeScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def search_videos(self, topic, keywords, max_results=12, preferred_channels=None):
        videos = []
        
        search_queries = [topic] + keywords
        
        if "law of action" in topic.lower() or "action" in topic.lower():
            search_queries.extend([
                "principle of least action physics",
                "Newton's laws of motion",
                "Lagrangian mechanics",
                "action principle physics",
                "variational principle physics"
            ])
        elif "machine learning" in topic.lower():
            search_queries.extend([
                "neural networks explained",
                "deep learning tutorial",
                "AI algorithms",
                "machine learning fundamentals"
            ])
        elif "quantum" in topic.lower():
            search_queries.extend([
                "quantum mechanics explained",
                "quantum physics basics",
                "quantum theory"
            ])
        
        for query in search_queries[:6]:
            try:
                query_videos = self._search_single_query(query, max_results // 2)
                videos.extend(query_videos)
                time.sleep(random.uniform(1, 3))
            except Exception as e:
                print(f"Error searching for '{query}': {e}")
                continue
        
        videos = self._remove_duplicates(videos)
        videos = self._calculate_relevance_scores(videos, keywords, preferred_channels)
        videos = sorted(videos, key=lambda x: x['relevance_score'], reverse=True)
        
        return videos[:max_results]
    
    def _search_single_query(self, query, max_results):
        search_url = f"https://www.youtube.com/results?search_query={quote_plus(query)}"
        
        try:
            response = self.session.get(search_url)
            response.raise_for_status()
            
            videos = self._parse_search_results(response.text)
            return videos[:max_results]
            
        except Exception as e:
            print(f"Error fetching search results: {e}")
            return []
    
    def _parse_search_results(self, html_content):
        videos = []
        
        script_pattern = r'var ytInitialData = ({.*?});'
        match = re.search(script_pattern, html_content)
        
        if not match:
            return self._fallback_parse(html_content)
        
        try:
            data = json.loads(match.group(1))
            contents = data.get('contents', {}).get('twoColumnSearchResultsRenderer', {}).get('primaryContents', {}).get('sectionListRenderer', {}).get('contents', [])
            
            for section in contents:
                items = section.get('itemSectionRenderer', {}).get('contents', [])
                for item in items:
                    video_data = item.get('videoRenderer', {})
                    if video_data:
                        video = self._extract_video_info(video_data)
                        if video:
                            videos.append(video)
            
        except Exception as e:
            print(f"Error parsing JSON data: {e}")
            return self._fallback_parse(html_content)
        
        return videos
    
    def _fallback_parse(self, html_content):
        videos = []
        soup = BeautifulSoup(html_content, 'html.parser')
        
        video_elements = soup.find_all('div', {'class': 'ytd-video-renderer'})
        
        for element in video_elements[:10]:
            try:
                title_elem = element.find('a', {'id': 'video-title'})
                if not title_elem:
                    continue
                
                title = title_elem.get('title', '').strip()
                url = 'https://www.youtube.com' + title_elem.get('href', '')
                
                channel_elem = element.find('a', {'class': 'yt-simple-endpoint'})
                channel = channel_elem.text.strip() if channel_elem else 'Unknown'
                
                video = {
                    'title': title,
                    'url': url,
                    'channel': channel,
                    'views': 'N/A',
                    'upload_date': 'N/A',
                    'duration': 'N/A',
                    'relevance_score': 50
                }
                
                videos.append(video)
                
            except Exception as e:
                continue
        
        return videos
    
    def _extract_video_info(self, video_data):
        try:
            title = video_data.get('title', {}).get('runs', [{}])[0].get('text', '')
            video_id = video_data.get('videoId', '')
            url = f"https://www.youtube.com/watch?v={video_id}"
            
            channel_name = video_data.get('ownerText', {}).get('runs', [{}])[0].get('text', 'Unknown')
            
            view_count_text = video_data.get('viewCountText', {}).get('simpleText', 'N/A')
            
            published_text = video_data.get('publishedTimeText', {}).get('simpleText', 'N/A')
            
            duration_text = video_data.get('lengthText', {}).get('simpleText', 'N/A')
            
            return {
                'title': title,
                'url': url,
                'channel': channel_name,
                'views': view_count_text,
                'upload_date': published_text,
                'duration': duration_text,
                'relevance_score': 50
            }
            
        except Exception as e:
            return None
    
    def _remove_duplicates(self, videos):
        seen_urls = set()
        unique_videos = []
        
        for video in videos:
            if video['url'] not in seen_urls:
                seen_urls.add(video['url'])
                unique_videos.append(video)
        
        return unique_videos
    
    def _calculate_relevance_scores(self, videos, keywords, preferred_channels=None):
        for video in videos:
            score = 30  # Start lower to allow more differentiation
            
            title_lower = video['title'].lower()
            
            for keyword in keywords:
                if keyword.lower() in title_lower:
                    score += 15
            
            educational_terms = ['explained', 'tutorial', 'lesson', 'course', 'introduction', 'basics', 'fundamentals']
            for term in educational_terms:
                if term in title_lower:
                    score += 8
            
            physics_terms = ['physics', 'mechanics', 'principle', 'law', 'theory', 'quantum', 'newton']
            for term in physics_terms:
                if term in title_lower:
                    score += 10
            
            if preferred_channels and video['channel'] in preferred_channels:
                score += 20
            
            views_text = video.get('views', '').lower()
            if 'million' in views_text or 'm views' in views_text:
                score += 25
            elif 'thousand' in views_text or 'k views' in views_text:
                import re
                numbers = re.findall(r'(\d+(?:\.\d+)?)', views_text)
                if numbers:
                    try:
                        num = float(numbers[0])
                        if num >= 500:  # 500K+ views
                            score += 15
                        elif num >= 100:  # 100K+ views
                            score += 10
                        else:
                            score += 5
                    except:
                        score += 8
            
            duration = video.get('duration', '')
            if duration and ':' in duration:
                try:
                    parts = duration.split(':')
                    if len(parts) == 2:
                        minutes = int(parts[0])
                        if 5 <= minutes <= 25:  # Ideal educational length
                            score += 10
                        elif minutes > 25:
                            score += 5
                except:
                    pass
            
            upload_date = video.get('upload_date', '').lower()
            if 'month' in upload_date:
                score += 8
            elif 'year' in upload_date:
                if '1 year' in upload_date or '2 year' in upload_date:
                    score += 12
                elif '3 year' in upload_date or '4 year' in upload_date:
                    score += 10
                else:
                    score += 5
            
            video['relevance_score'] = min(score, 100)
        
        return videos
