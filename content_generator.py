from physics_knowledge import PhysicsKnowledge

class ContentGenerator:
    def __init__(self):
        self.knowledge = PhysicsKnowledge()
    
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
        
        topic_data = self.knowledge.get_topic_data(topic_name)
        key_concepts = topic_data.get('key_concepts', [])
        math_foundations = topic_data.get('mathematical_foundations', [])
        
        summary += "## Key Topics Covered\n"
        if key_concepts:
            for concept in key_concepts[:4]:
                summary += f"- {concept}\n"
        else:
            summary += f"- Fundamental concepts in {topic_name.lower()}\n"
            summary += "- Practical applications and examples\n"
            summary += "- Advanced theoretical frameworks\n"
            summary += "- Historical context and development\n"
        summary += "\n"
        
        if math_foundations:
            summary += "## Mathematical Foundations\n"
            for foundation in math_foundations[:3]:
                summary += f"- {foundation}\n"
            summary += "\n"
        
        summary += "## Video Collection Analysis\n\n"
        summary += f"The selected videos represent a comprehensive learning path from basic concepts to advanced applications. They include:\n"
        summary += "- Conceptual explanations suitable for beginners\n"
        summary += "- Mathematical derivations for advanced students\n"
        summary += "- Historical context and development\n"
        summary += "- Modern applications and connections\n\n"
        
        summary += "## Featured Videos\n\n"
        
        for i, video in enumerate(videos, 1):
            summary += f"{i}. **{video['title']}** by {video['channel']}\n"
            summary += f"   - Views: {video['views']} | Duration: {video['duration']} | Uploaded: {video['upload_date']}\n"
            summary += f"   - Relevance Score: {video['relevance_score']}/100\n"
            summary += f"   - URL: {video['url']}\n\n"
        
        return summary
    
    def _generate_briefing_document(self, topic_name, videos):
        briefing = f"# Briefing Document: {topic_name}\n\n"
        
        topic_data = self.knowledge.get_topic_data(topic_name)
        key_concepts = topic_data.get('key_concepts', [])
        math_foundations = topic_data.get('mathematical_foundations', [])
        applications = topic_data.get('applications', [])
        learning_progression = topic_data.get('learning_progression', [])
        
        briefing += f"{topic_name} encompasses fundamental principles and concepts that are essential for understanding this field. "
        briefing += f"This briefing covers the most important concepts based on analysis of {len(videos)} educational videos from leading educators and institutions.\n\n"
        
        briefing += "## Core Concepts\n\n"
        if key_concepts:
            briefing += f"**Definition**: {key_concepts[0] if key_concepts else f'{topic_name} involves fundamental principles governing this domain.'}\n\n"
            briefing += "**Key Principles**:\n"
            for concept in key_concepts[1:5]:
                briefing += f"- {concept}\n"
        else:
            briefing += f"**Definition**: {topic_name} involves the study and application of key principles that govern this domain.\n\n"
            briefing += "**Key Components**:\n"
            briefing += "- Fundamental theories and principles\n"
            briefing += "- Mathematical foundations and frameworks\n"
            briefing += "- Practical applications and implementations\n"
            briefing += "- Historical development and context\n"
        briefing += "\n"
        
        if math_foundations:
            briefing += "## Mathematical Foundation\n\n"
            for foundation in math_foundations:
                briefing += f"- {foundation}\n"
            briefing += "\n"
        
        briefing += "## Applications\n\n"
        if applications:
            briefing += f"Understanding {topic_name} is essential for:\n"
            for application in applications:
                briefing += f"- {application}\n"
        else:
            briefing += f"Understanding {topic_name} is crucial for:\n"
            briefing += "- Academic study and research\n"
            briefing += "- Professional development and career advancement\n"
            briefing += "- Practical problem-solving and implementation\n"
            briefing += "- Innovation and creative applications\n"
        briefing += "\n"
        
        briefing += "## Educational Sources\n\n"
        briefing += "Our curated collection includes content from:\n"
        
        channels = list(set([video['channel'] for video in videos]))
        channel_descriptions = {
            'PBS Space Time': 'Advanced theoretical concepts with excellent visualizations',
            'TED-Ed': 'Clear, accessible explanations with engaging animations',
            'CrashCourse': 'Systematic coverage of fundamental principles',
            'Physics with Elliot': 'Mathematical rigor with clear explanations',
            'Khan Academy': 'Step-by-step problem-solving approaches',
            'Terra Physica': 'Deep theoretical insights and advanced concepts'
        }
        
        for channel in channels[:5]:
            description = channel_descriptions.get(channel, 'High-quality educational content with clear explanations')
            briefing += f"- **{channel}**: {description}\n"
        
        briefing += "\n## Learning Path\n\n"
        if learning_progression:
            for i, step in enumerate(learning_progression, 1):
                briefing += f"{i}. {step}\n"
        else:
            briefing += "1. Begin with foundational concepts and definitions\n"
            briefing += "2. Develop understanding through examples and demonstrations\n"
            briefing += "3. Progress to advanced theoretical frameworks\n"
            briefing += "4. Apply knowledge to practical problems and scenarios\n"
            briefing += "5. Explore cutting-edge developments and research\n"
        briefing += "\n"
        
        return briefing
    
    def _generate_study_guide(self, topic_name, videos):
        guide = f"# Study Guide: {topic_name}\n\n"
        guide += f"This study guide provides a structured approach to learning {topic_name} using the curated video collection.\n\n"
        
        topic_data = self.knowledge.get_topic_data(topic_name)
        key_concepts = topic_data.get('key_concepts', [])
        math_foundations = topic_data.get('mathematical_foundations', [])
        learning_progression = topic_data.get('learning_progression', [])
        
        guide += "## Learning Objectives\n\n"
        guide += f"By the end of this study program, you should be able to:\n"
        if key_concepts:
            for concept in key_concepts[:4]:
                guide += f"- Understand {concept.lower()}\n"
        else:
            guide += f"- Understand the fundamental principles of {topic_name}\n"
            guide += "- Apply key concepts to solve problems\n"
            guide += "- Explain the historical development and context\n"
            guide += "- Identify practical applications and use cases\n"
        guide += "\n"
        
        guide += "## Study Schedule\n\n"
        
        sorted_videos = sorted(videos, key=lambda x: x['relevance_score'], reverse=True)
        
        guide += "### Week 1: Foundations\n"
        for video in sorted_videos[:3]:
            guide += f"- Watch: {video['title']} ({video['duration']})\n"
        
        guide += "\n### Week 2: Core Concepts\n"
        for video in sorted_videos[3:6]:
            guide += f"- Watch: {video['title']} ({video['duration']})\n"
        
        if len(sorted_videos) > 6:
            guide += "\n### Week 3: Advanced Topics\n"
            for video in sorted_videos[6:9]:
                guide += f"- Watch: {video['title']} ({video['duration']})\n"
        
        if len(sorted_videos) > 9:
            guide += "\n### Week 4: Specialized Applications\n"
            for video in sorted_videos[9:]:
                guide += f"- Watch: {video['title']} ({video['duration']})\n"
        
        guide += "\n## Key Terms and Concepts\n\n"
        guide += f"Important terminology related to {topic_name}:\n"
        
        if "law of action" in topic_name.lower() or "action" in topic_name.lower():
            guide += "- **Action (S)**: The integral of the Lagrangian over time, S = ∫ L dt\n"
            guide += "- **Lagrangian (L)**: The difference between kinetic and potential energy, L = T - V\n"
            guide += "- **Principle of Least Action**: Physical systems follow paths that make the action stationary\n"
            guide += "- **Euler-Lagrange Equation**: The fundamental equation of motion derived from the action principle\n"
            guide += "- **Variational Principle**: Mathematical method for finding extrema of functionals\n"
        elif math_foundations:
            for i, foundation in enumerate(math_foundations[:5], 1):
                term = foundation.split(':')[0] if ':' in foundation else f"Concept {i}"
                definition = foundation.split(':')[1] if ':' in foundation else foundation
                guide += f"- **{term}**: {definition.strip()}\n"
        else:
            guide += "- [Term 1]: Definition and explanation\n"
            guide += "- [Term 2]: Definition and explanation\n"
            guide += "- [Term 3]: Definition and explanation\n"
        guide += "\n"
        
        guide += "## Practice Problems\n\n"
        if "law of action" in topic_name.lower() or "action" in topic_name.lower():
            guide += "1. Derive Newton's second law from the principle of least action for a simple harmonic oscillator\n"
            guide += "2. Compare the Newtonian and Lagrangian approaches to solving a pendulum problem\n"
            guide += "3. Explain how the action principle leads to conservation laws via Noether's theorem\n"
            guide += "4. Apply the principle of least action to electromagnetic field theory\n"
            guide += "5. Analyze the connection between classical action and quantum path integrals\n"
        else:
            guide += "1. Explain the fundamental principles covered in the video collection\n"
            guide += "2. Compare and contrast different approaches presented by various educators\n"
            guide += "3. Apply the concepts to real-world scenarios\n"
            guide += "4. Analyze the historical development of key ideas\n"
        guide += "\n"
        
        return guide
    
    def _generate_faq(self, topic_name, videos):
        faq = f"# Frequently Asked Questions: {topic_name}\n\n"
        
        topic_data = self.knowledge.get_topic_data(topic_name)
        key_concepts = topic_data.get('key_concepts', [])
        math_foundations = topic_data.get('mathematical_foundations', [])
        applications = topic_data.get('applications', [])
        
        faq += f"## What is {topic_name}?\n\n"
        if key_concepts:
            faq += f"{key_concepts[0]} "
            faq += "The curated video collection provides comprehensive coverage from basic concepts to advanced applications, "
            faq += f"exploring {', '.join(key_concepts[1:3]).lower()} and related topics.\n\n"
        else:
            faq += f"{topic_name} is a fundamental area of study that encompasses key principles and concepts essential for understanding this field. "
            faq += "The curated video collection provides comprehensive coverage from basic concepts to advanced applications.\n\n"
        
        faq += f"## Why is {topic_name} important?\n\n"
        if "law of action" in topic_name.lower() or "action" in topic_name.lower():
            faq += "The principle of least action is arguably the most fundamental principle in physics, underlying all other physical laws. "
            faq += "It provides a unified framework for understanding classical mechanics, quantum mechanics, field theory, and general relativity. "
            faq += "Mastering this principle is essential for advanced physics study and research.\n\n"
        elif applications:
            faq += f"Understanding {topic_name} is crucial because it applies to {', '.join(applications[:3]).lower()}. "
            faq += "It provides the foundation for more advanced study and real-world applications.\n\n"
        else:
            faq += f"Understanding {topic_name} is crucial for academic success, professional development, and practical problem-solving. "
            faq += "It provides the foundation for more advanced study and real-world applications.\n\n"
        
        faq += "## How should I approach learning this topic?\n\n"
        if "law of action" in topic_name.lower() or "action" in topic_name.lower():
            faq += "Start with Newton's laws and basic mechanics to build intuition, then progress to energy methods and Lagrangian mechanics. "
            faq += "Focus on understanding the conceptual meaning before diving into mathematical derivations. "
            faq += "Practice applying the principle to simple systems like harmonic oscillators and pendulums.\n\n"
        else:
            faq += "Start with the foundational videos to build a solid understanding, then progress to more advanced content. "
            faq += "Take notes, pause to reflect on key concepts, and try to apply what you learn to practical examples.\n\n"
        
        if math_foundations:
            faq += "## What mathematical background do I need?\n\n"
            if "law of action" in topic_name.lower() or "action" in topic_name.lower():
                faq += "A solid understanding of calculus (derivatives and integrals) is essential. "
                faq += "Familiarity with differential equations, vector calculus, and basic linear algebra will be helpful for advanced topics. "
                faq += "The mathematical foundations include variational calculus and the Euler-Lagrange equation.\n\n"
            else:
                faq += "The mathematical foundations include:\n"
                for foundation in math_foundations[:3]:
                    faq += f"- {foundation}\n"
                faq += "\n"
        
        faq += "## Which videos should I watch first?\n\n"
        faq += "Begin with the highest-rated videos from well-known educational channels:\n"
        
        top_videos = sorted(videos, key=lambda x: x['relevance_score'], reverse=True)[:3]
        for i, video in enumerate(top_videos, 1):
            faq += f"{i}. {video['title']} by {video['channel']} (Score: {video['relevance_score']}/100)\n"
        
        faq += "\n## How long will it take to complete all videos?\n\n"
        total_minutes = 0
        for video in videos:
            duration = video.get('duration', '')
            if ':' in duration:
                try:
                    parts = duration.split(':')
                    if len(parts) == 2:
                        total_minutes += int(parts[0]) + int(parts[1]) / 60
                except:
                    pass
        
        if total_minutes > 0:
            hours = int(total_minutes // 60)
            minutes = int(total_minutes % 60)
            total_duration = f"approximately {hours} hours and {minutes} minutes"
        else:
            total_duration = "approximately 2-4 hours"
        
        faq += f"The total viewing time is {total_duration}, but allow additional time for note-taking, reflection, and practice problems.\n\n"
        
        faq += "## Are there prerequisites for this topic?\n\n"
        if "law of action" in topic_name.lower() or "action" in topic_name.lower():
            faq += "A strong foundation in calculus and basic physics (mechanics) is recommended. "
            faq += "Familiarity with Newton's laws, energy conservation, and basic differential equations will be helpful. "
            faq += "The video collection includes content for various skill levels, from conceptual introductions to advanced mathematical treatments.\n\n"
        else:
            faq += "Basic mathematical and scientific literacy is helpful, but the video collection includes content for various skill levels, "
            faq += "from beginner-friendly explanations to advanced theoretical discussions.\n\n"
        
        return faq
    
    def _generate_timeline_characters(self, topic_name, videos):
        timeline = f"# Timeline and Key Figures: {topic_name}\n\n"
        
        topic_data = self.knowledge.get_topic_data(topic_name)
        historical_timeline = topic_data.get('historical_timeline', {})
        
        timeline += "## Historical Timeline\n\n"
        timeline += f"The development of {topic_name} spans centuries of scientific and intellectual progress:\n\n"
        
        if historical_timeline and len(historical_timeline) > 1:
            for year, data in sorted(historical_timeline.items()):
                if year != "Ancient" and isinstance(data, dict):
                    timeline += f"### {year} - {data['figure']}\n"
                    timeline += f"- {data['contribution']}\n"
                    if 'quote' in data:
                        timeline += f"- **Quote**: \"{data['quote']}\"\n\n"
        else:
            timeline += "### Ancient Period (Before 1600)\n"
            timeline += "- Early philosophical and mathematical foundations\n"
            timeline += "- Initial observations and theoretical frameworks\n\n"
            
            timeline += "### Classical Period (1600-1900)\n"
            timeline += "- Formalization of key principles\n"
            timeline += "- Mathematical development and proofs\n\n"
            
            timeline += "### Modern Era (1900-2000)\n"
            timeline += "- Advanced theoretical frameworks\n"
            timeline += "- Practical applications and technology\n\n"
            
            timeline += "### Contemporary Developments (2000-Present)\n"
            timeline += "- Current research and innovations\n"
            timeline += "- Future directions and possibilities\n\n"
        
        timeline += "## Key Figures\n\n"
        timeline += f"Important contributors to the field of {topic_name}:\n\n"
        
        if historical_timeline and len(historical_timeline) > 1:
            timeline += "### Historical Pioneers\n"
            for year, data in sorted(historical_timeline.items()):
                if year != "Ancient" and isinstance(data, dict):
                    timeline += f"- **{data['figure']} ({year})**: {data['contribution']}\n"
            timeline += "\n"
            
            if "law of action" in topic_name.lower() or "action" in topic_name.lower():
                timeline += "### Modern Developments\n"
                timeline += "- **Emmy Noether (1915)**: Connected symmetries to conservation laws via Noether's theorem\n"
                timeline += "- **Paul Dirac (1933)**: Extended action principles to quantum field theory\n"
                timeline += "- **Julian Schwinger (1948)**: Developed quantum action principle formulation\n\n"
        else:
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
