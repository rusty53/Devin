#!/usr/bin/env python3

import json
import sys
import os
from youtube_scraper import YouTubeScraper
from notebooklm_formatter import NotebookLMFormatter
from content_generator import ContentGenerator

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <topic_name> [max_videos] [min_relevance_score]")
        print("Example: python main.py 'Machine Learning' 15 70")
        return
    
    topic_name = sys.argv[1]
    max_videos = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    min_relevance = int(sys.argv[3]) if len(sys.argv) > 3 else 65
    
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    predefined_topic = None
    for topic in config['predefined_topics']:
        if topic['name'].lower() == topic_name.lower():
            predefined_topic = topic
            break
    
    if predefined_topic:
        keywords = predefined_topic['keywords']
        print(f"Using predefined topic: {predefined_topic['name']}")
    else:
        keywords = [topic_name]
        print(f"Using custom topic: {topic_name}")
    
    print(f"Searching for {max_videos} videos with minimum relevance score of {min_relevance}")
    
    scraper = YouTubeScraper()
    formatter = NotebookLMFormatter()
    generator = ContentGenerator()
    
    preferred_channels = config['search_settings']['preferred_channels']
    
    print("Searching YouTube videos...")
    videos = scraper.search_videos(topic_name, keywords, max_videos, preferred_channels)
    
    videos = [v for v in videos if v['relevance_score'] >= min_relevance]
    print(f"Found {len(videos)} relevant videos")
    
    if not videos:
        print("No videos found matching the criteria. Try lowering the minimum relevance score.")
        return
    
    print("Generating content...")
    content = generator.generate_content(topic_name, videos)
    
    print("Formatting for NotebookLM...")
    notebook = formatter.format_notebook(topic_name, videos, content)
    
    output_dir = f"output_{topic_name.replace(' ', '_').lower()}"
    os.makedirs(output_dir, exist_ok=True)
    
    formatter.save_notebook(notebook, os.path.join(output_dir, 'notebooklm_notebook.json'))
    formatter.save_videos_json(videos, os.path.join(output_dir, 'youtube_videos.json'))
    generator.save_content(content, os.path.join(output_dir, 'content'))
    
    print(f"\nWorkflow completed successfully!")
    print(f"Output files saved to: {output_dir}/")
    print(f"- notebooklm_notebook.json")
    print(f"- youtube_videos.json")
    print(f"- content_summary.md")
    print(f"- content_briefing_document.md")
    print(f"- content_study_guide.md")
    print(f"- content_faq.md")
    print(f"- content_timeline_characters.md")

if __name__ == "__main__":
    main()
