"""
SEO Optimization Task for AI Content Studio

This task handles SEO optimization workflows.
"""

from typing import Dict, Any, Optional, List
from .base_task import BaseTask
from app.agents.seo_agent import SEOAgent


class SEOOptimizationTask(BaseTask):
    """Task for SEO optimization"""
    
    def __init__(self, seo_agent: SEOAgent):
        """
        Initialize SEO Optimization Task
        
        Args:
            seo_agent: Agent for SEO optimization
        """
        self.seo_agent = seo_agent
        
        super().__init__(
            name="SEO Optimization",
            description="Optimize content for search engines with keyword research and SEO best practices",
            agent=seo_agent,
            expected_output="SEO-optimized content with meta tags and keyword analysis"
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
            target_keywords: Target keywords
            content_type: Type of content
            target_audience: Target audience
            
        Returns:
            Dict containing SEO optimization results
        """
        seo_result = self.seo_agent.optimize_content(
            content=content,
            target_keywords=target_keywords,
            content_type=content_type,
            target_audience=target_audience
        )
        
        return {
            "seo_data": seo_result,
            "original_content": content,
            "optimization_timestamp": self._get_timestamp(),
            "status": "optimized"
        }
    
    def generate_meta_tags(self, 
                          content: str,
                          target_keywords: List[str],
                          content_type: str = "article") -> Dict[str, Any]:
        """
        Generate meta tags for content
        
        Args:
            content: Content to generate meta tags for
            target_keywords: Target keywords
            content_type: Type of content
            
        Returns:
            Dict containing meta tags
        """
        meta_tags = self.seo_agent.generate_meta_tags(
            content=content,
            target_keywords=target_keywords,
            content_type=content_type
        )
        
        return {
            "meta_tags": meta_tags,
            "content": content,
            "generation_timestamp": self._get_timestamp(),
            "status": "meta_tags_generated"
        }
    
    def _get_timestamp(self) -> str:
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now().isoformat() 