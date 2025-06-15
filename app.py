from flask import Flask, render_template, request, jsonify, send_file
import json
import os
import uuid
from datetime import datetime
from youtube_scraper import YouTubeScraper
from notebooklm_formatter import NotebookLMFormatter
from content_generator import ContentGenerator

app = Flask(__name__)

scraper = YouTubeScraper()
formatter = NotebookLMFormatter()
generator = ContentGenerator()

OUTPUT_DIR = 'output'
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/topics')
def get_topics():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return jsonify(config['predefined_topics'])

@app.route('/api/generate', methods=['POST'])
def generate_workflow():
    try:
        data = request.json
        topic = data['topic']
        max_videos = data.get('max_videos', 12)
        min_relevance = data.get('min_relevance', 65)
        
        with open('config.json', 'r') as f:
            config = json.load(f)
        
        preferred_channels = config['search_settings']['preferred_channels']
        
        print(f"Searching for videos on topic: {topic['name']}")
        videos = scraper.search_videos(
            topic['name'], 
            topic['keywords'], 
            max_videos, 
            preferred_channels
        )
        
        videos = [v for v in videos if v['relevance_score'] >= min_relevance]
        
        print(f"Found {len(videos)} relevant videos")
        
        print("Generating content...")
        content = generator.generate_content(topic['name'], videos)
        
        print("Formatting for NotebookLM...")
        notebook = formatter.format_notebook(topic['name'], videos, content)
        
        session_id = str(uuid.uuid4())
        session_dir = os.path.join(OUTPUT_DIR, session_id)
        os.makedirs(session_dir, exist_ok=True)
        
        formatter.save_notebook(notebook, os.path.join(session_dir, 'notebooklm_notebook.json'))
        formatter.save_videos_json(videos, os.path.join(session_dir, 'youtube_videos.json'))
        generator.save_content(content, os.path.join(session_dir, 'content'))
        
        return jsonify({
            'success': True,
            'session_id': session_id,
            'videos': videos,
            'topic_name': topic['name']
        })
        
    except Exception as e:
        print(f"Error in generate_workflow: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/download/notebook/<session_id>')
def download_notebook(session_id):
    file_path = os.path.join(OUTPUT_DIR, session_id, 'notebooklm_notebook.json')
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True, download_name='notebooklm_notebook.json')
    return "File not found", 404

@app.route('/download/videos/<session_id>')
def download_videos(session_id):
    file_path = os.path.join(OUTPUT_DIR, session_id, 'youtube_videos.json')
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True, download_name='youtube_videos.json')
    return "File not found", 404

@app.route('/download/summary/<session_id>')
def download_summary(session_id):
    file_path = os.path.join(OUTPUT_DIR, session_id, 'content_summary.md')
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True, download_name='summary.md')
    return "File not found", 404

@app.route('/download/briefing/<session_id>')
def download_briefing(session_id):
    file_path = os.path.join(OUTPUT_DIR, session_id, 'content_briefing_document.md')
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True, download_name='briefing_document.md')
    return "File not found", 404

@app.route('/download/study_guide/<session_id>')
def download_study_guide(session_id):
    file_path = os.path.join(OUTPUT_DIR, session_id, 'content_study_guide.md')
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True, download_name='study_guide.md')
    return "File not found", 404

@app.route('/download/faq/<session_id>')
def download_faq(session_id):
    file_path = os.path.join(OUTPUT_DIR, session_id, 'content_faq.md')
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True, download_name='faq.md')
    return "File not found", 404

@app.route('/download/timeline/<session_id>')
def download_timeline(session_id):
    file_path = os.path.join(OUTPUT_DIR, session_id, 'content_timeline_characters.md')
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True, download_name='timeline_characters.md')
    return "File not found", 404

if __name__ == '__main__':
    import os
    port = int(os.environ.get('FLASK_RUN_PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)
