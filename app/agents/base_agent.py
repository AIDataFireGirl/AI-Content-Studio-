"""
Base Agent class for AI Content Studio

This module provides the foundation for all specialized agents in the content studio.
It includes common functionality like logging, error handling, and agent configuration.
"""

import logging
from typing import Dict, Any, Optional, List
from crewai import Agent
from langchain_openai import ChatOpenAI
from app.config import settings


class BaseAgent:
    """Base class for all content creation agents"""
    
    def __init__(self, name: str, role: str, goal: str, verbose: bool = True):
        """
        Initialize base agent
        
        Args:
            name: Agent name
            role: Agent role description
            goal: Agent's primary goal
            verbose: Whether to enable verbose logging
        """
        self.name = name
        self.role = role
        self.goal = goal
        self.verbose = verbose
        self.logger = logging.getLogger(f"agent.{name.lower()}")
        
        # Initialize OpenAI LLM
        self.llm = ChatOpenAI(
            model=settings.openai_model,
            api_key=settings.openai_api_key,
            temperature=0.7
        )
        
        # Create CrewAI agent
        self.agent = Agent(
            role=role,
            goal=goal,
            verbose=verbose,
            llm=self.llm,
            allow_delegation=False
        )
    
    def execute_task(self, task_description: str, context: Optional[Dict[str, Any]] = None) -> str:
        """
        Execute a task with the agent
        
        Args:
            task_description: Description of the task to execute
            context: Additional context for the task
            
        Returns:
            str: Task execution result
        """
        try:
            self.logger.info(f"Executing task: {task_description}")
            
            # Prepare task input
            task_input = task_description
            if context:
                task_input += f"\n\nContext: {context}"
            
            # Execute task using CrewAI agent
            result = self.agent.execute_task(task_input)
            
            self.logger.info(f"Task completed successfully")
            return result
            
        except Exception as e:
            self.logger.error(f"Error executing task: {str(e)}")
            raise
    
    def get_agent_info(self) -> Dict[str, Any]:
        """
        Get agent information
        
        Returns:
            Dict containing agent details
        """
        return {
            "name": self.name,
            "role": self.role,
            "goal": self.goal,
            "verbose": self.verbose
        }
    
    def validate_input(self, input_data: Any) -> bool:
        """
        Validate input data for the agent
        
        Args:
            input_data: Data to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        # Base validation - can be overridden by subclasses
        if not input_data:
            return False
        return True
    
    def preprocess_input(self, input_data: str) -> str:
        """
        Preprocess input data before task execution
        
        Args:
            input_data: Raw input data
            
        Returns:
            str: Preprocessed input data
        """
        # Base preprocessing - can be overridden by subclasses
        return input_data.strip()
    
    def postprocess_output(self, output_data: str) -> str:
        """
        Postprocess output data after task execution
        
        Args:
            output_data: Raw output data
            
        Returns:
            str: Postprocessed output data
        """
        # Base postprocessing - can be overridden by subclasses
        return output_data.strip() 