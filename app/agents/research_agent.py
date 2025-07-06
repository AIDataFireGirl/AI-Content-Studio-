"""
Research Agent for AI Content Studio

This agent specializes in gathering information, facts, and data for content creation.
It focuses on finding accurate, relevant, and up-to-date information.
"""

from typing import Dict, Any, Optional, List
from .base_agent import BaseAgent


class ResearchAgent(BaseAgent):
    """Agent specialized in research and information gathering"""
    
    def __init__(self, verbose: bool = True):
        """
        Initialize Research Agent
        
        Args:
            verbose: Whether to enable verbose logging
        """
        super().__init__(
            name="Research Specialist",
            role="Expert researcher with extensive experience in gathering accurate, relevant, and up-to-date information from reliable sources. Specializes in fact-checking, data analysis, and providing comprehensive research insights.",
            goal="Gather comprehensive, accurate, and relevant information to support content creation, ensuring all facts are verified and sources are credible.",
            verbose=verbose
        )
    
    def research_topic(self, 
                      topic: str,
                      research_depth: str = "comprehensive",
                      content_type: str = "article",
                      target_audience: str = "general") -> Dict[str, Any]:
        """
        Research a topic comprehensively
        
        Args:
            topic: Topic to research
            research_depth: Level of research (basic, comprehensive, in-depth)
            content_type: Type of content being created
            target_audience: Target audience for the content
            
        Returns:
            Dict containing research findings and insights
        """
        if not self.validate_input(topic):
            raise ValueError("Topic cannot be empty")
        
        task_description = f"""
        Conduct {research_depth} research on the topic: "{topic}"
        
        Content Type: {content_type}
        Target Audience: {target_audience}
        
        Please provide:
        1. Key facts and statistics
        2. Current trends and developments
        3. Expert opinions and quotes
        4. Relevant case studies or examples
        5. Historical context (if applicable)
        6. Controversial aspects or debates
        7. Future implications or predictions
        8. Credible sources and references
        9. Data visualization suggestions
        10. Research gaps or areas for further study
        """
        
        result = self.execute_task(task_description)
        return self._parse_research_result(result, topic)
    
    def fact_check_content(self, 
                          content: str,
                          topic: str) -> Dict[str, Any]:
        """
        Fact-check content for accuracy
        
        Args:
            content: Content to fact-check
            topic: Main topic of the content
            
        Returns:
            Dict containing fact-checking results
        """
        task_description = f"""
        Fact-check the following content about "{topic}":
        
        {content}
        
        Please verify:
        1. All factual claims and statements
        2. Statistics and data accuracy
        3. Quote authenticity and attribution
        4. Date and timeline accuracy
        5. Source credibility and reliability
        6. Context accuracy and completeness
        7. Potential biases or misinformation
        8. Recommendations for corrections
        """
        
        result = self.execute_task(task_description)
        return self._parse_fact_check_result(result)
    
    def gather_statistics(self, 
                         topic: str,
                         time_period: Optional[str] = None,
                         geographic_scope: Optional[str] = None) -> Dict[str, Any]:
        """
        Gather relevant statistics for a topic
        
        Args:
            topic: Topic to gather statistics for
            time_period: Specific time period for data
            geographic_scope: Geographic scope for data
            
        Returns:
            Dict containing statistics and data
        """
        task_description = f"""
        Gather relevant statistics and data for: "{topic}"
        """
        
        if time_period:
            task_description += f"\nTime Period: {time_period}"
        if geographic_scope:
            task_description += f"\nGeographic Scope: {geographic_scope}"
        
        task_description += """
        
        Please provide:
        1. Key statistics and numbers
        2. Growth trends and patterns
        3. Comparative data and benchmarks
        4. Demographic breakdowns
        5. Industry-specific metrics
        6. Economic impact data
        7. Social and cultural statistics
        8. Data sources and reliability
        9. Data visualization suggestions
        10. Limitations and caveats
        """
        
        result = self.execute_task(task_description)
        return self._parse_statistics_result(result)
    
    def find_expert_quotes(self, 
                           topic: str,
                           quote_type: str = "general") -> Dict[str, Any]:
        """
        Find relevant expert quotes for a topic
        
        Args:
            topic: Topic to find quotes for
            quote_type: Type of quotes (general, industry, academic, etc.)
            
        Returns:
            Dict containing expert quotes and insights
        """
        task_description = f"""
        Find relevant {quote_type} expert quotes and insights for: "{topic}"
        
        Please provide:
        1. Expert quotes with proper attribution
        2. Industry leader insights
        3. Academic expert opinions
        4. Thought leader perspectives
        5. Controversial or opposing viewpoints
        6. Historical expert commentary
        7. Future predictions from experts
        8. Expert credentials and credibility
        9. Quote context and relevance
        10. Source verification and reliability
        """
        
        result = self.execute_task(task_description)
        return self._parse_quotes_result(result)
    
    def analyze_trends(self, 
                       topic: str,
                       time_period: str = "recent",
                       trend_type: str = "general") -> Dict[str, Any]:
        """
        Analyze trends related to a topic
        
        Args:
            topic: Topic to analyze trends for
            time_period: Time period for trend analysis
            trend_type: Type of trends to analyze
            
        Returns:
            Dict containing trend analysis
        """
        task_description = f"""
        Analyze {trend_type} trends related to: "{topic}"
        
        Time Period: {time_period}
        
        Please provide:
        1. Current trend analysis
        2. Historical trend patterns
        3. Emerging trends and developments
        4. Trend drivers and factors
        5. Industry-specific trends
        6. Consumer behavior trends
        7. Technology impact on trends
        8. Future trend predictions
        9. Trend implications and consequences
        10. Data sources and methodology
        """
        
        result = self.execute_task(task_description)
        return self._parse_trends_result(result)
    
    def _parse_research_result(self, research_text: str, topic: str) -> Dict[str, Any]:
        """
        Parse research result into structured format
        
        Args:
            research_text: Raw research text
            topic: Original research topic
            
        Returns:
            Dict containing structured research data
        """
        return {
            "topic": topic,
            "research_findings": research_text,
            "key_facts": self._extract_key_facts(research_text),
            "sources": self._extract_sources(research_text),
            "insights": self._extract_insights(research_text),
            "recommendations": self._extract_recommendations(research_text)
        }
    
    def _parse_fact_check_result(self, fact_check_text: str) -> Dict[str, Any]:
        """
        Parse fact-check result into structured format
        
        Args:
            fact_check_text: Raw fact-check text
            
        Returns:
            Dict containing structured fact-check data
        """
        return {
            "fact_check_results": fact_check_text,
            "verified_facts": self._extract_verified_facts(fact_check_text),
            "corrections_needed": self._extract_corrections(fact_check_text),
            "accuracy_score": self._extract_accuracy_score(fact_check_text),
            "sources_verified": self._extract_verified_sources(fact_check_text)
        }
    
    def _parse_statistics_result(self, stats_text: str) -> Dict[str, Any]:
        """
        Parse statistics result into structured format
        
        Args:
            stats_text: Raw statistics text
            
        Returns:
            Dict containing structured statistics data
        """
        return {
            "statistics_data": stats_text,
            "key_numbers": self._extract_key_numbers(stats_text),
            "trends": self._extract_trends(stats_text),
            "data_sources": self._extract_data_sources(stats_text),
            "visualization_suggestions": self._extract_viz_suggestions(stats_text)
        }
    
    def _parse_quotes_result(self, quotes_text: str) -> Dict[str, Any]:
        """
        Parse quotes result into structured format
        
        Args:
            quotes_text: Raw quotes text
            
        Returns:
            Dict containing structured quotes data
        """
        return {
            "expert_quotes": quotes_text,
            "quotes_list": self._extract_quotes(quotes_text),
            "expert_credentials": self._extract_credentials(quotes_text),
            "quote_sources": self._extract_quote_sources(quotes_text)
        }
    
    def _parse_trends_result(self, trends_text: str) -> Dict[str, Any]:
        """
        Parse trends result into structured format
        
        Args:
            trends_text: Raw trends text
            
        Returns:
            Dict containing structured trends data
        """
        return {
            "trend_analysis": trends_text,
            "current_trends": self._extract_current_trends(trends_text),
            "emerging_trends": self._extract_emerging_trends(trends_text),
            "future_predictions": self._extract_future_predictions(trends_text),
            "trend_implications": self._extract_trend_implications(trends_text)
        }
    
    # Helper methods for extracting specific information
    def _extract_key_facts(self, text: str) -> List[str]:
        """Extract key facts from research text"""
        facts = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['fact', 'statistic', 'data', 'figure']):
                facts.append(line.strip())
        return facts
    
    def _extract_sources(self, text: str) -> List[str]:
        """Extract sources from research text"""
        sources = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['source', 'reference', 'study', 'report']):
                sources.append(line.strip())
        return sources
    
    def _extract_insights(self, text: str) -> List[str]:
        """Extract insights from research text"""
        insights = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['insight', 'finding', 'discovery', 'observation']):
                insights.append(line.strip())
        return insights
    
    def _extract_recommendations(self, text: str) -> List[str]:
        """Extract recommendations from research text"""
        recommendations = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['recommend', 'suggest', 'advise', 'propose']):
                recommendations.append(line.strip())
        return recommendations
    
    def _extract_verified_facts(self, text: str) -> List[str]:
        """Extract verified facts from fact-check text"""
        facts = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['verified', 'confirmed', 'accurate', 'correct']):
                facts.append(line.strip())
        return facts
    
    def _extract_corrections(self, text: str) -> List[str]:
        """Extract corrections needed from fact-check text"""
        corrections = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['correction', 'error', 'inaccurate', 'wrong']):
                corrections.append(line.strip())
        return corrections
    
    def _extract_accuracy_score(self, text: str) -> Optional[int]:
        """Extract accuracy score from fact-check text"""
        import re
        score_match = re.search(r'accuracy[:\s]*(\d+)', text.lower())
        return int(score_match.group(1)) if score_match else None
    
    def _extract_verified_sources(self, text: str) -> List[str]:
        """Extract verified sources from fact-check text"""
        sources = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['verified source', 'credible', 'reliable']):
                sources.append(line.strip())
        return sources
    
    def _extract_key_numbers(self, text: str) -> List[str]:
        """Extract key numbers from statistics text"""
        numbers = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['percent', 'million', 'billion', 'thousand']):
                numbers.append(line.strip())
        return numbers
    
    def _extract_trends(self, text: str) -> List[str]:
        """Extract trends from statistics text"""
        trends = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['trend', 'growth', 'increase', 'decrease']):
                trends.append(line.strip())
        return trends
    
    def _extract_data_sources(self, text: str) -> List[str]:
        """Extract data sources from statistics text"""
        sources = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['source', 'data from', 'according to']):
                sources.append(line.strip())
        return sources
    
    def _extract_viz_suggestions(self, text: str) -> List[str]:
        """Extract visualization suggestions from statistics text"""
        suggestions = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['chart', 'graph', 'visualization', 'diagram']):
                suggestions.append(line.strip())
        return suggestions
    
    def _extract_quotes(self, text: str) -> List[str]:
        """Extract quotes from quotes text"""
        quotes = []
        lines = text.split('\n')
        for line in lines:
            if '"' in line or "'" in line:
                quotes.append(line.strip())
        return quotes
    
    def _extract_credentials(self, text: str) -> List[str]:
        """Extract expert credentials from quotes text"""
        credentials = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['phd', 'professor', 'expert', 'specialist']):
                credentials.append(line.strip())
        return credentials
    
    def _extract_quote_sources(self, text: str) -> List[str]:
        """Extract quote sources from quotes text"""
        sources = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['source', 'interview', 'study', 'report']):
                sources.append(line.strip())
        return sources
    
    def _extract_current_trends(self, text: str) -> List[str]:
        """Extract current trends from trends text"""
        trends = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['current', 'present', 'now', 'today']):
                trends.append(line.strip())
        return trends
    
    def _extract_emerging_trends(self, text: str) -> List[str]:
        """Extract emerging trends from trends text"""
        trends = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['emerging', 'new', 'developing', 'growing']):
                trends.append(line.strip())
        return trends
    
    def _extract_future_predictions(self, text: str) -> List[str]:
        """Extract future predictions from trends text"""
        predictions = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['future', 'prediction', 'forecast', 'will']):
                predictions.append(line.strip())
        return predictions
    
    def _extract_trend_implications(self, text: str) -> List[str]:
        """Extract trend implications from trends text"""
        implications = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['implication', 'impact', 'effect', 'consequence']):
                implications.append(line.strip())
        return implications
    
    def validate_input(self, input_data: Any) -> bool:
        """
        Validate input for research agent
        
        Args:
            input_data: Data to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        if isinstance(input_data, str):
            return len(input_data.strip()) > 0
        return False 