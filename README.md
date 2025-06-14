# YouTube to NotebookLM Workflow

Transform YouTube educational content into structured NotebookLM materials with an intuitive web dashboard.

## Features

- **Web Dashboard**: Interactive interface for topic selection and workflow management
- **Predefined Topics**: Curated topics including Physics, Machine Learning, Calculus, and more
- **Custom Topics**: Support for user-defined topics with custom keywords
- **YouTube Integration**: Automated video search and metadata extraction
- **Content Generation**: Automatic creation of study materials including:
  - Summary documents
  - Briefing documents
  - Study guides
  - FAQ documents
  - Timeline and key figures
- **NotebookLM Format**: Output optimized for Google's NotebookLM platform

## Quick Start

### Web Interface

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the web application:
```bash
python app.py
```

3. Open your browser to `http://localhost:5000`

4. Select a predefined topic or create a custom one

5. Configure settings and generate materials

6. Download the generated NotebookLM files

### Command Line Interface

```bash
python main.py "Machine Learning" 15 70
```

Parameters:
- Topic name (required)
- Maximum videos (optional, default: 12)
- Minimum relevance score (optional, default: 65)

## Configuration

Edit `config.json` to customize:
- Predefined topics and keywords
- Search settings
- Preferred YouTube channels
- Output parameters

## Output Files

The workflow generates:
- `notebooklm_notebook.json` - Main NotebookLM format file
- `youtube_videos.json` - Curated video list with metadata
- `content_summary.md` - Topic summary and video overview
- `content_briefing_document.md` - Comprehensive briefing document
- `content_study_guide.md` - Structured learning guide
- `content_faq.md` - Frequently asked questions
- `content_timeline_characters.md` - Historical timeline and key figures

## Example Topics

- **The Law of Action**: Physics principles including Newton's laws and least action
- **Quantum Mechanics**: Core quantum physics concepts
- **Machine Learning**: AI algorithms and neural networks
- **Calculus**: Mathematical foundations and applications
- **Data Structures**: Computer science algorithms and structures

## Architecture

- `app.py` - Flask web application and API endpoints
- `youtube_scraper.py` - YouTube search and metadata extraction
- `notebooklm_formatter.py` - NotebookLM JSON formatting
- `content_generator.py` - Study material generation
- `main.py` - Command-line interface
- `config.json` - Configuration settings
- `templates/index.html` - Web dashboard interface

## Requirements

- Python 3.7+
- Flask 2.3+
- Requests
- BeautifulSoup4
- yt-dlp

## License

This project is part of the Devin AI experiments repository.
