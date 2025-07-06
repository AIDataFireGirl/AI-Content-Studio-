"""
Editor Agent for AI Content Studio

This agent specializes in reviewing, editing, and improving content drafts.
It focuses on grammar, style, clarity, and overall content quality.
"""

from typing import Dict, Any, Optional, List
from .base_agent import BaseAgent


class EditorAgent(BaseAgent):
    """Agent specialized in reviewing and improving content"""
    
    def __init__(self, verbose: bool = True):
        """
        Initialize Editor Agent
        
        Args:
            verbose: Whether to enable verbose logging
        """
        super().__init__(
            name="Content Editor",
            role="Expert content editor with extensive experience in reviewing, editing, and improving articles, blog posts, and marketing content. Specializes in grammar, style, clarity, and ensuring content meets quality standards.",
            goal="Review and improve content to ensure it is grammatically correct, well-structured, engaging, and meets the highest quality standards while maintaining the original message and tone.",
            verbose=verbose
        )
    
    def review_content(self, 
                      content: str,
                      content_type: str = "article",
                      target_audience: str = "general",
                      review_focus: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Review content and provide feedback
        
        Args:
            content: Content to review
            content_type: Type of content being reviewed
            target_audience: Target audience for the content
            review_focus: Specific areas to focus on (grammar, style, clarity, etc.)
            
        Returns:
            Dict containing review results and suggestions
        """
        if not self.validate_input(content):
            raise ValueError("Content cannot be empty")
        
        # Default review focus areas
        if review_focus is None:
            review_focus = ["grammar", "style", "clarity", "structure", "engagement"]
        
        task_description = f"""
        Review the following {content_type} content for {target_audience} audience:
        
        {content}
        
        Focus areas for review: {', '.join(review_focus)}
        
        Please provide a comprehensive review including:
        1. Overall assessment and score (1-10)
        2. Grammar and spelling issues
        3. Style and tone consistency
        4. Clarity and readability
        5. Structure and flow
        6. Engagement and impact
        7. Specific suggestions for improvement
        8. Positive aspects to maintain
        """
        
        result = self.execute_task(task_description)
        return self._parse_review_result(result)
    
    def edit_content(self, 
                    content: str,
                    edit_instructions: str,
                    preserve_style: bool = True) -> str:
        """
        Edit content based on specific instructions
        
        Args:
            content: Content to edit
            edit_instructions: Specific editing instructions
            preserve_style: Whether to preserve the original writing style
            
        Returns:
            str: Edited content
        """
        task_description = f"""
        Edit the following content according to these instructions:
        
        Content:
        {content}
        
        Edit Instructions:
        {edit_instructions}
        
        Requirements:
        - Follow the edit instructions precisely
        - Maintain the original message and key points
        - Ensure grammatical correctness
        - Improve clarity and flow
        """
        
        if preserve_style:
            task_description += "\n- Preserve the original writing style and tone"
        
        result = self.execute_task(task_description)
        return self.postprocess_output(result)
    
    def improve_content(self, 
                       content: str,
                       improvement_areas: Optional[List[str]] = None) -> str:
        """
        Improve content quality without changing the core message
        
        Args:
            content: Content to improve
            improvement_areas: Specific areas to improve (clarity, engagement, etc.)
            
        Returns:
            str: Improved content
        """
        if improvement_areas is None:
            improvement_areas = ["clarity", "engagement", "flow", "impact"]
        
        task_description = f"""
        Improve the following content by focusing on: {', '.join(improvement_areas)}
        
        Original Content:
        {content}
        
        Please:
        1. Maintain the core message and key points
        2. Improve clarity and readability
        3. Enhance engagement and impact
        4. Ensure smooth flow and transitions
        5. Fix any grammatical or style issues
        6. Make the content more compelling
        """
        
        result = self.execute_task(task_description)
        return self.postprocess_output(result)
    
    def check_grammar_and_style(self, content: str) -> Dict[str, Any]:
        """
        Perform detailed grammar and style check
        
        Args:
            content: Content to check
            
        Returns:
            Dict containing grammar and style analysis
        """
        task_description = f"""
        Perform a detailed grammar and style analysis of the following content:
        
        {content}
        
        Please provide:
        1. Grammar errors and corrections
        2. Style issues and suggestions
        3. Punctuation and formatting issues
        4. Word choice and vocabulary suggestions
        5. Sentence structure improvements
        6. Overall writing quality assessment
        """
        
        result = self.execute_task(task_description)
        return self._parse_grammar_result(result)
    
    def _parse_review_result(self, review_text: str) -> Dict[str, Any]:
        """
        Parse review result into structured format
        
        Args:
            review_text: Raw review text
            
        Returns:
            Dict containing structured review data
        """
        # Simple parsing - in a real implementation, this would be more sophisticated
        return {
            "review_text": review_text,
            "overall_score": self._extract_score(review_text),
            "suggestions": self._extract_suggestions(review_text),
            "positive_aspects": self._extract_positive_aspects(review_text)
        }
    
    def _parse_grammar_result(self, grammar_text: str) -> Dict[str, Any]:
        """
        Parse grammar check result into structured format
        
        Args:
            grammar_text: Raw grammar analysis text
            
        Returns:
            Dict containing structured grammar data
        """
        return {
            "grammar_analysis": grammar_text,
            "errors_found": self._extract_errors(grammar_text),
            "suggestions": self._extract_grammar_suggestions(grammar_text)
        }
    
    def _extract_score(self, text: str) -> Optional[int]:
        """Extract numerical score from review text"""
        # Simple extraction - would be more sophisticated in real implementation
        import re
        score_match = re.search(r'score[:\s]*(\d+)', text.lower())
        return int(score_match.group(1)) if score_match else None
    
    def _extract_suggestions(self, text: str) -> List[str]:
        """Extract improvement suggestions from review text"""
        # Simple extraction - would be more sophisticated in real implementation
        suggestions = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['suggest', 'improve', 'consider', 'try']):
                suggestions.append(line.strip())
        return suggestions
    
    def _extract_positive_aspects(self, text: str) -> List[str]:
        """Extract positive aspects from review text"""
        # Simple extraction - would be more sophisticated in real implementation
        positives = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['good', 'excellent', 'strong', 'effective']):
                positives.append(line.strip())
        return positives
    
    def _extract_errors(self, text: str) -> List[str]:
        """Extract grammar errors from analysis text"""
        # Simple extraction - would be more sophisticated in real implementation
        errors = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['error', 'incorrect', 'wrong', 'fix']):
                errors.append(line.strip())
        return errors
    
    def _extract_grammar_suggestions(self, text: str) -> List[str]:
        """Extract grammar suggestions from analysis text"""
        # Simple extraction - would be more sophisticated in real implementation
        suggestions = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['suggest', 'consider', 'try', 'improve']):
                suggestions.append(line.strip())
        return suggestions
    
    def validate_input(self, input_data: Any) -> bool:
        """
        Validate input for editor agent
        
        Args:
            input_data: Data to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        if isinstance(input_data, str):
            return len(input_data.strip()) > 0
        return False 