import json
from datetime import datetime

class NotebookLMFormatter:
    def __init__(self):
        pass
    
    def format_notebook(self, topic_name, videos, generated_content=None):
        notebook = {
            "name": topic_name,
            "created_at": datetime.now().isoformat(),
            "sources": [],
            "documents": {
                "summary": generated_content.get('summary') if generated_content else None,
                "briefing_document": generated_content.get('briefing_document') if generated_content else None,
                "study_guide": generated_content.get('study_guide') if generated_content else None,
                "faq": generated_content.get('faq') if generated_content else None,
                "timeline_characters": generated_content.get('timeline_characters') if generated_content else None
            }
        }
        
        for video in videos:
            source = {
                "type": "youtube_video",
                "title": video['title'],
                "url": video['url'],
                "channel": video['channel'],
                "metadata": {
                    "views": video['views'],
                    "upload_date": video['upload_date'],
                    "duration": video['duration'],
                    "relevance_score": video['relevance_score']
                }
            }
            notebook['sources'].append(source)
        
        return notebook
    
    def save_notebook(self, notebook, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=2, ensure_ascii=False)
    
    def save_videos_json(self, videos, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(videos, f, indent=2, ensure_ascii=False)
