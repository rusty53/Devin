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
        
        topic_data = self.knowledge.get_topic_data(topic_name)
        key_concepts = topic_data.get('key_concepts', [])
        math_foundations = topic_data.get('mathematical_foundations', [])
        learning_progression = topic_data.get('learning_progression', [])
        practice_problems = topic_data.get('practice_problems', [])
        
        guide += "## Learning Objectives\n\n"
        guide += "By completing this study guide, you will be able to:\n\n"
        
        guide += "### Beginner Level\n"
        if key_concepts:
            for i, concept in enumerate(key_concepts[:2], 1):
                guide += f"{i}. Explain {concept.lower()}\n"
        guide += f"3. State and apply Newton's three laws of motion\n"
        guide += f"4. Understand the relationship between action principles and Newton's laws\n\n"
        
        guide += "### Intermediate Level\n"
        guide += "1. Set up and solve problems using Newton's laws\n"
        guide += "2. Calculate action integrals for simple systems\n"
        guide += "3. Apply the Euler-Lagrange equation to derive equations of motion\n"
        guide += "4. Use energy methods and conservation principles\n\n"
        
        guide += "### Advanced Level\n"
        guide += "1. Connect classical mechanics to quantum mechanics via path integrals\n"
        guide += "2. Understand how symmetries relate to conservation laws\n"
        guide += "3. Appreciate the unifying power of variational principles\n"
        guide += "4. Recognize action principles in field theory and relativity\n\n"
        
        guide += "## Study Schedule\n\n"
        
        sorted_videos = sorted(videos, key=lambda x: x['relevance_score'], reverse=True)
        
        guide += "### Week 1: Foundations\n"
        guide += "**Recommended Videos:**\n"
        for video in sorted_videos[:3]:
            guide += f"- \"{video['title']}\" ({video['duration']}) by {video['channel']}\n"
        
        guide += "\n**Key Concepts to Master:**\n"
        guide += "- **Inertia**: Objects resist changes in motion\n"
        guide += "- **F = ma**: Quantitative relationship between force, mass, and acceleration\n"
        guide += "- **Action-Reaction**: Forces always come in pairs acting on different objects\n\n"
        
        guide += "**Practice Problems:**\n"
        if practice_problems:
            for problem in practice_problems[:2]:
                guide += f"1. {problem}\n"
        guide += "\n**Common Misconceptions to Address:**\n"
        guide += "- Normal force and weight are NOT action-reaction pairs (they act on the same object)\n"
        guide += "- Heavier objects do NOT fall faster in vacuum\n"
        guide += "- Force is NOT needed to maintain constant velocity\n\n"
        
        guide += "### Week 2: Energy Methods\n"
        guide += "**Recommended Videos:**\n"
        for video in sorted_videos[3:6]:
            guide += f"- \"{video['title']}\" ({video['duration']}) by {video['channel']}\n"
        
        guide += "\n**Key Concepts to Master:**\n"
        guide += "- **Kinetic Energy**: T = ½mv²\n"
        guide += "- **Potential Energy**: Various forms (gravitational, elastic, etc.)\n"
        guide += "- **Conservation of Energy**: Total energy remains constant in isolated systems\n"
        guide += "- **Optimization in Nature**: Why physical systems follow certain paths\n\n"
        
        guide += "**Activities:**\n"
        guide += "1. **Brachistochrone Problem**: Understand the curve of fastest descent\n"
        guide += "2. **Fermat's Principle**: Light follows the path of least time\n"
        guide += "3. **Energy Diagrams**: Sketch potential energy vs. position graphs\n\n"
        
        guide += "**Mathematical Tools:**\n"
        guide += "- Basic calculus (derivatives and integrals)\n"
        guide += "- Vector addition and components\n"
        guide += "- Trigonometry for inclined planes and projectile motion\n\n"
        
        if len(sorted_videos) > 6:
            guide += "### Week 3: Action Principle\n"
            guide += "**Recommended Videos:**\n"
            for video in sorted_videos[6:9]:
                guide += f"- \"{video['title']}\" ({video['duration']}) by {video['channel']}\n"
            
            guide += "\n**Key Concepts to Master:**\n"
            guide += "- **Action Definition**: S = ∫ L dt where L = T - V\n"
            guide += "- **Lagrangian**: L = Kinetic Energy - Potential Energy\n"
            guide += "- **Variational Principle**: δS = 0 for physical paths\n"
            guide += "- **Euler-Lagrange Equation**: d/dt(∂L/∂q̇) - ∂L/∂q = 0\n\n"
            
            guide += "**Advanced Topics:**\n"
            guide += "1. **Generalized Coordinates**: Beyond Cartesian coordinates\n"
            guide += "2. **Constraints**: How to handle systems with restrictions\n"
            guide += "3. **Symmetries**: Connection to conservation laws (Noether's theorem)\n\n"
        
        if len(sorted_videos) > 9:
            guide += "### Week 4: Advanced Applications\n"
            guide += "**Recommended Videos:**\n"
            for video in sorted_videos[9:]:
                guide += f"- \"{video['title']}\" ({video['duration']}) by {video['channel']}\n"
            
            guide += "\n**Advanced Concepts:**\n"
            guide += "- **Path Integrals**: Quantum mechanical formulation\n"
            guide += "- **Field Theory**: Action principles for continuous systems\n"
            guide += "- **General Relativity**: Einstein-Hilbert action\n"
            guide += "- **Gauge Theories**: Symmetries in particle physics\n\n"
            
            guide += "**Research Projects:**\n"
            guide += "1. **Historical Development**: Trace the evolution from Newton to Lagrange to modern physics\n"
            guide += "2. **Applications**: Choose a specific field (robotics, astrophysics, etc.) and explore how action principles apply\n"
            guide += "3. **Computational Methods**: Use software to solve complex mechanical systems\n\n"
        
        if practice_problems:
            guide += "## Practice Problems\n\n"
            for i, problem in enumerate(practice_problems, 1):
                guide += f"{i}. {problem}\n"
            guide += "\n"
        
        guide += "## Problem-Solving Strategy\n\n"
        guide += "1. Identify the system and constraints\n"
        guide += "2. Choose appropriate generalized coordinates\n"
        guide += "3. Write kinetic and potential energy expressions\n"
        guide += "4. Form the Lagrangian L = T - V\n"
        guide += "5. Apply Euler-Lagrange equation\n"
        guide += "6. Solve the resulting differential equation\n\n"
        
        guide += "## Self-Assessment Questions\n\n"
        guide += "1. What is the difference between mass and weight?\n"
        guide += "2. Why don't action-reaction forces cancel each other out?\n"
        guide += "3. What makes the principle of least action \"least\"?\n"
        guide += "4. How does quantum mechanics use the action principle?\n\n"
        
        guide += "## Assessment and Mastery\n\n"
        guide += "You'll know you've mastered this material when you can:\n"
        guide += "- Solve mechanics problems using multiple approaches\n"
        guide += "- Explain physical principles to others clearly\n"
        guide += "- See connections between different areas of physics\n"
        guide += "- Appreciate the elegance and power of variational principles\n"
        guide += "- Apply these concepts to new and unfamiliar situations\n\n"
        
        guide += "## Additional Resources\n\n"
        guide += "### Textbooks\n"
        guide += "- \"Classical Mechanics\" by Herbert Goldstein\n"
        guide += "- \"The Feynman Lectures on Physics\" Volume I\n"
        guide += "- \"Introduction to Classical Mechanics\" by David Morin\n\n"
        
        guide += "### Online Tools\n"
        guide += "- PhET Interactive Simulations (University of Colorado)\n"
        guide += "- Wolfram Alpha for calculations\n"
        guide += "- GeoGebra for visualizations\n\n"
        
        guide += "### Mathematical Prerequisites\n"
        guide += "- Single-variable calculus (derivatives and integrals)\n"
        guide += "- Basic differential equations\n"
        guide += "- Vector algebra and trigonometry\n"
        guide += "- Some multivariable calculus for advanced topics\n\n"
        
        guide += "### Extension Activities\n"
        guide += "1. **Simulation**: Create a computer program that demonstrates the principle of least action\n"
        guide += "2. **Experiment**: Design and conduct an experiment that illustrates Newton's laws\n"
        guide += "3. **Teaching**: Create educational materials to explain these concepts to others\n"
        guide += "4. **Research**: Investigate a current application of action principles in modern physics or engineering\n\n"
        
        return guide
    
    def _generate_faq(self, topic_name, videos):
        faq = f"# Frequently Asked Questions: {topic_name}\n\n"
        
        topic_data = self.knowledge.get_topic_data(topic_name)
        key_concepts = topic_data.get('key_concepts', [])
        math_foundations = topic_data.get('mathematical_foundations', [])
        applications = topic_data.get('applications', [])
        misconceptions = topic_data.get('common_misconceptions', [])
        
        faq += f"## What is {topic_name}?\n\n"
        if key_concepts:
            faq += f"**A:** {key_concepts[0]} "
            faq += "The curated video collection provides comprehensive coverage from basic concepts to advanced applications, "
            faq += f"exploring {', '.join(key_concepts[1:3]).lower()} and related topics.\n\n"
        else:
            faq += f"**A:** {topic_name} is a fundamental area of study that encompasses key principles and concepts essential for understanding this field. "
            faq += "The curated video collection provides comprehensive coverage from basic concepts to advanced applications.\n\n"
        
        faq += f"## Why is {topic_name} important?\n\n"
        if "law of action" in topic_name.lower() or "action" in topic_name.lower():
            faq += "**A:** The principle of least action is arguably the most fundamental principle in physics, underlying all other physical laws. "
            faq += "It provides a unified framework for understanding classical mechanics, quantum mechanics, field theory, and general relativity. "
            faq += "Mastering this principle is essential for advanced physics study and research.\n\n"
        elif applications:
            faq += f"**A:** Understanding {topic_name} is crucial because it applies to {', '.join(applications[:3]).lower()}. "
            faq += "It provides the foundation for more advanced study and real-world applications.\n\n"
        else:
            faq += f"**A:** Understanding {topic_name} is crucial for academic success, professional development, and practical problem-solving. "
            faq += "It provides the foundation for more advanced study and real-world applications.\n\n"
        
        if misconceptions:
            faq += "## What are common misconceptions?\n\n"
            for i, misconception in enumerate(misconceptions, 1):
                faq += f"**A{i}:** {misconception}\n\n"
        
        faq += "## How should I approach learning this topic?\n\n"
        if "law of action" in topic_name.lower() or "action" in topic_name.lower():
            faq += "**A:** Start with Newton's laws and basic mechanics to build intuition, then progress to energy methods and Lagrangian mechanics. "
            faq += "Focus on understanding the conceptual meaning before diving into mathematical derivations. "
            faq += "Practice applying the principle to simple systems like harmonic oscillators and pendulums.\n\n"
        else:
            faq += "**A:** Start with the foundational videos to build a solid understanding, then progress to more advanced content. "
            faq += "Take notes, pause to reflect on key concepts, and try to apply what you learn to practical examples.\n\n"
        
        if math_foundations:
            faq += "## What mathematical background do I need?\n\n"
            if "law of action" in topic_name.lower() or "action" in topic_name.lower():
                faq += "**A:** A solid understanding of calculus (derivatives and integrals) is essential. "
                faq += "Familiarity with differential equations, vector calculus, and basic linear algebra will be helpful for advanced topics. "
                faq += "The mathematical foundations include variational calculus and the Euler-Lagrange equation.\n\n"
            else:
                faq += "**A:** The mathematical foundations include:\n"
                for foundation in math_foundations[:3]:
                    faq += f"- {foundation}\n"
                faq += "\n"
        
        faq += "## Which videos should I watch first?\n\n"
        faq += "**A:** Begin with the highest-rated videos from well-known educational channels:\n"
        
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
        
        faq += f"**A:** The total viewing time is {total_duration}, but allow additional time for note-taking, reflection, and practice problems.\n\n"
        
        faq += "## Are there prerequisites for this topic?\n\n"
        if "law of action" in topic_name.lower() or "action" in topic_name.lower():
            faq += "**A:** A strong foundation in calculus and basic physics (mechanics) is recommended. "
            faq += "Familiarity with Newton's laws, energy conservation, and basic differential equations will be helpful. "
            faq += "The video collection includes content for various skill levels, from conceptual introductions to advanced mathematical treatments.\n\n"
        else:
            faq += "**A:** Basic mathematical and scientific literacy is helpful, but the video collection includes content for various skill levels, "
            faq += "from beginner-friendly explanations to advanced theoretical discussions.\n\n"
        
        faq += "## How do I know if I understand the material?\n\n"
        faq += "**A:** You understand when you can:\n"
        faq += "- Solve problems using multiple approaches\n"
        faq += "- Explain concepts to someone else clearly\n"
        faq += "- Predict what will happen in new situations\n"
        faq += "- See connections between different areas of physics\n"
        faq += "- Appreciate the elegance and unity of the principles\n\n"
        
        if applications:
            faq += "## Where is this used in practice?\n\n"
            faq += "**A:** Everywhere! Examples include:\n"
            for application in applications:
                category = application.split(' and ')[0]
                faq += f"- **{category}**: {application}\n"
            faq += "\n"
        
        faq += "## What learning strategies work best?\n\n"
        faq += "**A:** \n"
        faq += "1. **Start with examples**: Work through many concrete problems\n"
        faq += "2. **Visualize**: Use simulations and animations\n"
        faq += "3. **Connect to experience**: Relate to everyday phenomena\n"
        faq += "4. **Teach others**: Explaining forces you to understand deeply\n"
        faq += "5. **Ask 'what if'**: Explore variations and limiting cases\n\n"
        
        return faq
    
    def _generate_timeline_characters(self, topic_name, videos):
        timeline = f"# Timeline and Key Figures: {topic_name}\n\n"
        
        topic_data = self.knowledge.get_topic_data(topic_name)
        historical_timeline = topic_data.get('historical_timeline', {})
        institutions = topic_data.get('institutions', [])
        
        timeline += "## Historical Timeline\n\n"
        timeline += f"The development of {topic_name} spans centuries of scientific and intellectual progress:\n\n"
        
        if historical_timeline and len(historical_timeline) > 1:
            ancient_figures = [k for k in historical_timeline.keys() if 'BCE' in k or 'CE' in k]
            if ancient_figures:
                timeline += "### Ancient Period\n\n"
                for year in sorted(ancient_figures):
                    data = historical_timeline[year]
                    timeline += f"**{year} - {data['figure']}**\n"
                    timeline += f"- {data['contribution']}\n"
                    timeline += f"- {data['details']}\n"
                    if 'quote' in data:
                        timeline += f"- **Quote**: \"{data['quote']}\"\n\n"
            
            classical_figures = [k for k in historical_timeline.keys() if k.isdigit() and 1600 <= int(k) <= 1900]
            classical_figures.extend([k for k in historical_timeline.keys() if 's' in k and any(char.isdigit() for char in k)])
            if classical_figures:
                timeline += "### Classical Period (1600-1900)\n\n"
                for year in sorted(classical_figures, key=lambda x: int(x.replace('s', '')) if 's' in x else int(x)):
                    data = historical_timeline[year]
                    timeline += f"**{year} - {data['figure']}**\n"
                    timeline += f"- {data['contribution']}\n"
                    if 'details' in data:
                        timeline += f"- {data['details']}\n"
                    if 'quote' in data:
                        timeline += f"- **Quote**: \"{data['quote']}\"\n\n"
            
            modern_figures = [k for k in historical_timeline.keys() if k.isdigit() and 1900 <= int(k) <= 2000]
            if modern_figures:
                timeline += "### Modern Era (1900-2000)\n\n"
                for year in sorted(modern_figures, key=int):
                    data = historical_timeline[year]
                    timeline += f"**{year} - {data['figure']}**\n"
                    timeline += f"- {data['contribution']}\n"
                    if 'details' in data:
                        timeline += f"- {data['details']}\n"
                    if 'quote' in data:
                        timeline += f"- **Quote**: \"{data['quote']}\"\n\n"
            
            timeline += "### Contemporary Developments (2000-Present)\n\n"
            timeline += "- Quantum computing and information theory\n"
            timeline += "- Condensed matter physics and many-body systems\n"
            timeline += "- String theory and theories of quantum gravity\n"
            timeline += "- Computational physics and numerical methods\n\n"
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
        
        timeline += "## Detailed Biographies\n\n"
        if historical_timeline:
            key_figures = ["1687", "1744", "1788", "1833", "1948"]
            for year in key_figures:
                if year in historical_timeline:
                    data = historical_timeline[year]
                    timeline += f"### {data['figure']}\n\n"
                    if 'background' in data:
                        timeline += f"**Background**: {data['background']}\n"
                    timeline += f"**Major Contributions**:\n"
                    timeline += f"- {data['contribution']}\n"
                    if 'innovation' in data:
                        timeline += f"- {data['innovation']}\n"
                    if 'personality' in data:
                        timeline += f"**Personal Note**: {data['personality']}\n"
                    if 'philosophy' in data:
                        timeline += f"**Philosophy**: {data['philosophy']}\n"
                    timeline += f"**Legacy**: {data['contribution']}\n"
                    if 'quote' in data:
                        timeline += f"**Quote**: \"{data['quote']}\"\n\n"
        
        if institutions:
            timeline += "## Institutional Development\n\n"
            timeline += "### Academic Institutions\n"
            for institution in institutions:
                timeline += f"- **{institution}**\n"
            timeline += "\n"
            
            timeline += "### Scientific Societies\n"
            timeline += "- **Royal Society of London** (1660): Newton was president\n"
            timeline += "- **French Academy of Sciences** (1666): Lagrange was a member\n"
            timeline += "- **American Physical Society** (1899): Modern physics community\n"
            timeline += "- **Nobel Foundation** (1901): Recognizes physics achievements\n\n"
        
        timeline += "## Modern Applications\n\n"
        timeline += "### Current Research Areas\n"
        timeline += "- Quantum gravity and theories of everything\n"
        timeline += "- Dark matter and dark energy\n"
        timeline += "- Quantum computing and information\n"
        timeline += "- Many-body quantum systems\n"
        timeline += "- Artificial intelligence applications\n\n"
        
        timeline += "### Technological Applications\n"
        timeline += "- Clean energy and sustainability\n"
        timeline += "- Medical physics and biotechnology\n"
        timeline += "- Advanced materials and nanotechnology\n"
        timeline += "- Space exploration and colonization\n\n"
        
        timeline += "## Educational Contributors\n\n"
        timeline += "The video collection features content from leading educators:\n"
        
        channels = list(set([video['channel'] for video in videos]))
        for channel in channels[:5]:
            timeline += f"- **{channel}**: Educational content and explanations\n"
        
        timeline += "\nThe story of the Law of Action in physics is ultimately a story of human curiosity and ingenuity, showing how mathematical principles can reveal the deep underlying unity and beauty of the natural world.\n"
        
        return timeline
    
    def save_content(self, content, base_filename):
        for content_type, text in content.items():
            filename = f"{base_filename}_{content_type}.md"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(text)
