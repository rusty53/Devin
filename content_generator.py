class ContentGenerator:
    def __init__(self):
        pass
    
    def generate_content(self, topic_name, videos):
        content = {
            'summary': self._generate_summary(topic_name, videos),
            'briefing_document': self._generate_briefing_document(topic_name, videos),
            'study_guide': self._generate_study_guide(topic_name, videos),
            'faq': self._generate_faq(topic_name, videos),
            'timeline_characters': self._generate_timeline_characters(topic_name, videos)
        }
        return content
    
    def _generate_summary(self, topic_name, videos):
        summary = f"# Summary: {topic_name}\n\n"
        summary += f"This collection of {len(videos)} YouTube episodes explores \"{topic_name}\" through curated educational content from leading channels.\n\n"
        
        summary += "## Key Topics Covered\n"
        summary += f"- Fundamental concepts in {topic_name.lower()}\n"
        summary += "- Practical applications and examples\n"
        summary += "- Advanced theoretical frameworks\n"
        summary += "- Historical context and development\n\n"
        
        summary += "## Video Collection\n\n"
        
        for i, video in enumerate(videos, 1):
            summary += f"{i}. **{video['title']}** by {video['channel']}\n"
            summary += f"   - Views: {video['views']} | Duration: {video['duration']} | Uploaded: {video['upload_date']}\n"
            summary += f"   - Relevance Score: {video['relevance_score']}/100\n"
            summary += f"   - URL: {video['url']}\n\n"
        
        return summary
    
    def _generate_briefing_document(self, topic_name, videos):
        briefing = f"# Briefing Document: {topic_name}\n\n"
        briefing += f"{topic_name} encompasses fundamental principles and concepts that are essential for understanding this field. "
        briefing += f"This briefing covers the most important concepts based on analysis of {len(videos)} educational videos from leading educators and institutions.\n\n"
        
        briefing += "## Core Concepts\n\n"
        briefing += f"**Definition**: {topic_name} involves the study and application of key principles that govern this domain.\n\n"
        briefing += "**Key Components**:\n"
        briefing += "- Fundamental theories and principles\n"
        briefing += "- Mathematical foundations and frameworks\n"
        briefing += "- Practical applications and implementations\n"
        briefing += "- Historical development and context\n\n"
        
        briefing += "## Educational Sources\n\n"
        briefing += "Our curated collection includes content from:\n"
        
        channels = list(set([video['channel'] for video in videos]))
        for channel in channels[:5]:
            briefing += f"- **{channel}**: High-quality educational content with clear explanations\n"
        
        briefing += "\n## Applications\n\n"
        briefing += f"Understanding {topic_name} is crucial for:\n"
        briefing += "- Academic study and research\n"
        briefing += "- Professional development and career advancement\n"
        briefing += "- Practical problem-solving and implementation\n"
        briefing += "- Innovation and creative applications\n\n"
        
        briefing += "## Learning Path\n\n"
        briefing += "1. Begin with foundational concepts and definitions\n"
        briefing += "2. Develop understanding through examples and demonstrations\n"
        briefing += "3. Progress to advanced theoretical frameworks\n"
        briefing += "4. Apply knowledge to practical problems and scenarios\n"
        briefing += "5. Explore cutting-edge developments and research\n\n"
        
        return briefing
    
    def _generate_study_guide(self, topic_name, videos):
        guide = f"# Study Guide: {topic_name}\n\n"
        guide += f"This study guide provides a structured approach to learning {topic_name} using the curated video collection.\n\n"
        
        guide += "## Learning Objectives\n\n"
        guide += f"By the end of this study program, you should be able to:\n"
        guide += f"- Understand the fundamental principles of {topic_name}\n"
        guide += "- Apply key concepts to solve problems\n"
        guide += "- Explain the historical development and context\n"
        guide += "- Identify practical applications and use cases\n\n"
        
        guide += "## Study Schedule\n\n"
        guide += "### Week 1: Foundations\n"
        for video in videos[:3]:
            guide += f"- Watch: {video['title']} ({video['duration']})\n"
        
        guide += "\n### Week 2: Core Concepts\n"
        for video in videos[3:6]:
            guide += f"- Watch: {video['title']} ({video['duration']})\n"
        
        guide += "\n### Week 3: Advanced Topics\n"
        for video in videos[6:9]:
            guide += f"- Watch: {video['title']} ({video['duration']})\n"
        
        if len(videos) > 9:
            guide += "\n### Week 4: Specialized Applications\n"
            for video in videos[9:]:
                guide += f"- Watch: {video['title']} ({video['duration']})\n"
        
        guide += "\n## Key Terms and Concepts\n\n"
        guide += f"Important terminology related to {topic_name}:\n"
        guide += "- [Term 1]: Definition and explanation\n"
        guide += "- [Term 2]: Definition and explanation\n"
        guide += "- [Term 3]: Definition and explanation\n\n"
        
        guide += "## Practice Problems\n\n"
        guide += "1. Explain the fundamental principles covered in the video collection\n"
        guide += "2. Compare and contrast different approaches presented by various educators\n"
        guide += "3. Apply the concepts to real-world scenarios\n"
        guide += "4. Analyze the historical development of key ideas\n\n"
        
        return guide
    
    def _generate_faq(self, topic_name, videos):
        faq = f"# Frequently Asked Questions: {topic_name}\n\n"
        
        faq += f"## What is {topic_name}?\n\n"
        faq += f"{topic_name} is a fundamental area of study that encompasses key principles and concepts essential for understanding this field. "
        faq += "The curated video collection provides comprehensive coverage from basic concepts to advanced applications.\n\n"
        
        faq += f"## Why is {topic_name} important?\n\n"
        faq += f"Understanding {topic_name} is crucial for academic success, professional development, and practical problem-solving. "
        faq += "It provides the foundation for more advanced study and real-world applications.\n\n"
        
        faq += "## How should I approach learning this topic?\n\n"
        faq += "Start with the foundational videos to build a solid understanding, then progress to more advanced content. "
        faq += "Take notes, pause to reflect on key concepts, and try to apply what you learn to practical examples.\n\n"
        
        faq += "## Which videos should I watch first?\n\n"
        faq += "Begin with the highest-rated videos from well-known educational channels:\n"
        
        top_videos = sorted(videos, key=lambda x: x['relevance_score'], reverse=True)[:3]
        for i, video in enumerate(top_videos, 1):
            faq += f"{i}. {video['title']} by {video['channel']} (Score: {video['relevance_score']}/100)\n"
        
        faq += "\n## How long will it take to complete all videos?\n\n"
        total_duration = "Approximately 2-4 hours"
        faq += f"The total viewing time is {total_duration}, but allow additional time for note-taking, reflection, and practice problems.\n\n"
        
        faq += "## Are there prerequisites for this topic?\n\n"
        faq += "Basic mathematical and scientific literacy is helpful, but the video collection includes content for various skill levels, "
        faq += "from beginner-friendly explanations to advanced theoretical discussions.\n\n"
        
        return faq
    
    def _generate_timeline_characters(self, topic_name, videos):
        timeline = f"# Timeline and Key Figures: {topic_name}\n\n"
        
        timeline += "## Historical Timeline\n\n"
        timeline += f"The development of {topic_name} spans centuries of scientific and intellectual progress:\n\n"
        
        timeline += "### Ancient Period\n"
        timeline += "- Early philosophical and mathematical foundations\n"
        timeline += "- Initial observations and theoretical frameworks\n\n"
        
        timeline += "### Classical Period\n"
        timeline += "- Formalization of key principles\n"
        timeline += "- Mathematical development and proofs\n\n"
        
        timeline += "### Modern Era\n"
        timeline += "- Advanced theoretical frameworks\n"
        timeline += "- Practical applications and technology\n\n"
        
        timeline += "### Contemporary Developments\n"
        timeline += "- Current research and innovations\n"
        timeline += "- Future directions and possibilities\n\n"
        
        timeline += "## Key Figures\n\n"
        timeline += f"Important contributors to the field of {topic_name}:\n\n"
        
        timeline += "### Historical Pioneers\n"
        timeline += "- **[Pioneer 1]**: Foundational contributions and discoveries\n"
        timeline += "- **[Pioneer 2]**: Theoretical developments and frameworks\n"
        timeline += "- **[Pioneer 3]**: Mathematical formulations and proofs\n\n"
        
        timeline += "### Modern Contributors\n"
        timeline += "- **[Contributor 1]**: Advanced theoretical work\n"
        timeline += "- **[Contributor 2]**: Practical applications and implementations\n"
        timeline += "- **[Contributor 3]**: Contemporary research and innovations\n\n"
        
        timeline += "## Educational Contributors\n\n"
        timeline += "The video collection features content from leading educators:\n"
        
        channels = list(set([video['channel'] for video in videos]))
        for channel in channels[:5]:
            timeline += f"- **{channel}**: Educational content and explanations\n"
        
        return timeline
    
    def save_content(self, content, base_filename):
        for content_type, text in content.items():
            filename = f"{base_filename}_{content_type}.md"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(text)
