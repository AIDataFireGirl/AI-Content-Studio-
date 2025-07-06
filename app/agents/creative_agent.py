"""
Creative Agent for AI Content Studio

This agent specializes in generating creative content ideas, brainstorming,
and innovative approaches to content creation.
"""

from typing import Dict, Any, Optional, List
from .base_agent import BaseAgent


class CreativeAgent(BaseAgent):
    """Agent specialized in creative content ideation"""
    
    def __init__(self, verbose: bool = True):
        """
        Initialize Creative Agent
        
        Args:
            verbose: Whether to enable verbose logging
        """
        super().__init__(
            name="Creative Specialist",
            role="Expert creative content strategist with extensive experience in brainstorming, ideation, and innovative content approaches. Specializes in generating unique, engaging, and viral-worthy content ideas.",
            goal="Generate innovative, creative, and engaging content ideas that capture audience attention, drive engagement, and stand out in the digital landscape.",
            verbose=verbose
        )
    
    def generate_content_ideas(self, 
                              topic: str,
                              content_type: str = "article",
                              target_audience: str = "general",
                              idea_count: int = 10,
                              creativity_level: str = "high") -> Dict[str, Any]:
        """
        Generate creative content ideas for a topic
        
        Args:
            topic: Main topic for content ideas
            content_type: Type of content to generate ideas for
            target_audience: Target audience
            idea_count: Number of ideas to generate
            creativity_level: Level of creativity (low, medium, high)
            
        Returns:
            Dict containing creative content ideas
        """
        if not self.validate_input(topic):
            raise ValueError("Topic cannot be empty")
        
        task_description = f"""
        Generate {idea_count} {creativity_level}-creativity content ideas for a {content_type} about "{topic}" targeting {target_audience} audience.
        
        Please provide:
        1. Unique and innovative angles
        2. Viral-worthy concepts
        3. Engaging storytelling approaches
        4. Interactive content ideas
        5. Visual and multimedia concepts
        6. Trending topic connections
        7. Controversial or thought-provoking angles
        8. Emotional appeal strategies
        9. Shareable content formats
        10. Cross-platform adaptation ideas
        
        For each idea, include:
        - Title/Headline
        - Brief description
        - Target audience appeal
        - Engagement potential
        - Implementation difficulty
        - Expected impact
        """
        
        result = self.execute_task(task_description)
        return self._parse_ideas_result(result, topic)
    
    def brainstorm_headlines(self, 
                           topic: str,
                           content_type: str = "article",
                           headline_count: int = 15,
                           headline_style: str = "clickbait") -> Dict[str, Any]:
        """
        Brainstorm creative headlines for content
        
        Args:
            topic: Topic for headlines
            content_type: Type of content
            headline_count: Number of headlines to generate
            headline_style: Style of headlines (clickbait, professional, creative, etc.)
            
        Returns:
            Dict containing headline ideas
        """
        task_description = f"""
        Generate {headline_count} {headline_style} headlines for a {content_type} about "{topic}".
        
        Headline styles to consider:
        - How-to guides
        - Listicles
        - Question-based
        - Controversial statements
        - Emotional triggers
        - Curiosity gaps
        - Number-based
        - Problem-solution
        - Behind-the-scenes
        - Expert insights
        
        For each headline, include:
        - Headline text
        - Style category
        - Emotional appeal
        - Click-through potential
        - SEO friendliness
        - Brand safety
        """
        
        result = self.execute_task(task_description)
        return self._parse_headlines_result(result)
    
    def create_content_hooks(self, 
                            topic: str,
                            hook_count: int = 10,
                            hook_type: str = "opening") -> Dict[str, Any]:
        """
        Create engaging content hooks
        
        Args:
            topic: Topic for hooks
            hook_count: Number of hooks to generate
            hook_type: Type of hook (opening, social media, email, etc.)
            
        Returns:
            Dict containing hook ideas
        """
        task_description = f"""
        Create {hook_count} engaging {hook_type} hooks for content about "{topic}".
        
        Hook types to consider:
        - Story-based openings
        - Shocking statistics
        - Provocative questions
        - Personal anecdotes
        - Current events connection
        - Problem identification
        - Promise of value
        - Controversial statements
        - Visual descriptions
        - Expert quotes
        
        For each hook, include:
        - Hook text
        - Hook type
        - Emotional impact
        - Engagement potential
        - Relevance to topic
        """
        
        result = self.execute_task(task_description)
        return self._parse_hooks_result(result)
    
    def generate_viral_concepts(self, 
                               topic: str,
                               platform: str = "general",
                               concept_count: int = 8) -> Dict[str, Any]:
        """
        Generate viral content concepts
        
        Args:
            topic: Topic for viral concepts
            platform: Target platform (social media, blog, video, etc.)
            concept_count: Number of concepts to generate
            
        Returns:
            Dict containing viral concept ideas
        """
        task_description = f"""
        Generate {concept_count} viral content concepts for "{topic}" on {platform} platform.
        
        Viral elements to consider:
        - Emotional triggers (joy, anger, surprise, fear)
        - Social proof and relatability
        - Trending topic connections
        - Shareable formats
        - Interactive elements
        - User-generated content potential
        - Influencer collaboration ideas
        - Hashtag campaigns
        - Challenge concepts
        - Behind-the-scenes content
        
        For each concept, include:
        - Concept description
        - Viral potential score (1-10)
        - Target emotions
        - Shareability factors
        - Implementation strategy
        - Expected reach
        """
        
        result = self.execute_task(task_description)
        return self._parse_viral_concepts_result(result)
    
    def create_content_series(self, 
                             topic: str,
                             series_length: int = 5,
                             content_type: str = "article") -> Dict[str, Any]:
        """
        Create content series concepts
        
        Args:
            topic: Main topic for series
            series_length: Number of pieces in series
            content_type: Type of content
            
        Returns:
            Dict containing series concept
        """
        task_description = f"""
        Create a {series_length}-part {content_type} series about "{topic}".
        
        Series structure to consider:
        - Progressive learning path
        - Problem-solution progression
        - Story arc development
        - Expert interview series
        - Case study progression
        - How-to step sequence
        - Industry deep dive
        - Trend analysis timeline
        - Comparison series
        - Behind-the-scenes journey
        
        For the series, include:
        - Series theme and concept
        - Individual piece titles
        - Content flow and progression
        - Engagement hooks for each piece
        - Cross-promotion strategies
        - Series completion incentives
        """
        
        result = self.execute_task(task_description)
        return self._parse_series_result(result)
    
    def _parse_ideas_result(self, ideas_text: str, topic: str) -> Dict[str, Any]:
        """
        Parse content ideas result into structured format
        
        Args:
            ideas_text: Raw ideas text
            topic: Original topic
            
        Returns:
            Dict containing structured ideas data
        """
        return {
            "topic": topic,
            "ideas_text": ideas_text,
            "idea_list": self._extract_ideas(ideas_text),
            "creative_angles": self._extract_creative_angles(ideas_text),
            "engagement_potential": self._extract_engagement_potential(ideas_text)
        }
    
    def _parse_headlines_result(self, headlines_text: str) -> Dict[str, Any]:
        """
        Parse headlines result into structured format
        
        Args:
            headlines_text: Raw headlines text
            
        Returns:
            Dict containing structured headlines data
        """
        return {
            "headlines_text": headlines_text,
            "headline_list": self._extract_headlines(headlines_text),
            "headline_styles": self._extract_headline_styles(headlines_text),
            "click_through_potential": self._extract_click_through_potential(headlines_text)
        }
    
    def _parse_hooks_result(self, hooks_text: str) -> Dict[str, Any]:
        """
        Parse hooks result into structured format
        
        Args:
            hooks_text: Raw hooks text
            
        Returns:
            Dict containing structured hooks data
        """
        return {
            "hooks_text": hooks_text,
            "hook_list": self._extract_hooks(hooks_text),
            "hook_types": self._extract_hook_types(hooks_text),
            "emotional_impact": self._extract_emotional_impact(hooks_text)
        }
    
    def _parse_viral_concepts_result(self, viral_text: str) -> Dict[str, Any]:
        """
        Parse viral concepts result into structured format
        
        Args:
            viral_text: Raw viral concepts text
            
        Returns:
            Dict containing structured viral concepts data
        """
        return {
            "viral_concepts_text": viral_text,
            "concept_list": self._extract_concepts(viral_text),
            "viral_scores": self._extract_viral_scores(viral_text),
            "emotional_triggers": self._extract_emotional_triggers(viral_text)
        }
    
    def _parse_series_result(self, series_text: str) -> Dict[str, Any]:
        """
        Parse series result into structured format
        
        Args:
            series_text: Raw series text
            
        Returns:
            Dict containing structured series data
        """
        return {
            "series_text": series_text,
            "series_concept": self._extract_series_concept(series_text),
            "series_parts": self._extract_series_parts(series_text),
            "series_flow": self._extract_series_flow(series_text)
        }
    
    # Helper methods for extracting specific information
    def _extract_ideas(self, text: str) -> List[str]:
        """Extract content ideas from text"""
        ideas = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['idea', 'concept', 'approach', 'angle']):
                ideas.append(line.strip())
        return ideas
    
    def _extract_creative_angles(self, text: str) -> List[str]:
        """Extract creative angles from ideas text"""
        angles = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['angle', 'perspective', 'viewpoint', 'approach']):
                angles.append(line.strip())
        return angles
    
    def _extract_engagement_potential(self, text: str) -> List[str]:
        """Extract engagement potential from ideas text"""
        engagement = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['engagement', 'viral', 'shareable', 'interactive']):
                engagement.append(line.strip())
        return engagement
    
    def _extract_headlines(self, text: str) -> List[str]:
        """Extract headlines from text"""
        headlines = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['headline', 'title', 'how to', 'why', 'what']):
                headlines.append(line.strip())
        return headlines
    
    def _extract_headline_styles(self, text: str) -> List[str]:
        """Extract headline styles from text"""
        styles = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['style', 'type', 'format', 'category']):
                styles.append(line.strip())
        return styles
    
    def _extract_click_through_potential(self, text: str) -> List[str]:
        """Extract click-through potential from headlines text"""
        potential = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['click', 'ctr', 'potential', 'appeal']):
                potential.append(line.strip())
        return potential
    
    def _extract_hooks(self, text: str) -> List[str]:
        """Extract hooks from text"""
        hooks = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['hook', 'opening', 'intro', 'start']):
                hooks.append(line.strip())
        return hooks
    
    def _extract_hook_types(self, text: str) -> List[str]:
        """Extract hook types from text"""
        types = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['story', 'statistic', 'question', 'anecdote']):
                types.append(line.strip())
        return types
    
    def _extract_emotional_impact(self, text: str) -> List[str]:
        """Extract emotional impact from hooks text"""
        impact = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['emotional', 'feeling', 'impact', 'response']):
                impact.append(line.strip())
        return impact
    
    def _extract_concepts(self, text: str) -> List[str]:
        """Extract viral concepts from text"""
        concepts = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['concept', 'idea', 'campaign', 'challenge']):
                concepts.append(line.strip())
        return concepts
    
    def _extract_viral_scores(self, text: str) -> List[str]:
        """Extract viral scores from text"""
        scores = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['score', 'viral', 'potential', 'rating']):
                scores.append(line.strip())
        return scores
    
    def _extract_emotional_triggers(self, text: str) -> List[str]:
        """Extract emotional triggers from viral concepts text"""
        triggers = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['joy', 'anger', 'surprise', 'fear', 'emotion']):
                triggers.append(line.strip())
        return triggers
    
    def _extract_series_concept(self, text: str) -> str:
        """Extract series concept from text"""
        lines = text.split('\n')
        for line in lines:
            if 'concept' in line.lower() or 'theme' in line.lower():
                return line.strip()
        return ""
    
    def _extract_series_parts(self, text: str) -> List[str]:
        """Extract series parts from text"""
        parts = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['part', 'piece', 'episode', 'chapter']):
                parts.append(line.strip())
        return parts
    
    def _extract_series_flow(self, text: str) -> List[str]:
        """Extract series flow from text"""
        flow = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['flow', 'progression', 'sequence', 'order']):
                flow.append(line.strip())
        return flow
    
    def validate_input(self, input_data: Any) -> bool:
        """
        Validate input for creative agent
        
        Args:
            input_data: Data to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        if isinstance(input_data, str):
            return len(input_data.strip()) > 0
        return False 