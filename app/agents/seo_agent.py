"""
SEO Agent for AI Content Studio

This agent specializes in optimizing content for search engines.
It focuses on keyword research, SEO best practices, and content optimization.
"""

from typing import Dict, Any, Optional, List
from .base_agent import BaseAgent


class SEOAgent(BaseAgent):
    """Agent specialized in SEO optimization"""
    
    def __init__(self, verbose: bool = True):
        """
        Initialize SEO Agent
        
        Args:
            verbose: Whether to enable verbose logging
        """
        super().__init__(
            name="SEO Specialist",
            role="Expert SEO specialist with deep knowledge of search engine optimization, keyword research, and content optimization strategies. Specializes in improving content visibility and ranking in search engines.",
            goal="Optimize content for search engines by implementing SEO best practices, keyword optimization, and ensuring content meets search engine requirements while maintaining quality and readability.",
            verbose=verbose
        )
    
    def optimize_content(self, 
                       content: str,
                       target_keywords: List[str],
                       content_type: str = "article",
                       target_audience: str = "general") -> Dict[str, Any]:
        """
        Optimize content for SEO
        
        Args:
            content: Content to optimize
            target_keywords: List of target keywords
            content_type: Type of content
            target_audience: Target audience
            
        Returns:
            Dict containing optimized content and SEO analysis
        """
        if not self.validate_input(content):
            raise ValueError("Content cannot be empty")
        
        task_description = f"""
        Optimize the following {content_type} content for SEO with target keywords: {', '.join(target_keywords)}
        
        Original Content:
        {content}
        
        Target Audience: {target_audience}
        
        Please provide:
        1. SEO-optimized version of the content
        2. Keyword density analysis
        3. Meta title and description suggestions
        4. Header structure recommendations
        5. Internal linking suggestions
        6. SEO score and recommendations
        7. Technical SEO improvements
        """
        
        result = self.execute_task(task_description)
        return self._parse_seo_result(result, target_keywords)
    
    def generate_meta_tags(self, 
                          content: str,
                          target_keywords: List[str],
                          content_type: str = "article") -> Dict[str, str]:
        """
        Generate meta tags for content
        
        Args:
            content: Content to generate meta tags for
            target_keywords: Target keywords
            content_type: Type of content
            
        Returns:
            Dict containing meta title and description
        """
        task_description = f"""
        Generate SEO-optimized meta title and description for the following {content_type}:
        
        Content:
        {content}
        
        Target Keywords: {', '.join(target_keywords)}
        
        Requirements:
        - Meta title: 50-60 characters
        - Meta description: 150-160 characters
        - Include primary keywords naturally
        - Compelling and click-worthy
        - Accurate representation of content
        """
        
        result = self.execute_task(task_description)
        return self._parse_meta_tags(result)
    
    def suggest_keywords(self, 
                        topic: str,
                        content_type: str = "article",
                        target_audience: str = "general") -> Dict[str, Any]:
        """
        Suggest relevant keywords for a topic
        
        Args:
            topic: Main topic
            content_type: Type of content
            target_audience: Target audience
            
        Returns:
            Dict containing keyword suggestions and analysis
        """
        task_description = f"""
        Suggest relevant keywords for a {content_type} about "{topic}" targeting {target_audience} audience.
        
        Please provide:
        1. Primary keywords (high search volume)
        2. Long-tail keywords (specific phrases)
        3. Related keywords and synonyms
        4. Keyword difficulty assessment
        5. Search intent analysis
        6. Seasonal keyword opportunities
        7. Local SEO keywords (if applicable)
        """
        
        result = self.execute_task(task_description)
        return self._parse_keyword_suggestions(result)
    
    def analyze_content_seo(self, 
                           content: str,
                           target_keywords: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Analyze content for SEO factors
        
        Args:
            content: Content to analyze
            target_keywords: Target keywords to check
            
        Returns:
            Dict containing SEO analysis results
        """
        task_description = f"""
        Perform comprehensive SEO analysis of the following content:
        
        {content}
        """
        
        if target_keywords:
            task_description += f"\n\nTarget Keywords: {', '.join(target_keywords)}"
        
        task_description += """
        
        Please analyze:
        1. Keyword usage and density
        2. Content structure and headers
        3. Readability and user experience
        4. Content length and depth
        5. Internal linking opportunities
        6. Technical SEO factors
        7. Mobile-friendliness considerations
        8. Overall SEO score and recommendations
        """
        
        result = self.execute_task(task_description)
        return self._parse_seo_analysis(result)
    
    def _parse_seo_result(self, seo_text: str, target_keywords: List[str]) -> Dict[str, Any]:
        """
        Parse SEO optimization result
        
        Args:
            seo_text: Raw SEO optimization text
            target_keywords: Target keywords used
            
        Returns:
            Dict containing structured SEO data
        """
        return {
            "optimized_content": self._extract_optimized_content(seo_text),
            "seo_analysis": seo_text,
            "target_keywords": target_keywords,
            "seo_score": self._extract_seo_score(seo_text),
            "recommendations": self._extract_seo_recommendations(seo_text)
        }
    
    def _parse_meta_tags(self, meta_text: str) -> Dict[str, str]:
        """
        Parse meta tags from result
        
        Args:
            meta_text: Raw meta tags text
            
        Returns:
            Dict containing meta title and description
        """
        lines = meta_text.split('\n')
        meta_title = ""
        meta_description = ""
        
        for line in lines:
            if 'title' in line.lower():
                meta_title = line.split(':')[-1].strip()
            elif 'description' in line.lower():
                meta_description = line.split(':')[-1].strip()
        
        return {
            "meta_title": meta_title,
            "meta_description": meta_description
        }
    
    def _parse_keyword_suggestions(self, keyword_text: str) -> Dict[str, Any]:
        """
        Parse keyword suggestions from result
        
        Args:
            keyword_text: Raw keyword suggestions text
            
        Returns:
            Dict containing structured keyword data
        """
        return {
            "keyword_suggestions": keyword_text,
            "primary_keywords": self._extract_primary_keywords(keyword_text),
            "long_tail_keywords": self._extract_long_tail_keywords(keyword_text),
            "keyword_analysis": self._extract_keyword_analysis(keyword_text)
        }
    
    def _parse_seo_analysis(self, analysis_text: str) -> Dict[str, Any]:
        """
        Parse SEO analysis result
        
        Args:
            analysis_text: Raw SEO analysis text
            
        Returns:
            Dict containing structured analysis data
        """
        return {
            "seo_analysis": analysis_text,
            "seo_score": self._extract_seo_score(analysis_text),
            "improvements": self._extract_seo_improvements(analysis_text),
            "strengths": self._extract_seo_strengths(analysis_text)
        }
    
    def _extract_optimized_content(self, text: str) -> str:
        """Extract optimized content from SEO result"""
        # Simple extraction - would be more sophisticated in real implementation
        lines = text.split('\n')
        optimized_content = []
        in_content = False
        
        for line in lines:
            if 'optimized content' in line.lower() or 'updated content' in line.lower():
                in_content = True
                continue
            if in_content and line.strip():
                optimized_content.append(line)
        
        return '\n'.join(optimized_content) if optimized_content else text
    
    def _extract_seo_score(self, text: str) -> Optional[int]:
        """Extract SEO score from analysis"""
        import re
        score_match = re.search(r'seo score[:\s]*(\d+)', text.lower())
        return int(score_match.group(1)) if score_match else None
    
    def _extract_seo_recommendations(self, text: str) -> List[str]:
        """Extract SEO recommendations from analysis"""
        recommendations = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['recommend', 'suggest', 'improve', 'optimize']):
                recommendations.append(line.strip())
        return recommendations
    
    def _extract_primary_keywords(self, text: str) -> List[str]:
        """Extract primary keywords from suggestions"""
        keywords = []
        lines = text.split('\n')
        for line in lines:
            if 'primary' in line.lower() and 'keyword' in line.lower():
                # Extract keywords from the line
                keywords.extend([word.strip() for word in line.split(',') if word.strip()])
        return keywords
    
    def _extract_long_tail_keywords(self, text: str) -> List[str]:
        """Extract long-tail keywords from suggestions"""
        keywords = []
        lines = text.split('\n')
        for line in lines:
            if 'long-tail' in line.lower() or 'long tail' in line.lower():
                # Extract keywords from the line
                keywords.extend([word.strip() for word in line.split(',') if word.strip()])
        return keywords
    
    def _extract_keyword_analysis(self, text: str) -> Dict[str, Any]:
        """Extract keyword analysis from suggestions"""
        return {
            "analysis_text": text,
            "keyword_count": len(self._extract_primary_keywords(text)) + len(self._extract_long_tail_keywords(text))
        }
    
    def _extract_seo_improvements(self, text: str) -> List[str]:
        """Extract SEO improvements from analysis"""
        improvements = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['improve', 'fix', 'optimize', 'enhance']):
                improvements.append(line.strip())
        return improvements
    
    def _extract_seo_strengths(self, text: str) -> List[str]:
        """Extract SEO strengths from analysis"""
        strengths = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['good', 'strong', 'excellent', 'well']):
                strengths.append(line.strip())
        return strengths
    
    def validate_input(self, input_data: Any) -> bool:
        """
        Validate input for SEO agent
        
        Args:
            input_data: Data to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        if isinstance(input_data, str):
            return len(input_data.strip()) > 0
        return False 